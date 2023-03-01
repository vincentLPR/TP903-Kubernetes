from os import environ
from flask import Flask, jsonify
import logging

app = Flask('motd')

app.logger.setLevel(logging.DEBUG)

MESSAGE = environ.get("MESSAGE", "this is a fallback message")
PORT = int(environ.get("PORT", "8080"))

app.logger.info("message is [{}]".format(MESSAGE))
app.logger.info("listen port is [{}]".format(PORT))

@app.get('/')
def get_motd():
    return jsonify({"message": MESSAGE})

if __name__ == '__main__':
    
    app.run(debug=True, port=PORT, host="0.0.0.0")
