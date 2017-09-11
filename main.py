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
    return str(get_diaries(user_id))

@app.route('/user/<user_id>/diary', methods=['POST'])
def post_new_diary(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        # TODO: this should be a 404 or something similar
        return 'user_id must be an integer'
    data = json.loads(request.data)

    # Check if an entry already exists for date
    if get_diary_by_date(user_id, date['date']):
        return 'diary for this user and date already exists'

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
    data = json.loads(request.data)
    # TODO how do we deal with conflicting dates?
    update_diary(user_id, diary_id, data.get('date', None), data.get('timeIntoBed', None),
                 data.get('timeOutOfBed', None), data.get('sleepQuality', None))
    return 'put_specific_diary'

@app.route('/user/<user_id>/diary/<diary_id>', methods=['DELETE'])
def delete_diary(user_id, diary_id):
    try:
        user_id = int(user_id)
        diary_id = int(diary_id)
    except ValueError:
        # TODO: this should be a 404 or something similar
        return 'user_id and diary_id must be integers'
    remove_diary(user_id, diary_id)
    return 'delete_diary'
