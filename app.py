from flask import Flask, request, render_template
from logica import automata

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/logica', methods=['POST'])
def logica():
    data = request.get_json()
    st = data.get('st')

    return automata.q0(st)


if __name__ == '__main__':
    app.run()
