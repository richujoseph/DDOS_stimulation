from flask import Flask, render_template, Response
import time

app = Flask(__name__, template_folder=r'C:\Users\SJCET\Downloads\New folder\project-folder\templates')



# Variable to track request count
request_count = 0
THRESHOLD = 100  # Number of requests before server returns 503

@app.route("/")
def home():
    global request_count

    # Simulate server overload
    request_count += 1
    if request_count > THRESHOLD:
        return Response("503 Service Unavailable: Server is overloaded!", status=503)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)
