from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_special_chars, use_numbers, exclude_chars):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    
    if use_lowercase:
        characters += string.ascii_lowercase
    
    if use_special_chars:
        characters += string.punctuation
    
    if use_numbers:
        characters += string.digits

    if exclude_chars:
        characters = characters.translate(str.maketrans('', '', exclude_chars))
    
    if not characters:
        return "Error: You must select at least one character type."
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        length = int(request.form['length'])
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_special_chars = 'special_chars' in request.form
        use_numbers = 'numbers' in request.form
        exclude_chars = request.form['exclude_chars']
        
        password = generate_password(length, use_uppercase, use_lowercase, use_special_chars, use_numbers, exclude_chars)
        return render_template('index.html', password=password, default_length=length, default_exclude_chars=exclude_chars)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
