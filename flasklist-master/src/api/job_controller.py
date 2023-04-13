from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.job_serializer import job_request, job_result, job_employee_result
from src.services.job_service import create, change, delete, get, get_job_employee, get_all
 

ns = api.namespace('api/job', description='Operations related to job')

@ns.route('')#define rota
class JobCollection(Resource):
    @api.expect(job_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(job_result)#define resultado da metodo 
    def post(self):
        """
        Create a new Job
        """ 
        job = create(request.json)
        return job 
    
    
@ns.route('/<int:id>/post')
class JobEmployeeCollection(Resource):
    @api.marshal_with(job_employee_result)
    def get(self,id):
        """
        Get employee with job by ID
        """
        job = get_job_employee(id)
        return job




    @api.marshal_with(job_result)#define resultado da metodo 
    def get(self):
        """
        Get all job
        """
        job_list = get_all()
        return job_list

 

@ns.route('/<int:id>')
class JobIDCollection(Resource): 
    @api.marshal_with(job_result)
    def get(self, id):
        """
        Get job by ID
        """ 
        job = get(id)
        return job 


    @api.expect(job_request)
    @api.marshal_with(job_result)
    def put(self, id):
        """
        Change job by ID
        """ 
        job = change(id,request.json)
        return job
 
    @api.marshal_with(job_result)
    def delete(self, id):
        """
        Delete job by ID
        """ 
        job = delete(id)
        return job 