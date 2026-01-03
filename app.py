import os
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# --- CONFIGURATION ---
# Response hamesha yahi link dikhayega
FIXED_LINK = "https://earnlinks.in/MGENo"

@app.route('/api', methods=['GET', 'POST'])
def finalize_api():
    # User ka input (API Key, URL, Alias) server receive karega
    # Agar alias khali hai (jaise aapne example diya), toh bhi koi problem nahi
    try:
        api_param = request.args.get('api')
        url_param = request.args.get('url')
        alias_param = request.args.get('alias')
    except:
        pass

    # EXACT JSON RESPONSE
    # Ye wahi format hai jo aapne manga tha
    response_data = {
        "status": "success",
        "message": "",
        "shortenedUrl": FIXED_LINK
    }

    # JSON format mein response return karna
    res = make_response(jsonify(response_data))
    res.headers['Content-Type'] = 'application/json'
    return res

# Error hone par bhi wahi fixed success response dikhao
@app.errorhandler(404)
@app.errorhandler(500)
def handle_errors(e):
    return jsonify({
        "status": "success",
        "message": "",
        "shortenedUrl": FIXED_LINK
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
