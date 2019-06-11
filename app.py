from flask import Flask, render_template, request
# from CarDetect import client,get_id
import requests
import pymysql
from flask_sqlalchemy  import SQLAlchemy
import flask_mysqldb

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/mydb"
app.config["SQLALCHEMY_ECHO"] = True
fdb = SQLAlchemy(app)
# 数据库类
class Car_id(fdb.Model):
    id = fdb.Column(fdb.Integer, primary_key=True)
    name = fdb.Column(fdb.String(128), unique=False)
    serial_id = fdb.Column(fdb.Integer, unique=False)
    type_id = fdb.Column(fdb.Integer, unique=False)

# 必须启动数据库navicat
db = pymysql.connect("localhost", "root", "123456", "mydb")
cursor = db.cursor()

serial_api = "http://apis.haoservice.com/lifeservice/car/GetModel/"
type_api = "http://apis.haoservice.com/lifeservice/car"


param = {"key": "d22ad5453ce14ae18dc9c07c220321a5", "id": id}

@app.route('/index', methods=["GET", "POST"])
def index():
    """
    定义首页路由函数
    :return:
    """
    if request.method == "POST":
        print(request.values)
    fdb.create_all()
    cid = Car_id(name="test", serial_id=25, type_id=27)
    # fdb.session.add(cid)
    # cid.name = "test2"
    fdb.session.commit()
    d = Car_id.query.get(1)
    d.name = "test2"
    fdb.session.commit()
    cursor.execute("select * from carserialid")
    car_names = cursor.fetchall()

    # db.commit()
    return render_template("index.html",  car_name=car_names)

@app.route("/serial/<int:ser>")
def serial(ser):
    out = Car_id.query.get(1)
    print(out)
    # if request.method == "GET":
    #     #     建立数据库
    #     cursor.execute("create table if not exists cartype (name varchar (128), car_type)")
    #     num = cursor.execute("select * from cartype where car_type=%d" % (ser))
    #     if num == 0:
    #         param["id"] = ser
    #         resp = requests.get(serial_api, params=param)
    #         car_id = resp.json()
    #         id_content = get_id(car_id)
    #         print(id_content)
    #         for i in id_content:
    #             cursor.execute("insert into cartype(name, car_type) values ('%s', %d)" % (i['N'], i['I']))
    #         db.commit()
    #     else:
    #         ret = cursor.fetchall()

    return render_template("serial.html")

@app.route("/type/<int:car_t>")
def car_type(car_t):
    return render_template("type.html")

@app.route("/param/<int:car_p>")
def car_param(car_p):
    return render_template("param.html")


if __name__ == '__main__':
    app.run(debug=True)
    db.commit()
    cursor.close()
    db.close()
