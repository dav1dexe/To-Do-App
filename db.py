import sqlite3
from datetime import datetime
from os import environ
import time


environ['TZ'] = 'Asia/Dubai'
time.tzset()


class Database:
    dt = datetime.now().strftime('%d/%m/%Y')
    database = 'database.db'
    connection = sqlite3.connect(database, check_same_thread=False)
    cursor = connection.cursor()

    '''Регистрирует пользователя'''
    def add_user(self, username, password_hash, time=dt):
        with self.connection:
            return self.cursor.connection.execute(
                'INSERT INTO users (username, hash, datetime) VALUES (?, ?, ?)', (username, password_hash, time)
            )

    '''Проверяет данные от пользователя'''
    def check_data(self, login):
        with self.connection:
            return self.cursor.connection.execute(
                'SELECT id, username, hash, datetime FROM users WHERE username = ?', (login,)).fetchone()

    '''Добавляет новую запись'''
    def add_post(self, login, title, text):
        with self.connection:
            return self.cursor.connection.execute(
                'INSERT INTO posts (username, title, text) VALUES (?, ?, ?)', (login, title, text))

    '''Показывает посты по имени'''
    def get_posts(self, login):
        with self.connection:
            return self.cursor.connection.execute(
                'SELECT title, text FROM posts WHERE username = ?', (login,)).fetchall()
