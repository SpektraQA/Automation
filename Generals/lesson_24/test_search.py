import logging
import sys
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"
ALL_FIELDS = {"brand", "year", "engine_volume", "price"}
TOTAL_CARS_IN_DB = 25

logger = logging.getLogger("tes_search")
logger.setLevel(logging.DEBUG)
logger.propagate = False

_formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

_file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
_file_handler.setLevel(logging.DEBUG)
_file_handler.setFormatter(_formatter)

_console_handler = logging.StreamHandler(sys.stdout)
_console_handler.setLevel(logging.INFO)
_console_handler.setFormatter(_formatter)

if not logger.handlers:
    logger.addHandler(_file_handler)
    logger.addHandler(_console_handler)

class TestCarsSearch:
    @pytest.fixture(scope="class", autouse=True)
    @classmethod
    def auth_session(cls, request):
        session = requests.Session()

        logger.info("Авторизація користувача '%s' на %s/auth", USERNAME, BASE_URL)
        try:
            response = session.post(
                f"{BASE_URL}/auth",
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                timeout=5,
            )
        except requests.exceptions.ConnectionError as exc:
            logger.error("Не вдалось підключитись до сервера: %s", exc)
            pytest.fail(
                "Сервер Flask недоступний на http://127.0.0.1:8080. "
                "Запустіть 'python cars_app.py' перед тестами."
            )

        assert response.status_code == 200, (
            f"Аутентифікація не пройшла: {response.status_code}, {response.text}"
        )
        access_token = response.json()["access_token"]
        session.headers.update({"Authorization": f"Bearer {access_token}"})

        logger.info("Токен отримано, сесія авторизована")
        cls.session = session

        yield session

        logger.info("Закриття сесії після завершення тестів класу")
        session.close()

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 3),
            ("engine_volume", 10),
            ("brand", 1),
            (None, 7),
            ("price", None),
            ("year", 25),
        ],
        ids=[
            "sort_by_price-limit_5",
            "sort_by_year-limit_3",
            "sort_by_engine_volume-limit_10",
            "sort_by_brand-limit_1",
            "no_sort_by-limit_7",
            "sort_by_price-no_limit",
            "sort_by_year-limit_full_db",
        ],
    )

    def test_search_cars(self, sort_by, limit):
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit
        logger.info("GET /cars з параметрами: %s", params)
        response = self.session.get(f"{BASE_URL}/cars", params=params, timeout=5)
        logger.info("Статус відповіді: %s", response.status_code)
        logger.debug("Тіло відповіді: %s", response.text)

        assert response.status_code == 200, (
            f"Неочікуваний статус: {response.status_code}, тіло: {response.text}"
        )
        cars = response.json()
        assert isinstance(cars, list), "Відповідь має бути списком автомобілів"
        if limit is not None:
            assert len(cars) <= limit, (
                f"Очікувалось не більше {limit} записів, отримано {len(cars)}"
            )
        else:
            assert len((cars)) == TOTAL_CARS_IN_DB, (
            f"Без limit очікувались усі {TOTAL_CARS_IN_DB} записів, отримано {len(cars)}"
        )
        for car in cars:
            assert ALL_FIELDS <= set(car.keys()), f"Відсутні поля в записі: {car}"

        effective_sort_field = sort_by if sort_by is not None else "brand"
        values = [car[effective_sort_field] for car in cars]
        assert values == sorted(values), (
            f"Записи не відсортовані за '{effective_sort_field}': {values}"
        )
        logger.info(
            "Тест пройдено: отримано %d запис(ів), відсортовано за '%s'",
            len(cars), effective_sort_field,
        )

