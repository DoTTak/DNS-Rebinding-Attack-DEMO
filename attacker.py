import json
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    referer = request.headers.get('Referer', 'Unknown')
    host = request.headers.get('Host', 'Unknown')

    first_host = None
    target_host = None

    if "-" in host:
        parts = host.split("-")
        if len(parts) > 2:
            first_host = parts[1]
            target_host = parts[2]

    if referer != 'Unknown':
        return f"DNS Rebinding...({first_host} to {target_host})"
    else:
        return render_template("index.html", rebind_info={
            "first_host": first_host,
            "target_host": target_host
        })

@app.route("/tracking", methods=["POST"])
def tracking():
    data = json.loads(request.data.decode())['data']
    print(f"Receive >> {data}")
    return {"data": data}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)