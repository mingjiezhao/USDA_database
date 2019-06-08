import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1] 
curs.execute(query)
names = [f[0] for f in curs.description]

print(sys.argv[1])
for row in curs.fetchall():
	for pair in zip(names, row):
		print('%s: %s' % pair)
	print