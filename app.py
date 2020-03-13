# flask untuk membuat API
# render template untuk memungkinkan API memberikan respon berupa HTML
# request : untk menerima data yang dikirim dari browser
from flask import Flask, render_template, request

app = Flask(__name__)

# home
@app.route('/')
def index() :
    return '<h1> Hello Flask ~</h1>'

@app.route('/base')
def base():
    name = 'Angel'
    todo = ['Running', 'Swimming', 'McD']
    return render_template('base.html', name=name) 

# error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
















# saat kita running file app.py maka variable __name__ akan berisi string 'main'
if __name__ == '__main__' :
    # debug = True memiliki dua efek :
    # 1. setiap kita memperbaharui kode, api akan restart secara otomatis
    # 2. memungkinkan menampilkan pesan error di browser sehingga mudah dibaca
    app.run(debug=True)