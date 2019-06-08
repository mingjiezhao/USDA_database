import sqlite3

def convert(value):
	if value.startswith('~'):
		return value.strip('~')
	if not value:
		value = '0'
	return(value)

conn=sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute(
	'''
	CREATE TABLE food(
	NDB_No	TEXT	PRIMARY KEY,
	FdGrp_Cd	TEXT,
	Long_Desc	TEXT,
	Shrt_Desc	TEXT,
	ComName	TEXT,
	ManufacName	TEXT,
	Survey	TEXT,
	Ref_desc	TEXT,
	Refuse		REAL,
	SciName	TEXT,
	N_Factor 	REAL,
	Pro_Factor	REAL,
	Fat_Factor	REAL,
	CHO_Factor	REAL
	)
	''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

for line in open('FOOD_DES.txt'):
	fields = line.split('^')
	vals = [convert(f) for f in fields]

	curs.execute(query, vals)

conn.commit()
conn.close()