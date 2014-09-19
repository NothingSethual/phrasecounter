from flask import Flask, render_template, request
import re
import string
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def app_page():
    if request.method == 'POST':
        entries = text_to_counted_phrases(
            request.form['text'],
            int(request.form['num_words']))
        return render_template('output.html', entries=entries)
    else:
        return render_template('input.html')


def remove_punctuation(s):
    regex1 = re.compile('[%s]' % re.escape(string.punctuation))
    regex2 = re.compile('[%s]' % re.escape("\n"))
    s2 = regex1.sub('', s)
    return regex2.sub(' ', s2)


def clean(s):
    return remove_punctuation(s).casefold()


def list_phrases(words, num):
    return set(" ".join(words[i:i+num]) for i in range(len(words))
               if len(words[i:i+num]) == num)


def count_phrases(phrases, text):
    return set(map(lambda p: (text.count(p), p), phrases))


def text_to_counted_phrases(text, num_words):
    words = clean(text).split()
    phrases = list_phrases(words, num_words)
    return sorted(count_phrases(phrases, " ".join(words)), reverse=True)


if __name__ == '__main__':
    app.run(debug=True)
