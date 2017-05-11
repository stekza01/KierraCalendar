@app.route('/')
def hello():
	return render_template('mainScreen.html')
