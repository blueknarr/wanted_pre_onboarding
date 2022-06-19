from app import db
from sqlalchemy.orm import relationship


class Company(db.Model):
    __tablename__='company'
    id = db.Column(db.String(30), primary_key=True)
    country = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(20), nullable=False)


class JobPosting(db.Model):
    __tablename__ = 'job_posting'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.String(20), db.ForeignKey('company.id', ondelete='CASCADE'))
    job_position = db.Column(db.String(20), nullable=False)
    bonus = db.Column(db.Integer, nullable=False)
    job_description = db.Column(db.Text(), nullable=False)
    tech_stack = db.Column(db.String(20), nullable=False)
    company = relationship('Company', lazy='joined')


class ApplicationHistory(db.Model):
    __tablename__ = 'application_history'
    id = db.Column(db.Integer, primary_key=True)
    job_posting_id = db.Column(db.Integer, db.ForeignKey('job_posting.id', ondelete='CASCADE'))
    user_id = db.Column(db.String(20), db.ForeignKey('users.id'))
    job_posting = relationship('JobPosting', lazy='joined')


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(30), primary_key=True)


