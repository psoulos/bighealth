import sqlite3
import os
from flask import Flask, g

app = Flask(__name__)

DATABASE = './Diary.db'

INSERT = 'INSERT INTO diary(userId,date_,timeIntoBed,timeOutOfBed,sleepQuality) VALUES(?, ?, ?, ?, ?)'
GET = 'SELECT * FROM diary WHERE userId=?'
UPDATE = 'UPDATE diary SET %s WHERE userId=? AND id=?'
DELETE = 'DELETE FROM diary where userId=? AND id=?'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))
    db.row_factory = make_dicts
    return db

# TODO: confirm how closing database connection works with the flask framework
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    if os.path.isfile(DATABASE):
        print('Database already exists, skipping init')
        return
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        db.close()

def insert_new_diary(user_id, date, timeIntoBed, timeOutOfBed, sleepQuality):
    db = get_db()
    cursor = db.cursor()
    values = (user_id, date, timeIntoBed, timeOutOfBed, sleepQuality)
    cursor.execute(INSERT, values)
    db.commit()

def get_diaries(user_id):
    '''
    Returns all diaries for the given user as a list where each row is a dictionary with keys as defined in schema.sql
    An empty list is returned if there are no matching rows.
    '''
    db = get_db()
    cursor = db.cursor()
    values = (user_id,)
    cursor.execute(GET, values)
    return cursor.fetchall()

def update_diary(user_id, diary_id, date=None, timeIntoBed=None, timeOutOfBed=None, sleepQuality=None):
    # TODO: what if an entry already exists for the new date?
    # date, time into bed, time out of bed, sleep quality

    # Create the set string and values to update the database
    set_string = ''
    values = ()

    if not date == None:
        set_string += 'date_=?'
        values += (date,)

    if not timeIntoBed == None:
        if set_string:
            set_string += ','
        set_string += 'timeIntoBed=?'
        values += (timeIntoBed,)

    if not timeOutOfBed == None:
        if set_string:
            set_string += ','
        set_string += 'timeOutOfBed=?'
        values += (timeOutOfBed,)

    if not sleepQuality == None:
        if set_string:
            set_string += ','
        set_string += 'sleepQuality=?'
        values += (sleepQuality,)

    values += (user_id, diary_id)

    print('Set string: %s' % set_string)
    print('Values: %s' % str(values))

    db = get_db()
    cursor = db.cursor()
    update = UPDATE % set_string
    cursor.execute(update, values)
    db.commit()

def remove_diary(user_id, diary_id):
    db = get_db()
    cursor = db.cursor()
    values = (user_id, diary_id)
    cursor.execute(DELETE, values)
    db.commit()
