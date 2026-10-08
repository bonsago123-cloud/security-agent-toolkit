from flask import Flask, request

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.get_json()

    print("event 값:", event)
    print("event 자료형:", type(event))

    if "rule" in event:
        return {"status": "ok", "rule": event["rule"]}, 200
    else:
        return {"status": "ok"}, 200


app.run(port=5002)
