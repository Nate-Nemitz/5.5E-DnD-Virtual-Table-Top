import sqlite3

class db_skills():
    def create_char_table():
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_characters( 
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        Level INTEGER,
        str INTEGER,
        dex INTEGER,
        con INTEGER,
        int INTEGER,
        wis INTEGER,
        cha INTEGER,
        acrobatics REAL DEFAULT 0,
        animal_handling REAL DEFAULT 0,
        arcana REAL DEFAULT 0,
        athletics REAL DEFAULT 0,
        deception REAL DEFAULT 0,
        history REAL DEFAULT 0,
        insight REAL DEFAULT 0,
        intimidation REAL DEFAULT 0,
        investigation REAL DEFAULT 0,
        medicine REAL DEFAULT 0,
        nature REAL DEFAULT 0,
        perception REAL DEFAULT 0,
        performance REAL DEFAULT 0,
        persuasion REAL DEFAULT 0,
        religion REAL DEFAULT 0,
        sleight_of_hand REAL DEFAULT 0,
        stealth REAL DEFAULT 0,
        survival REAL DEFAULT 0
        ''')
    def write_char_column():
        cursor.execute('''
        INSERT OR IGNORE INTO test_characters(
        id, name, str, dex, con, int, wis, cha)VALUES(
        1,'Luke', 16,  14,  15,  10,  12,  8)
        ''')
    def read_char_columns():
        cursor.execute("SELECT * FROM test_characters WHERE name='Luke'")

def char_creation():
    conn=sqlite3.connect("character_skill_test.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()

    db_skills.create_char_table()
    db_skills.write_char_column()
    db_skills.read_char_columns()

    conn.commit()
    Luke=cursor.fetchone()
    conn.close()
    return Luke

char_creation()

#test print for data retrieval
print(f"Name: {Luke['name']}")
print(f"Strength: {Luke['str']}")
print(f"Dexterity: {Luke['dex']}")
print(f"Constitution: {Luke['con']}")
print(f"Intelligence: {Luke['int']}")
print(f"Wisdom: {Luke['wis']}")
print(f"Charisma: {Luke['cha']}")