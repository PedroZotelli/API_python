from src.models import db
from src.models.employee import Employee
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de author e incluir um apelido ao get para evitar conflito com o get do post
from src.services.job_service import get as get_job

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do Employee
###

def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400,"text is required")

        job_id = data.get('job_id')
        if not job_id:
            json_abort(400,"job_id is required")

        birthday = data.get('birthday')
        if not birthday:
            json_abort(400,"birthday is required")
        
        salary = data.get('salary')
        if not salary:
            json_abort(400,"salary is required")
        
        department = data.get('department')
        if not department:
            json_abort(400,"department is required")


        job = get_job(job_id)

        employee = Employee(name=name,job_id=job_id,job = job,birthday=birthday ,salary=salary,department=department)
        db.session.add(employee)
        db.session.commit()

        return employee

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        employee = Employee.query.filter_by(id=id).first()

        if not employee:
            json_abort(400,"Post not found")
        else:
            return employee

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_all():
    try:
        employee = Employee.query.all()

        if not employee:
            json_abort(400,"Posts not found")
        else:
            return employee

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_employee_jobhistory(id):
    try:
        employee = Employee.query.filter_by(id=id).first()
        employee.listEmployee = Employee.query.filter_by(job_id=id).all()
        
        if not employee:
            json_abort(400,"Job not found")
        else:
            return employee

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        employee = Employee.query.filter_by(id=id).first()

        if not employee:
            json_abort(400,"Post not found")
        else:

            name = data.get('name')
        if not name:
            json_abort(400,"text is required")

        birthday = data.get('birthday')
        if not birthday:
            json_abort(400,"birthday is required")
        
        salary = data.get('salary')
        if not salary:
            json_abort(400,"salary is required")
        
        department = data.get('department')
        if not department:
            json_abort(400,"department is required")

        employee.name = name
        employee.birthday = birthday
        employee.salary = salary
        employee.department = department
        
        db.session.commit()
        
        return employee

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        employee = Employee.query.filter_by(id=id).first()

        if not employee:
            json_abort(400,"Post not found")
        else:
            db.session.delete(employee)
            db.session.commit()
        
            return employee

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)