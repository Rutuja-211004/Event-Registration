from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key'

participants = []
users = {'admin': 'admin'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid Credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html', participants=participants)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        participant = {
            'name': request.form['name'],
            'event': request.form['event'],
            'project': request.form['project']
        }
        participants.append(participant)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        participants[index] = {
            'name': request.form['name'],
            'event': request.form['event'],
            'project': request.form['project']
        }
        return redirect(url_for('dashboard'))
    return render_template('edit.html', participant=participants[index], index=index)

@app.route('/delete/<int:index>')
def delete(index):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    participants.pop(index)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
