from src.models import db
from src.models.jobhistory import JobHistory
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de author e incluir um apelido ao get para evitar conflito com o get do post
from src.services.employee_service import get as get_employee

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do Employee
###

def create(data):
    try:

        title = data.get('title')
        if not title:
            json_abort(400,"text is required")

        employee_id = data.get('employee_id')
        if not employee_id:
            json_abort(400,"job_id is required")

        startDate = data.get('startDate')
        if not startDate:
            json_abort(400,"startDate is required")
            
        salary = data.get('salary')
        if not salary:
            json_abort(400,"salary is required")
        
        endDate = data.get('endDate')
        if not endDate:
            json_abort(400,"endDate is required")
        
        job = data.get('job')
        if not job:
            json_abort(400,"job is required")


        employee = get_employee(employee_id)

        jobhistory = JobHistory(title=title,employee_id=employee_id,employee=employee,startDate=startDate,salary=salary,endDate=endDate,job=job)
        db.session.add(jobhistory)
        db.session.commit()

        return jobhistory

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        jobhistory = JobHistory.query.filter_by(id=id).first()

        if not jobhistory:
            json_abort(400,"jobhistory not found")
        else:
            return jobhistory

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_all():
    try:
        jobhistory = JobHistory.query.all()

        if not jobhistory:
            json_abort(400,"JobHistory not found")
        else:
            return jobhistory

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        jobhistory = JobHistory.query.filter_by(id=id).first()

        if not jobhistory:
            json_abort(400,"jobhistory not found")
        else:

            title = data.get('title')
        if not title:
            json_abort(400,"text is required")

        startDate = data.get('startDate')
        if not startDate:
            json_abort(400,"startDate is required")
        
        salary = data.get('salary')
        if not salary:
            json_abort(400,"salary is required")
            
        endDate = data.get('endDate')
        if not endDate:
            json_abort(400,"endDate is required")
        
        job = data.get('job')
        if not job:
            json_abort(400,"job is required")

        jobhistory.title = title
        jobhistory.startDate = startDate
        jobhistory.salary = salary
        jobhistory.endDate = endDate
        jobhistory.job = job
        
        db.session.commit()
        
        return jobhistory

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        jobhistory = JobHistory.query.filter_by(id=id).first()

        if not jobhistory:
            json_abort(400,"jobhistory not found")
        else:
            db.session.delete(jobhistory)
            db.session.commit()
        
            return jobhistory

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)