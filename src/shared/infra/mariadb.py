import mariadb

config = {
    'host' : 'localhost',
    'port' : 3308,
    'user' : 'root',
    'password' : '',
    'database' : 'estudiantes',
}

DB = mariadb.connect(**config)
DB.autocommit = True