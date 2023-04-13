from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.employee_serializer import employee_result


job_request = api.model('Job Request', {
    'name': fields.String(required=True, description='name post') ,
    'description': fields.String(required=True, description='description post')
    
})

job_result = api.model('Job Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'name': fields.String(required=True, description='name post'), 
    'description': fields.String(required=True, description='description post')

})

job_employee_result = api.model('Job Post Result', {
    'id' : fields.Integer(required=True, description='Post Id'),
    'name': fields.String(required=True, description='name post'), 
    'description': fields.String(required=True, description='description post'),
    'listEmployee' : fields.List(fields.Nested(employee_result), description='list posts')
})
