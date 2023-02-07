from flask import Flask, request, render_template, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'dklfsghls;d/'

# 首页
@app.route('/index')
def index():
    return render_template('index.html')

# 名字全称应用
@app.route('/name', methods=['POST', 'GET'])
def fullname():
    return render_template("name.html")

@app.route('/result', methods=['POST', 'GET'])
def result_name():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    full_name = firstname.title() + ' ' + lastname.title()
    return render_template("result.html", name=full_name)

# 元音字母词频统计
@app.route('/vowels', methods=['POST', 'GET'])
def words():
    return render_template("vowels.html")

@app.route('/results', methods=['POST', 'GET'])
def result_word():
    word = request.form.get("word")
    vowels = request.form.get("vowels")
    py_found = {}
    for i in word:
        if i in vowels:
            # 初始化 setdefault
            py_found.setdefault(i, 0)
            py_found[i] += 1
    for r in py_found:
        k = r
        v = py_found[r]
    return render_template("vowels_result.html",
                           key=k,
                           found=v
                           )

# 购物车
@app.route('/shop', methods=['POST', 'GET'])
def shopping():
    products = [
        ("纸巾", " 30¥"),
        ("纯牛奶", " 60¥"),
        ("可乐", " 5¥"),
        ("水杯", " 36¥"),
        ("雨伞", " 15¥"),
        ("香甜吐司", " 15¥"),
        ("梳子", " 8¥"),
        ("月球灯", " 48¥"),
        ("暖手宝", " 38¥"),
        ("香氛灯", " 56¥"),
        ("迷你小风扇", "34¥")
    ]
    return render_template('shopping.html', products=products)

@app.route('/list', methods=['POST', 'GET'])
def submit():
    return render_template('shopping_list.html')

@app.route('/final', methods=['POST', 'GET'])
def last():
    return render_template("final.html")

# 404错误页面
@app.errorhandler(404)
def page_not_fount(error):
    return render_template('error.html'), 404

# 505错误页面
@app.errorhandler(500)
def internal_server_error(error):
    return 'Datebase connection failed', 500


if __name__ == '__main__':
    app.run(debug=True)