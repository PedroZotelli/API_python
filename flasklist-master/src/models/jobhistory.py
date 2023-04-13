from . import db
from .employee import Employee

#configura modelo de dados do JobHistory
class JobHistory(db.Model):
    __tablename__ = 'jobhistory'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(
        db.Integer, db.ForeignKey('employee.id', ondelete='CASCADE'))
    employee = db.relationship('Employee')
    title = db.Column(db.String(255))
    startDate = db.Column(db.String(255))
    salary = db.Column(db.Float(10,2))
    endDate = db.Column(db.String(255))
   
    job = db.Column(db.String(255))

    def __str__(self):
        return self.title
    
    def get_jobhistory_id(self):
        return self.id
    
