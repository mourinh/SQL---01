import sqlite3
conexao = sqlite3.connect('sqlatt_att')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE cliente (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	cpf TEXT,
	data_de_cadastro TEXT,
	endereco TEXT
);
''')
conexao.commit()
conexao.close()
