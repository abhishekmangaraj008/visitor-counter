from flask import Flask

app = Flask(__name__)

visits = 0

@app.route("/")
def index():
    global visits
    visits += 1
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Visitor Counter</title>
</head>
<body>
    <h1>Welcome to the Real-World DevOps App!</h1>
    <p>Visited {visits} times.</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
