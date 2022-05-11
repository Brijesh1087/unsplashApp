from flask import Flask,request,render_template,redirect
import sqlite3,time,os,requests,threading
app = Flask(__name__)

key = "sdiwereriweruwe87485723^^^&&*(9r83"
# home
@app.route("/")
def home():
	return render_template("index.html")

# downlaod
@app.route("/download/<img>")
def urls(img):
	url = f"https://pixabay.com/get/{img}"
	res = requests.get(url).content
	with open(f"static/Download_IMG/{url[-15::]}","wb") as file:
		file.write(res)
		file.close()
	th_1 = threading.Thread(target=delete,args=(url[-15::],))
	th_1.start()
	return render_template("index.html",url=f"/static/Download_IMG/{url[-15::]}")
	
def delete(url):
	print("deleting...",url)
	time.sleep(5)
	os.remove(f"static/Download_IMG/{url}")


app.run(debug=True)
