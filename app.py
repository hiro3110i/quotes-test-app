from flask import Flask, render_template
import random

app = Flask(__name__)

# 格言を読み込む
def load_quotes():
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes]  # 改行を削除してリストに格納

@app.route('/')
def index():
    quotes = load_quotes()
    random_quote = random.choice(quotes)  # ランダムに1つの格言を選ぶ
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234, debug=False)
