from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask import request, jsonify
from marshmallow import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:PG123@localhost/Contactosdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cellnumber = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Contact {self.name}>'

ma = Marshmallow(app)

class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        load_instance = True

@app.route('/contact', methods=['GET'])
def get_contacts():
    all_records = request.args.get('all', type=bool, default=False)
    if all_records:
        # Retorna todos los contactos sin paginación
        contacts = Contact.query.all()
        contact_schema = ContactSchema(many=True)
        return jsonify(contact_schema.dump(contacts))
    else:
        # Paginación
        page = request.args.get('page', 1, type=int)
        page_size = request.args.get('page_size', 10, type=int)
        contacts_query = Contact.query.paginate(page=page, per_page=page_size, error_out=False)
        contacts = contacts_query.items
        contact_schema = ContactSchema(many=True)
        return jsonify(contact_schema.dump(contacts))


@app.route('/contact/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get_or_404(id)
    contact_schema = ContactSchema()
    return jsonify(contact_schema.dump(contact))

@app.route('/contact', methods=['POST'])
def create_contact():
    contact_schema = ContactSchema()
    try:
        contact = contact_schema.load(request.json)
        db.session.add(contact)
        db.session.commit()
        return jsonify(contact_schema.dump(contact)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@app.route('/contact/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    contact_schema = ContactSchema()
    updated_contact = contact_schema.load(request.json, instance=contact)
    db.session.commit()
    return jsonify(contact_schema.dump(updated_contact))

@app.route('/contact/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True)
    
