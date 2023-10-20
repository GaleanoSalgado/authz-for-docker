from flask import Flask, jsonify, request

app = Flask(__name__)
application = app


@app.route("/")
def index():
    return "Docker Authz Plugin"

@app.route("/Plugin.Activate", methods=['POST'])
def activate():
    return jsonify({'Implements': ['authz']})

@app.route("/AuthZPlugin.AuthZReq", methods=['POST'])
def authz_request():
    print("AuthZ Request")
    print(request.data)
    
    return {"Allow": True, "Msg":   "The request authorization succeeded."}

    # return {"Allow": False,
    #                 "Msg":   "The request authorization failed. You must say hello first",
    #                 "Err":   "You must say hello first."}


@app.route("/AuthZPlugin.AuthZRes", methods=['POST'])
def authz_response():
    print("AuthZ Response")
    response = {"Allow": True}
    return jsonify(**response)

if __name__ == "__main__":
    app.run()
