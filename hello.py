from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'POST':
		entries = sorted(text_to_counted_phrases(request.form['text'], int(request.form['num_words'])), reverse=True)
		return render_template('output.html', entries=entries)
	else:
		return render_template('input.html')

def remove_punctuation(s):
    import re, string
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    return regex.sub('', s)

def clean(s):
    return remove_punctuation(s).casefold()

def list_phrases(words, num):
    return [" ".join(words[i:i+num]) for i in range(len(words)) if len(words[i:i+num]) == num]

def count_phrases(phrases, text):
    return set(map(lambda p: (text.count(p), p), phrases))

def text_to_counted_phrases(text, num_words):
    clean_text = clean(text)
    words = clean_text.split()
    phrases = list_phrases(words, num_words)
    return count_phrases(phrases, clean_text)

if __name__ == '__main__':
    app.run(debug=True)

# TODO: Make work with line endings