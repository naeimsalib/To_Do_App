from flask import Flask, render_template,requests
app = Flask (__name__, template_folder='template')

@app.route("/")
def website():
	return render_template('website.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, threaded=True)

cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}

r = requests.post('https://hunter-todo-api.herokuapp.com', cookies=cookies)
