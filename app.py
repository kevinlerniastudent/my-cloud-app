from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h1>Enter your name</h1>
        <form action="/greet">
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/greet")
def greet():
    name = request.args.get("name", "stranger")
    return f"<h1>Hello from Azure {name}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 

   
