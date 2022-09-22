from flask_mongoengine import MongoEngine
db = MongoEngine()

class Student(db.Document):
  name = db.StringField()
  email = db.StringField()

  def to_json(self):
    return {
      'name': self.name,
      'email': self.email,
    }



class StudentQuery:
  def __init__(self):
    pass

  def save(data):
    student = Student()
    student.name = data['name']
    student.email = data['email']
    return student.save()

  def find_all():
    students = Student.objects()
    return students