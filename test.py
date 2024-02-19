import pytest
from main import StudentsInMLOps

def test_enroll_students():
    school = StudentsInMLOps()
    school.enrollStudents(5)
    assert school.getTotalStrength() == 5

def test_drop_students():
    school = StudentsInMLOps()
    school.enrollStudents(10)
    school.dropStudents(3)
    assert school.getTotalStrength() == 7

def test_get_class_name():
    school = StudentsInMLOps()
    assert school.getClassName() == "MLOps"
