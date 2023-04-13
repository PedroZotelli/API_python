from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.employee_serializer import employee_request, employee_result,employee_jobhistory_result
from src.services.employee_service import create, change, delete, get, get_employee_jobhistory, get_all
 

ns = api.namespace('api/employee', description='Operations related to employee')

@ns.route('/<int:id>/post')
class EmployeeJobHistoryCollection(Resource):
    @api.marshal_with(employee_jobhistory_result)
    def get(self,id):
        """
        Get enplyee whit job by ID
        """
        job = get_employee_jobhistory(id)
        return job

@ns.route('')#refine rota
class EmployeeCollection(Resource):
    @api.expect(employee_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(employee_result)#define resultado da metodo 
    def post(self):
        """
        Create a new employee
        """ 
        employee = create(request.json)
        return employee 
    
    @api.marshal_with(employee_result)#define resultado da metodo 
    def get(self):
        """
        Get all employees
        """
        employee = get_all()
        
        return employee


 

@ns.route('/<int:id>')
class EmployeeIDCollection(Resource): 
    @api.marshal_with(employee_result)
    def get(self, id):
        """
        Get employee by ID
        """ 
        employee = get(id)
        return employee 


    @api.expect(employee_request)
    @api.marshal_with(employee_result)
    def put(self, id):
        """
        Change employee by ID
        """ 
        employee = change(id,request.json)
        return employee 
 
    @api.marshal_with(employee_result)
    def delete(self, id):
        """
        Delete employee by ID
        """ 
        employee = delete(id)
        return employee