# $pip install bcrypt
import random
import sqlite3
#import bcrypt

def main():
    db = sqlite3.connect('passwords.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user
                   (user_id, user_name, user_password)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS password
                   (user_id, password)''')
    db.commit()
    db.close()
    


## add database
## add hashing + salting
## GUI


def generate_password(n_lower=6, n_upper=4, n_num=3, n_sym=3):
    password = []
    password.extend(random.choices(ABC_LOWER, k=n_lower))
    password.extend(random.choices(ABC_UPPER, k=n_upper))
    password.extend(random.choices(NUMBERS, k=n_num))
    password.extend(random.choices(SYMBOLS, k=n_sym))
    
    random.shuffle(password)
    return "".join(password)


def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())
     

def check_password(password, hash):
    return bcrypt.checkpw(password, hash)


if __name__ == "__main__":
    ABC_LOWER = list("abcdefghijklmnopqrstuvwxyz")
    ABC_UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    NUMBERS = list("0123456789")
    SYMBOLS = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
    main()
    