import sqlite3

def conectar():
    conn = sqlite3.connect("dados.db")
    conn.execute("PRAGMA foreign_keys = ON")

    return conn, conn.cursor()

def criar_tabelas():
    conn, cursor = conectar()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                carga_horaria INTEGER,
                nivel TEXT
                )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                curso_id INTEGER,
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
                )
    """)

    conn.commit()
    conn.close()
