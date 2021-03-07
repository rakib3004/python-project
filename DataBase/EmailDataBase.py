import sqlite3
connection = sqlite3.connect('email.sqlite')
current = connection.cursor()

current.execute('''
DROP TABLE IF EXISTS Department''')

current.execute('''
CREATE TABLE Department(DeptName Text, StuNo INTEGER )''')

fileName = input('Enter File Name')