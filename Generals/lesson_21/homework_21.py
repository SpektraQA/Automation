import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg://postgres:mysecretpassword@localhost:5432/school_db")

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    courses = relationship("Course", secondary=student_course, backref="students")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


if session.query(Course).count() == 0:
    courses = [
        Course(title="Math"),
        Course(title="Physics"),
        Course(title="History"),
        Course(title="Biology"),
        Course(title="English")
    ]
    session.add_all(courses)
    session.commit()

fake = Faker()

if session.query(Student).count() ==0:
    all_courses = session.query(Course).all()

    for _ in range(20):
        student = Student(name=fake.name())
        student.courses = random.sample(all_courses, k=random.randint(1,3))
        session.add(student)

    session.commit()

course = session.query(Course).filter(Course.title == "Math").first()
print(f"Студенти на курсі {course.title}:")
for student in course.students:
    print(student.name)

student = session.query(Student).filter(Student.name == "Jonathan Boyd Jr.").first()
print(f"Курси студента {student.name}:")
for course in student.courses:
    print(course.title)

student_to_update = session.query(Student).filter(Student.name == "Jonathan Boyd Jr.").first()
student_to_update.name = "Jonathan Boyd Jr."
session.commit()

student_to_delete = session.query(Student).filter(Student.name == "Jonathan Boyd Jr.").first()
session.delete(student_to_delete)
session.commit()