from flask import Flask, render_template, Response

app = Flask(__name__, template_folder=r"C:\Users\user\DDOS_stimulation\project-folder\templates")

# Global request count (not thread-safe)
request_count = 0
THRESHOLD = 100  # Number of requests before returning 503

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
