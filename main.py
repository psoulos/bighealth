from flask import Flask
app = Flask(__name__)

@app.route('/user/<user_id>/diaries', methods=['GET'])
def get_user_diares(user_id):
    # Return a list of all diary entries for a user
    return 'get_user_diares'

@app.route('/user/<user_id>/diary', methods=['POST'])
def post_new_diary(user_id):
    return 'post_new_diary'

@app.route('/user/<user_id>/diary/<diary_id>', methods=['PUT'])
def put_update_diary(user_id, diary_id):
    return 'put_specific_diary'

@app.route('/user/<user_id>/diary/<diary_id>', methods=['DELETE'])
def delete_diary(user_id, diary_id):
    return 'delete_diary'
