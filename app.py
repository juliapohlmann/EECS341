from flask import Flask, render_template, json, request, session, redirect
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
# from gevent.wsgi import WSGIServer

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abc123'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

@app.route('/showAdmin')
def showAdmin():
    return render_template('admin.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/addCurator', methods=['POST'])
def addCurator():
	_name = request.form['inputCuratorName']
	_expertise = request.form['inputExpertise']
	_startDate = request.form['inputCuratorStartDate']
	_endDate = request.form['inputCuratorEndDate']
	
	try:
		connection = mysql.connect()
		cursor = connection.cursor()
		cursor.callproc('addcurator',(_name, _expertise, _startDate, _endDate))
		returned_data = cursor.fetchall()

		if len(returned_data) == 0:
			connection.commit()
			return json.dumps({'message':'Success in adding new curator'})
		else:
			return json.dumps({'error':str(returned_data)})
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/addPiece', methods=['POST'])
def addPiece():
	_pieceType = request.form['inputPieceType']
	_artist = request.form['inputArtist']
	_dateCreated = request.form['inputDateCreated']
	_desc = request.form['inputDesc']
	try:
		connection = mysql.connect()
		cursor = connection.cursor()
		cursor.callproc('addpiece',(_pieceType, _artist, _dateCreated, _desc))
		returned_data = cursor.fetchall()

		if len(returned_data) == 0:
			connection.commit()
			return json.dumps({'message':'Success in creating new piece'})
		else:
			return json.dumps({'error':str(returned_data)})
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/addExhibit', methods=['POST'])
def addExhibit():
	_exhibitStartDate = request.form['inputExhibitStartDate']
	_exhibitEndDate = request.form['inputExhibitEndDate']
	_location = request.form['inputLocation']
	_name = request.form['inputExhibitName']
	try:
		connection = mysql.connect()
		cursor = connection.cursor()
		cursor.callproc('addexhibit',(_exhibitStartDate, _exhibitEndDate, _location, _name))
		returned_data = cursor.fetchall()

		if len(returned_data) == 0:
			connection.commit()
			return json.dumps({'message':'Success in creating new exhibit'})
		else:
			return json.dumps({'error':str(returned_data)})
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/signUp', methods=['POST'])
def signUp():
	_username = request.form['inputUsername']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	try:
		if _username and _email and _password:
			connection = mysql.connect()
			cursor = connection.cursor()
			_hash_pw = generate_password_hash(_password)
			cursor.callproc('createUser',(_username, _email, _hash_pw))
			returned_data = cursor.fetchall()

			if len(returned_data) == 0:
				connection.commit()
				return json.dumps({'message':'Success in creating user'})
			else:
				return json.dumps({'error':str(returned_data)})
		else:
			return json.dumps({'html':'<span>Please fill in all neccessary fields</span>'})

	except Exception as ex:
		return json.dumps({'error':str(ex)+' hashed password: ' + _hash_pw})
	finally:
		cursor.close()
		connection.close()

@app.route('/signIn', methods=['POST'])
def signIn():
	# return json.dumps({'message':'Success in creating user'})

	try:
		_username = request.form['inputUsername']
		_password = request.form['inputPassword']

		connection = mysql.connect()
		cursor = connection.cursor()
		cursor.callproc('signin', (_username,))
		returned_array = cursor.fetchall()
		data = returned_array[0]

		# return json.dumps({'got here':str(data)})

		if len(data) == 3:
			# return json.dumps({'got here': 'aalskdjfklajs'})
			if check_password_hash(str(data[2]), _password):
				session['user'] = data[0]
				# return json.dumps({'got here': 'aalskdjfklajs'})
				return json.dumps({'good':'logged in!'})
				# return render_template('index.html')
				# target = '/'
				# return redirect(url_for(target))
				# console.log("abcdefgh")
				# return redirect(url_for('answer_page.html'))
				# return render_template('index.html')
				# redirect(url_for('index.html'))
				# main()
				# redirect('index.html')
				# render_template('signin.html')
				# return redirect('/showSignUp')
				# return json.dumps({'message':'All good'})
			else:
				return json.dumps({'error1':'Wrong password or user name'})
		else:
			return json.dumps({'error2':'Wrong password or user name'})
	except Exception as ex:
		return json.dumps({'error2':str(ex)})
	finally:
		cursor.close()
		connection.close()


    # except Exception as e:
    #     return render_template('error.html',error = str(e))
    # finally:
    #     cursor.close()
    #     connection.close()
	# _username = request.form['inputUsername']
	# _password = request.form['inputPassword']
	# try:
	# 	if _username and _password:
	# 		connection = mysql.connect()
	# 		cursor = connection.cursor()
	# 		cursor.callproc('signin',(_username))
	# 		returned_data = cursor.fetchall()

	# 		if len(returned_data) > 0:
	# 			if check_password_hash(str(data[0][3]), _password):
	# 				session['user'] = data[0][0]
	# 				return json.dumps({'message':'Success in creating user'})
	# 				# return redirect('/')
	# 			else:
	# 				return json.dumps({'html':'<span>Wrong username or password</span>'})
	# 		else:
	# 			return json.dumps({'html':'<span>Wrong username or password</span>'})
	# except Exception as ex:
	# 	return json.dumps({'error':str(ex)})
	# finally:
	# 	cursor.close()
	# 	connection.close()

if __name__ == "__main__":
	app.debug = True
	# threaded=True, 
	app.run(port=5000)
	# http_server = WSGIServer(('', 5000), app)
	# http_server.serve_forever()



