from . import db
from .job import Job

#configura modelo de dados do Employee
class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(
        db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))
    job = db.relationship('Job')
    name = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    salary = db.Column(db.Float(10,2))
    department = db.Column(db.String(255))
    
    def get_employee_id(self):
        return self.id
    
    def __str__(self):
        return self.name
