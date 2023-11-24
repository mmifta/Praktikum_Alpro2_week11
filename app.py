from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


default_messages2 = [
    "Makan patty itu SpongeBob",
    "Berdansalah, Patrick",
    "Mari menangkap ubur-ubur",
    "Hidup memang tidak adil, jadi biasakan dirimu kawan.",
    "Imagination",
    "Ayo makan krabby patty",
    "Aku siap, aku siap!",
    "Sebenarnya aku takut naik wahana ini, tapi aku tidak ingin membuatmu kecewa.",
    "Ternyata semua yang berkilau itu belum tentu emas",
    "Hiduplah seperti Larry"
]

@app.route('/')
def index():
    return render_template('index.html', message2=None)

@app.route('/random_message', methods=['GET', 'POST'])
def get_random_message():
    if request.method == 'GET':
        nama = request.args.get('nama')
        if nama:
            message2 = f"{nama}, {random.choice(default_messages2)}"
            return jsonify(message2)
        else:
            return jsonify(random.choice(default_messages2))
    
    elif request.method == 'POST':
        nama = request.form.get('nama')
        if nama:
            message = f"Selamat Datang, {nama}, Anda berhasil masuk ke Puja Kerang Ajaib"
            return jsonify(message)       
        else:
            return jsonify(message=None)       
        

if __name__ == '__main__':
    app.run(debug=True)
