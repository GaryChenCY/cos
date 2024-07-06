import pymongo
client=pymongo.MongoClient("mongodb+srv://gary:gary1217@atlascluster.vhmlc4e.mongodb.net/")
db=client.member_system
print("資料庫連線成功")


from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="any string but secret"

@app.route("/")
def home():
    return render_template("signin.html")

@app.route("/register")
def index():
    return render_template("register.html")

@app.route("/member") #在這邊需要加入一個Session來記錄會員資料，以防別人直接登進自己的會員路由頁面
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg", "發生錯誤訊息，請聯繫客服")
    return render_template("error.html", message=message)


@app.route("/signup", methods=["POST"]) #這部份很重要!建出一個路由給登入
def signup():
    nickname=request.form["nickname"] #從前端接收資訊
    email=request.form["email"]
    password=request.form["password"]
    phonenumber=request.form["phonenumber"]
    
    collection=db.user #根據接收到的資料與資料庫互動
    #檢查會員集合中是否有相同email資料
    result=collection.find_one({
        "email":email
    })
    if result !=None:
        return redirect("/error?msg=信箱已經被註冊")
    #把資料放入資料庫完成註冊
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password,  #還得再塞入幾筆資料 待完成!
        "phonenumber":phonenumber
    })
    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    #從前端取得使用者的輸入
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user #合資料庫互動
    #檢查信箱密碼是否正確
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    #找不到對應的資料，登入失敗，導向錯誤頁面
    if result==None:
        return redirect("/error?msg=帳號密碼輸入錯誤")
    session["nickname"]=result["nickname"] #在Session紀錄會員資訊
    return redirect("/member") #登入成功，導入會員頁面

@app.route("/signout")
def signout():
    del session["nickname"] #移除Session中的會員資料
    return redirect("/") #並跳回登入頁面

app.run(port=3000)

""" 需新增項目 """
#推上git
#解決登入、註冊點擊not found的問題
#需要手機或email傳送驗證
#新增美化前端網頁
#上傳商品圖