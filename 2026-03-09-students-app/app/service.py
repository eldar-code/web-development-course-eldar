# application logic
import db

def add_student(student):
    return db.add_student(student)


def get_students():
    return db.get_students()


def get_student(student_id):
    return db.get_student(student_id)


def update_student(student_update):
    return db.update_student(student_update)


def delete_student(student_id):
    return db.delete_student(student_id)
