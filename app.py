import subprocess, sqlite3

# BAD: Hardcoded credentials
DB_PASSWORD = "admin123"
API_KEY     = "sk-1234abcdef"

def get_user(username):
    conn = sqlite3.connect('u.db')
       # BAD: SQL injection
    q  = "SELECT * FROM users"
    q += f" WHERE u='{username}'"
    return conn.execute(q).fetchall()

def run_cmd(user_input):
    # BAD: Shell injection
    subprocess.call(
        'ls ' + user_input,
        shell=True)