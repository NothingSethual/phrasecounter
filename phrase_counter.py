from flask import Flask, render_template, request
import re
import string
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def app_page():
    if request.method == 'POST':
        num_words = int(request.form['num_words'] or 4)
        text = request.form['text'] or "Try entering some text. Try entering some text."
        text_title = request.form['text_title'] or "your text"
        entries = text_to_counted_phrases(text, num_words)
        if len(entries) < 10:
            chart_title = "Phrase frequency"
        else:
            chart_title = "Phrase frequency (top 10)"
        return render_template('output.html',
                               entries=entries, chart_title=chart_title,
                               text_title=text_title, num_words=num_words)
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
    app.run()
