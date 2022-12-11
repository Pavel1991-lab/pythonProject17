from utils import load_candidates, get_all, get_by_pk, get_by_skill
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    candit = load_candidates()
    result = '<br>'
    for cand in candit:
        result += cand['name'] + '<br>'
        result += cand['position'] + '<br>'
        result += cand['skills'] + '<br>'
        result += '<br>'
    return f'<pre>{result}<pre/>'

@app.route("/candidate/<int:pk>")
def get_candit_by_pk(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return 'Кандидат не найден'

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'


    return f'''
        <img src="{candidate['picture']}">
        <pre>{result}<pre/>
    '''



@app.route("/candidate/<skill>")
def get_candit_by_skill(skill):
    candidates = get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f'<pre>{result}<pre/>'



if __name__ == '__main__':
    app.run(debug=True)