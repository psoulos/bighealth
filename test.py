import requests
import os

# This assumes flask is running on the default port
HOST = 'http://127.0.0.1:5000/'

# TODO: test_get should be updated to check for valid JSON matching the test db
def test_get():
    url = os.path.join(HOST, 'user/-1/diaries')
    res = requests.get(url)
    if res.status_code != 200 or res.text != 'get_user_diares -1':
        raise Exception('test_get failed')

def test_get_fail_invalid_userid():
    url = os.path.join(HOST, 'user/hello/diaries')
    res = requests.get(url)
    if res.text != 'user id must be an integer':
        raise Exception('test_get_fail_invalid_userid failed')

# test_post needs to be updated to include JSON data to post
def test_post():
    url = os.path.join(HOST, 'user/-1/diary')
    res = requests.post(url)
    if res.status_code != 200 or res.text != 'post_new_diary':
        raise Exception('test_post failed')

def test_put():
    url = os.path.join(HOST, 'user/-1/diary/-1')
    res = requests.put(url)
    if res.status_code != 200 or res.text != 'put_specific_diary':
        raise Exception('test_put failed')

def test_delete():
    url = os.path.join(HOST, 'user/-1/diary/-1')
    res = requests.delete(url)
    if res.status_code != 200 or res.text != 'delete_diary':
        raise Exception('test_delete failed')

def test_all():
    test_get()
    test_post()
    test_put()
    test_delete()

if __name__ == "__main__":
    test_all()
