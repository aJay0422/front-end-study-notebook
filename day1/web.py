from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")   # 默认即为templates


# 创建了网址 /show/info 和 函数index 的对应关系
@app.route("/show/info")
def index():
    # return "<span style='color: red;'>中国</span>联通"
    # Flask 内部自动打开文件，并读取内容，将内容返回给用户
    # 默认：取当前项目目录的templates文件夹中找
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("get_news.html")

@app.route("/goods/list")
def goods_list():
    return render_template("goods_list.html")

@app.route("/user/list")
def user_list():
    return render_template("user_list.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run()
