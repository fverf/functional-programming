from flask import Flask, request, jsonify, abort
import string, random

app = Flask(__name__)
db = {}

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/short-url/<short_url>', methods=['GET'])
def get_url(short_url):
    if short_url in db:
        return jsonify({'url': db[short_url]})
    return abort(404)

@app.route('/normal-url', methods=['POST'])
def create_url():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        return abort(400)
    short_url = generate_short_url()
    db[short_url] = original_url
    return jsonify({'short_url': short_url})

@app.route('/short-url/<short_url>', methods=['PUT'])
def update_url(short_url):
    if short_url not in db:
        return abort(404)
    data = request.get_json()
    new_url = data.get('url')
    if not new_url:
        return abort(400)
    db[short_url] = new_url
    return jsonify({'message': 'URL updated'})

@app.route('/short-url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
    if short_url in db:
        del db[short_url]
        return jsonify({'message': 'URL deleted'})
    return abort(404)

if __name__ == '__main__':
    app.run(port=5000)