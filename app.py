from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Путь к файлу для сохранения email (можно заменить на БД)
EMAILS_FILE = 'emails.txt'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email and '@' in email:
        # Сохраняем email в файл
        with open(EMAILS_FILE, 'a', encoding='utf-8') as f:
            f.write(email + '\n')
        flash('Спасибо за подписку! 💌', 'success')
    else:
        flash('Пожалуйста, введите корректный email.', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Создаём файл, если не существует
    if not os.path.exists(EMAILS_FILE):
        open(EMAILS_FILE, 'w').close()
    app.run(debug=True, host='0.0.0.0', port=5000)