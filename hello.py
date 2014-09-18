from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'POST':
		text = request.form['text']
		return render_template('output.html', text=text)
	else:
		return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)