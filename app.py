from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    events = pd.read_csv('event.csv').to_dict(orient='records')
    return render_template('home.html', events=events)

@app.route('/register/<event_id>', methods=['GET', 'POST'])
def register(event_id):
    events = pd.read_csv('event.csv')
    event = event[event['Event ID'] == event_id].iloc[0]

    if request.method == 'POST':
        name = request.form['participant']
        contact = request.form['contact']

        new_data = pd.DataFrame([{
            'Event ID': event_id,
            'Event Name': event['Event Name'],
            'Participant': name,
            'Contact': contact
        }])

        # Check if the Excel file exists
        file_path = 'data.xlsx'
        if os.path.exists(file_path):
            # Load existing data and append
            existing_data = pd.read_excel(file_path)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            # No file exists, use new data
            updated_data = new_data

        # Save to Excel file
        updated_data.to_excel(file_path, index=False)

        return redirect(url_for('home'))

    return render_template('register.html', event_id=event_id)

@app.route('/participants/<event_id>')
def participants(event_id):
    file_path = 'data.xlsx'
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        event_participants = df[df['Event ID'] == event_id].to_dict(orient='records')
    else:
        event_participants = []

    return render_template('participants.html', event_id=event_id, participants=event_participants)

if __name__ == '__main__':
    app.run(debug=True)
