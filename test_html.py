import pymysql
from flask import Flask

app=Flask(__name__)
@app.route("/show/info")
def index():
  return "1.html"

if __name__=='__main__':
  app.run()

# conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123" , database="unicom",charset='utf8')
# cursor = conn.cursor()
#
# cursor.execute("insert into admin(username,password,mobile) values('def','def123','13888888888')")
# conn.commit()
# cursor.close()
# conn.close()

