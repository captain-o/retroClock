from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Function to write data to a JSON file
def write_to_json(time, weekdays):
    data = {
        "id": len(get_json_data()) + 1,
        "time": time,
        "weekdays": weekdays
    }

    current_data = get_json_data()
    current_data.append(data)

    with open('data.json', 'w') as json_file:
        json.dump(current_data, json_file, indent=4)

# Function to read data from the JSON file
def get_json_data():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as json_file:
            json.dump([], json_file)

    with open('data.json', 'r') as json_file:
        return json.load(json_file)

# Function to remove an entry by ID
def remove_entry_by_id(entry_id):
    current_data = get_json_data()
    updated_data = [entry for entry in current_data if entry["id"] != entry_id]

    with open('data.json', 'w') as json_file:
        json.dump(updated_data, json_file, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_time = request.form['time']
        selected_weekdays = request.form.getlist('weekday')
        write_to_json(user_time, selected_weekdays)
        return redirect(url_for('index'))

    # Read data from the JSON file to display on the page
    data = get_json_data()

    return render_template('index.html', data=data)

@app.route('/remove/<int:entry_id>', methods=['POST'])
def remove_entry(entry_id):
    remove_entry_by_id(entry_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
