from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def oauth_redirect():
    code = request.args.get('code')
    # Now you can exchange `code` for an access token
    # Remember to perform the exchange server-side and keep your client secret secure
    return "Authorization code: " + code

if __name__ == "__main__":
    app.run(port=3000)
