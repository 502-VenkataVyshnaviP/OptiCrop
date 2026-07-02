# OptiCrop - Smart Agriculture Management System
# Main Application File

from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('opticrop.db')
    cursor = conn.cursor()
    
    # Create crops table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            variety TEXT,
            planting_date TEXT,
            expected_harvest TEXT,
            location TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create weather data table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop_id INTEGER NOT NULL,
            temperature REAL,
            humidity REAL,
            rainfall REAL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (crop_id) REFERENCES crops(id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to OptiCrop!"})

@app.route('/crops', methods=['GET'])
def get_crops():
    conn = sqlite3.connect('opticrop.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM crops')
    crops = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(crops)

@app.route('/crops', methods=['POST'])
def add_crop():
    data = request.json
    conn = sqlite3.connect('opticrop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO crops (name, variety, planting_date, expected_harvest, location)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['name'], data['variety'], data['planting_date'], 
          data['expected_harvest'], data['location']))
    
    conn.commit()
    conn.close()
    return jsonify({"message": "Crop added successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)