from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        user = request.form.get("username")
        pwd = request.form.get("password")
        gender = request.form.get("gender")
        hobby_list = request.form.get("hobby")
        city = request.form.get("city")
        areas_list = request.form.get("areas")
        remark = request.form.get("remark")
        print(user, pwd, gender, hobby_list, city, areas_list, remark)
        return "Successfully Registered"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        user = request.form.get("username")
        pwd = request.form.get("password")
        return "Successfully logged in"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()