from src.models import db
from src.models.job import Job
from src.models.employee import Employee
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do Job
###

def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400," Name is required")

        description = data.get('description')
        if not description:
            json_abort(400,"Descrition is required")

        #chama objeto para gravar no banco
        job = Job(name=name,description=description)
        db.session.add(job)
        db.session.commit()

        return job

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        job = Job.query.filter_by(id=id).first()

        if not job:
            json_abort(400,"Job not found")
        else:
            return job

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def get_all():
    try:
        
        job = Job.query.all()

        if not job:
            json_abort(400, "Job not found")
        else:
            return job

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error) 



def get_job_employee(id):
    try:
        job = Job.query.filter_by(id=id).first()
        job.listEmployee = Employee.query.filter_by(job_id=id).all()
        
        if not job:
            json_abort(400,"Job not found")
        else:
            return job

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        job = Job.query.filter_by(id=id).first()

        if not job:
            json_abort(400,"Job not found")
        else:

            name = data.get('name')
            if not name:
                json_abort(400,"Name is required")

            description = data.get('description')
            if not description:
                json_abort(400,"Description is required")

        

            job.name = job.name
            job.description = description
            
            db.session.commit()
        
            return job

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        job = Job.query.filter_by(id=id).first()

        if not Job:
            json_abort(400,"Job not found")
        else:
            db.session.delete(job)
            db.session.commit()
        
            return job

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)