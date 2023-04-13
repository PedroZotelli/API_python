from . import db 

#configura modelo de dados do JOB
class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def get_user_id(self):
        return self.id
    
    def __str__(self):
        return self.name

    

