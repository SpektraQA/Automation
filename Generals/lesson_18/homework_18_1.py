import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(search_url, params=search_params)

data = response.json()
items = data["collection"]["items"]
nasa_ids = []
for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

for index, nasa_id in enumerate(nasa_ids[:2], start=1):
    asset_url = asset_url_template.format(nasa_id=nasa_id)
    asset_response = requests.get(asset_url)
    asset_items = asset_response.json()["collection"]["items"]

    jpg_links = []
    for asset_item in asset_items:
        href = asset_item["href"]
        if href.endswith(".jpg"):
            jpg_links.append(href)

    chosen_jpg = jpg_links[0]
    image_response = requests.get(chosen_jpg)

    filename = f"mars_photo{index}.jpg"
    with open(filename, "wb") as f:
        f.write(image_response.content)