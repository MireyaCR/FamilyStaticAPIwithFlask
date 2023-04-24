"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import Family
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = Family("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    member = request.get_json()
    if not member:
        return jsonify({"error": "No member provided"}), 400
    
    first_name = member.get("first_name")
    age = member.get("age")
    lucky_numbers = member.get("lucky_numbers", [])
    member_id = member.get("id", jackson_family._generateId())

    new_member = {
        "id": member_id,
        "first_name": first_name,
        "last_name": jackson_family.last_name,
        "age": age,
        "lucky_numbers": lucky_numbers
    }

    jackson_family.add_member(new_member)

    return jsonify(), 200

def delete_member(member_id):
  
    member = next((m for m in family['members'] if m['id'] == member_id), None)
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
 
    family['members'].remove(member)

    return jsonify({'done': True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
