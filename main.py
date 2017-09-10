import json
from flask import Flask, request

from database import *

app = Flask(__name__)

@app.before_first_request
def bootup():
    init_db()

@app.route('/user/<user_id>/diaries', methods=['GET'])
def get_user_diares(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        # TODO: this should be a 404 or something similar
        return 'user_id must be an integer'

    # Return a list of all diary entries for a user
    return 'get_user_diares %s' % user_id

@app.route('/user/<user_id>/diary', methods=['POST'])
def post_new_diary(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        # TODO: this should be a 404 or something similar
        return 'user_id must be an integer'
    data = json.loads(request.data)
    # TODO: check if an entry already exists for date
    insert_new_diary(user_id, data['date'], data['timeIntoBed'], data['timeOutOfBed'], data['sleepQuality'])
    return 'post_new_diary'

@app.route('/user/<user_id>/diary/<diary_id>', methods=['PUT'])
def put_update_diary(user_id, diary_id):
    try:
        user_id = int(user_id)
        diary_id = int(diary_id)
    except ValueError:
        # TODO: this should be a 404 or something similar
        return 'user_id and diary_id must be integers'
    return 'put_specific_diary'

@app.route('/user/<user_id>/diary/<diary_id>', methods=['DELETE'])
def delete_diary(user_id, diary_id):
    try:
        user_id = int(user_id)
        diary_id = int(diary_id)
    except ValueError:
        # TODO: this should be a 404 or something similar
        return 'user_id and diary_id must be integers'
    return 'delete_diary'
