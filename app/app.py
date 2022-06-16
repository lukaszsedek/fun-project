from flask import Flask, render_template, abort, jsonify
from flask_mysqlpool import MySQLPool
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASS'] = 'password'
app.config['MYSQL_DB'] = 'mysql'
app.config['MYSQL_POOL_NAME'] = 'mysql_pool'
app.config['MYSQL_POOL_SIZE'] = 5
app.config['MYSQL_AUTOCOMMIT'] = True

db = MySQLPool(app)


@app.route('/status')
def health_check():
    try:
        conn = db.connection.get_connection()  # get connection from pool
        #cursor = conn.cursor(dictionary=True)
        #cursor.execute("select * from world_x.city limit 10", )
        #result = cursor.fetchall()
        conn.close()  # return connection to pool
        return ('', 200)
    except mysql.connector.ProgrammingError as err:
        print(err)
        abort(500)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)