from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.jobhistory_serializer import jobhistory_request, jobhistory_result
from src.services.jobhistory_service import create, change, delete, get, get_all
 

ns = api.namespace('api/jobhistory', description='Operations related to jobhistory')


@ns.route('')#refine rota
class JobHistoryCollection(Resource):
    @api.expect(jobhistory_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(jobhistory_result)#define resultado da metodo 
    def post(self):
        """
        Create a new jobhistory
        """ 
        jobhistory = create(request.json)
        return jobhistory 
    
    @api.marshal_with(jobhistory_result)#define resultado da metodo 
    def get(self):
        """
        Get all jobhistory
        """
        jobhistory = get_all()
        
        return jobhistory


 

@ns.route('/<int:id>')
class JobHistoryIDCollection(Resource): 
    @api.marshal_with(jobhistory_result)
    def get(self, id):
        """
        Get jobhistory by ID
        """ 
        jobhistory = get(id)
        return jobhistory


    @api.expect(jobhistory_request)
    @api.marshal_with(jobhistory_result)
    def put(self, id):
        """
        Change jobhistory by ID
        """ 
        jobhistory = change(id,request.json)
        return jobhistory 
 
    @api.marshal_with(jobhistory_result)
    def delete(self, id):
        """
        Delete jobhistory by ID
        """ 
        jobhistory = delete(id)
        return jobhistory