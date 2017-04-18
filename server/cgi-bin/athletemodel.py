#!/usr/local/bin/python3

import sqlite3
from athletelist import AthleteList
import pickle

db_name = 'coachdata.sqlite'

def get_namesID_from_store():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    results = cursor.execute('SELECT name,id FROM athletes')
    response = results.fetchall()
    conn.close()
    return(response)

def get_names_from_store():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    results = cursor.execute('SELECT name FROM athletes')
    response = [ row[0] for row in results.fetchall() ]
    conn.close()
    return(response)

def get_athlete_from_id(athlete_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    results = cursor.execute('SELECT name, dob FROM athletes WHERE id=?', (athlete_id,))
    (name, dob) = results.fetchone()
    results = cursor.execute('SELECT value FROM timing_data WHERE athlete_id=?', (athlete_id,))
    data = sorted([row[0] for row in results.fetchall()])
    response = { 'Name': name,
                 'DOB': dob,
                 'data': data,
                 'top3': data[0:3]}
    conn.close()
    return(response)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return(AthleteList(temp1.pop(0), temp1.pop(0), temp1))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for file in files_list:
        athlete = get_coach_data(file)
        if athlete != None:
            all_athletes[athlete.name] = athlete
    return(all_athletes)
