from flask_sqlalchemy import SQLAlchemy
from app import app
import json

db = SQLAlchemy(app)

class Tech(db.Model):
	__tablename__= 'tech'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	nod = db.Column(db.Float, nullable=False)
	rank = db.Column(db.Integer, nullable=False)

	def add_tech(_name, _nod, _rank):
		new_tech = Tech(name=_name, nod=_nod, rank=_rank)
		db.session.add(new_tech)
		db.session.commit()

	def get_tech_by_rank(_rank):
		return Tech.convert_json(Tech.query.filter_by(rank=_rank).first())

	def get_all_tech():
		return [Tech.convert_json(tech) for tech in Tech.query.all()]

	def update_tech_name(_rank, _name):
		update_tech_object = Tech.query.filter_by(rank=_rank).first()
		update_tech_object.name = _name
		db.session.commit()

	def update_tech_nod(_rank, _nod):
		update_tech_object = Tech.query.filter_by(rank=_rank).first()
		update_tech_object.nod = _nod
		db.session.commit()

	def replace_tech(_rank, _name, _nod):
		replace_tech_object = Tech.query.filter_by(rank=_rank).first()
		replace_tech_object.name = _name
		replace_tech_object.nod = _nod
		db.session.commit()

	def delete_tech(_rank):
		is_success = Tech.query.filter_by(rank=_rank).delete()
		db.session.commit()
		return bool(is_success)

	def convert_json(self):
		return {'name':self.name, 'nod':self.nod, 'rank':self.rank, 'id': self.id}

	def __repr__(self):
		tech_object = {
		'name' : self.name,
		'nod' : self.nod,
		'rank' : self.rank,
		'id': self.id
		}
		return json.dumps(tech_object)