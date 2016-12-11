#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def check(answer):
    a = answer[0]
    b = answer[1]
    c = answer[2]
    print(a)
    print(b)
    print(c)


def insert(answer):
    name = answer[0]
    age = answer[1]
    hero = answer[2]
    print(name)
    print(age)
    print(hero)
    connect = lite.connect('bot.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO profile (first_name, age, fav_superhero) VALUES (?, ?, ?)', (name, age, hero))
    connect.commit()


#Метод поиска текста песни по названию песни
def find_lyrics(message):
    song = message
    connect = lite.connect('bot.db')
    cursor = connect.cursor()
    cursor.execute('SELECT text FROM lyrics WHERE song_name = ?', song)
    data = cursor.fetchall()
    return data

# def select(name):
#     cursor = connect.cursor()
#     cursor.execute('SELECT * FROM profile WHERE first_name = %s' % name)
#     data = cursor.fetchone()
#     return data

