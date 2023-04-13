from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.jobhistory_serializer import jobhistory_result


employee_request = api.model('Employee Request', {
    'job_id': fields.Integer(required=True, description='post job ID '),
    'name': fields.String(required=True, description='name'),
    'birthday' : fields.String(required=True, description='birthday'),
    'salary' : fields.Float(required=True, description='salary'),
    'department' : fields.String(required=True, description='department')

})

employee_result = api.model('Employee Result', {
    'id': fields.Integer(required=True, description='employee Id'),
    'name': fields.String(required=True, description='name text'),
    'job_id': fields.Integer(required=True, description='post job ID'),
    'birthday': fields.String(required=True, description='birthday'),
    'salary' : fields.Float(required=True, description='salary'),
    'department' : fields.String(required=True, description='department')
    
})

employee_jobhistory_result = api.model('Employee Result', {
    'id': fields.Integer(required=True, description='employee Id'),
    'name': fields.String(required=True, description='name text'),
    'job_id': fields.Integer(required=True, description='post job ID'),
    'birthday': fields.String(required=True, description='birthday'),
    'salary' : fields.Float(required=True, description='salary'),
    'department' : fields.String(required=True, description='department'),
    'listjobhistory' : fields.List(fields.Nested(jobhistory_result), description='list posts')
})