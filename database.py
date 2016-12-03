#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def insert(answer):
    name = answer[0]
    age = answer[1]
    hero = answer[2]
    connect = lite.connect('bot.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO profiles(first_name, age, fav_superhero) VALUES (%s, %s, %s)' % name, age, hero)

#
# def select(name):
#     cursor = connect.cursor()
#     cursor.execute('SELECT * FROM profile WHERE first_name = %s' % name)
#     data = cursor.fetchone()
#     return data

