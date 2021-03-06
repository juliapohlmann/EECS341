#app.py runs the application 
#created by Julia, Haley, Max

#import necessary packages
from flask import Flask, render_template, json, request, session, redirect
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

#MySQL setup 
mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abc123'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#initialize the application
mysql.init_app(app)


#routing functions, renders the template based on the route
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showHome")
def showHome():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')

@app.route('/showExhibitPage')
def showExhibitPage():
    return render_template('exhibit.html')

@app.route('/showDonorPage')
def showDonorPage():
    return render_template('donor.html')

@app.route('/showCuratorPage')
def showCuratorPage():
    return render_template('curator.html')

@app.route('/showAdmin')
def showAdmin():
    return render_template('admin.html')

@app.route('/showPiecePage')
def showPiecePage():
    return render_template('piece.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')


#routing functions that call stored procedures in database

#getCuratorsByExhibit
@app.route('/getCuratorsByExhibit', methods=['POST'])
def getCuratorsByExhibit():
	try:
        #get exhibit id from the serialized form
		_exhibit = request.form['exhibitSelectList']

        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getcuratorsbyexhibit',(_exhibit,))
		curators = cursor.fetchall()

        #return results
		curators_dict = []
		for curator in curators:
			curator_dict = {
					'Name': curator[0]}
			curators_dict.append(curator_dict)
		return json.dumps(curators_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})

#getCuratorsByExpertise
@app.route('/getCuratorsByExpertise', methods=['POST'])
def getCuratorsByExpertise():
	try:
        #get expertise from the serialized form
		_expertise = request.form['expertiseSelectList']

        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getcuratorsbyexpertise',(_expertise,))
		curators = cursor.fetchall()

        #return results
		curators_dict = []
		for curator in curators:
			curator_dict = {
					'Name': curator[0]}
			curators_dict.append(curator_dict)
		return json.dumps(curators_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})

#showAllExpertises
@app.route('/showAllExpertises')
def showAllExpertises():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getallexpertises',())
        expertises = cursor.fetchall()

        #return results
        expertises_dict = []
        for expertise in expertises:
            expertise_dict = {
                    'Expertise': expertise[0]}
            expertises_dict.append(expertise_dict)
        return json.dumps(expertises_dict)
        
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

#getCuratorsByDate
@app.route('/getCuratorsByDate', methods=['POST'])
def getCuratorsByDate():
	try:
        #get expertise from the serialized form
		_date = request.form['inputStartDate']

        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getcuratorsactiveondate',(_date,))
		curators = cursor.fetchall()

        #return results
		curators_dict = []
		for curator in curators:
			curator_dict = {
					'Name': curator[0],
					'Expertise': curator[1]}
			curators_dict.append(curator_dict)
		return json.dumps(curators_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/showCurrentCurators')
def showAllCurrentCurators():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getallcurrentcurators',())
        curators = cursor.fetchall()

        #return results
        curators_dict = []
        for curator in curators:
            curator_dict = {
                    'Name': curator[0],
                    'Expertise': curator[1]}
            curators_dict.append(curator_dict)
        return json.dumps(curators_dict)
        
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/showAllCurators')
def showAllCurators():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getallcurators',())
        curators = cursor.fetchall()

        #return results
        curators_dict = []
        for curator in curators:
            curator_dict = {
                    'Name': curator[0],
                    'Expertise': curator[1]}
            curators_dict.append(curator_dict)
        return json.dumps(curators_dict)
        
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getDonationsByDate', methods=['POST'])
def getDonationsByDate():
	try:
        #get field from serialized form
		_date = request.form['inputStartDate']

        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getdonationsbydate',(_date,))
		pieces = cursor.fetchall()

        #return results
		pieces_dict = []
		for piece in pieces:
			piece_dict = {
					'DonorName': piece[0],
					'PieceName': piece[1]}
			pieces_dict.append(piece_dict)
            # return json.dumps({'yay':str(exhibits_dict)})
		return json.dumps(pieces_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/showAllDonatedPieces')
def showAllDonatedPieces():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getallpiecesdonated',())
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Name': piece[0],
                    'Artist':piece[1]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error1':str(ex)})

@app.route('/showAllDonors')
def showAllDonors():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getalldonors',())
        donors = cursor.fetchall()

        #return results
        donors_dict = []
        for donor in donors:
            donor_dict = {
                    'Id': donor[0],
                    'Name': donor[1]}
            donors_dict.append(donor_dict)
        return json.dumps(donors_dict)
        
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getPieceLocation', methods=['POST'])
def getPieceLocation():
	try:
        #get field from serialized form
		_piece = request.form['pieceUnavailableSelectList']

        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getpiecelocation',(_piece,))
		pieces = cursor.fetchall()

        #return results
		pieces_dict = []
		for piece in pieces:
			piece_dict = {
					'ExhibitName': piece[0],
					'ExhibitLocation': piece[1]}
			pieces_dict.append(piece_dict)
		return json.dumps(pieces_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/getPiecesByTimePeriod', methods=['POST'])
def getPiecesByTimePeriod():
	try:
        #get fields from serialized form
		_startDate = request.form['inputStartDate']
		_endDate = request.form['inputEndDate']   

        #make connection and call process 	
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getpiecesintimerange',(_startDate,_endDate))
		pieces = cursor.fetchall()

        #return results
		pieces_dict = []
		for piece in pieces:
			piece_dict = {
					'Id': piece[0],
					'Name': piece[1],
					'Artist': piece[2]}
			pieces_dict.append(piece_dict)
		return json.dumps(pieces_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})

@app.route('/getPiecesByType', methods=['POST'])
def getPiecesByType():
    try:
        #get field from serialized form
    	_type = request.form.get('typeSelectList')

        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getpiecesbytype',(_type,))
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Name': piece[1],
                    'Artist':piece[2]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error1':str(ex)})

@app.route('/getPiecesByArtist', methods=['POST'])
def getPiecesByArtist():
    try:
        #get field from serialized form
    	_artist = request.form.get('artistSelectList')

        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getpiecesbyartist',(_artist,))
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Name': piece[1]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error1':str(ex)})

@app.route('/getArtists')
def getArtists():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getartists',())
        artists = cursor.fetchall()

        #return results
        artists_dict = []
        for artist in artists:
            artist_dict = {
                    'Artist': artist[0]}
            artists_dict.append(artist_dict)
        return json.dumps(artists_dict)
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getPieceById', methods=['POST'])
def getPieceById():
    try:
        #get field from serialized form
    	_piece = request.form.get('pieceSelectList')

        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getpiecebyid',(_piece,))
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Type': piece[1],
                    'Artist': piece[2],
                    'Date_Created': piece[3],
                    'Piece_Desc': piece[4],
                    'Available': piece[5],
                    'Name': piece[6]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error1':str(ex)})

@app.route('/showAllPieces')
def showAllPieces():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getallpieces',())
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Type': piece[1],
                    'Artist': piece[2],
                    'Date_Created': piece[3],
                    'Piece_Desc': piece[4],
                    'Available': piece[5],
                    'Name': piece[6]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
        
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getExhibitsByLocation', methods=['POST'])
def getExhibitsByLocation():
	try:
        #get field from serialized form
		_location = request.form.get('locationSelectList')

        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getexhibitbylocation',(_location,))
		exhibits = cursor.fetchall()

        #return results
		exhibits_dict = []
		for exhibit in exhibits:
			exhibit_dict = {
					'Id': exhibit[0],
					'Name': exhibit[1]}
			exhibits_dict.append(exhibit_dict)
		return json.dumps(exhibits_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})
    
@app.route('/getLocations')
def getLocations():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getlocations',())
        locations = cursor.fetchall()

        #return results
        locations_dict = []
        for location in locations:
            location_dict = {
                    'Location': location[0]
                    }
            locations_dict.append(location_dict)
        return json.dumps(locations_dict)
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getPiecesFromExhibitByType', methods=['POST'])
def getPiecesFromExhibitByType():
    try:
        #get fields from serialized form
    	_exhibit = request.form.get('exhibitSelectList1')
    	_type = request.form.get('typeSelectList')

        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getpiecesfromexhibitbytype',(_exhibit, _type))
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Name': piece[1],
                    'Artist': piece[2]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error1':str(ex)})

@app.route('/getPieceTypes')
def getPieceTypes():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getpiecetypes',())
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Type': piece[0]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error':str(ex)})
    
@app.route('/getExhibitsByTimeFrame', methods=['POST'])
def getExhibitsByTimeFrame():
	try:
        #get fields from serialized form
		_startDate = request.form['inputExhibitStartDate']
		_endDate = request.form['inputExhibitEndDate'] 

        #make connection and call process   	
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('getexhibitsbytimeframe',(_startDate,_endDate))
		exhibits = cursor.fetchall()

        #return results
		exhibits_dict = []
		for exhibit in exhibits:
			exhibit_dict = {
					'Id': exhibit[0],
					'Name': exhibit[1],
					'Location': exhibit[2],
					'Start Date': exhibit[3],
					'End Date': exhibit[4]}
			exhibits_dict.append(exhibit_dict)
		return json.dumps(exhibits_dict)
	except Exception as ex:
		return json.dumps({'error':str(ex)})


@app.route('/getPiecesFromExhibit', methods=['POST'])
def getPiecesFromExhibit():
    try:

    	_exhibit = request.form.get('exhibitSelectList2')

        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getpiecesfromexhibit',(_exhibit,))
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Name': piece[1],
                    'Artist': piece[2]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error1':str(ex)})

@app.route('/addPieceToExhibit', methods=['POST'])
def addPieceToExhibit():
	if session.get('user'):
        #get fields from serialized form
		_piece = request.form['pieceSelectList']
		_exhibit = request.form['exhibitSelectList']

		try:
            #make connection and call process
			con = mysql.connect()
			cursor = con.cursor()
			cursor.callproc('addpiecetoexhibit',(_exhibit, _piece))
			returned_data = cursor.fetchall()

            #return results
			if len(returned_data) == 0:
				connection.commit()
				return json.dumps({'message':'Success in adding piece to exhibit'})
			else:
				return json.dumps({'error':str(returned_data)})
		except Exception as ex:
			return json.dumps({'error':str(ex)})
	else:
		return json.dumps({'error':'Unauthorized access, please log in'})

@app.route('/showAllExhibits')
def showAllExhibits():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getallexhibits',())
        exhibits = cursor.fetchall()

        #return results
        exhibits_dict = []
        for exhibit in exhibits:
            exhibit_dict = {
                    'Name': exhibit[0],
                    'Location': exhibit[1], 
                    'Id': exhibit[2]}
            exhibits_dict.append(exhibit_dict)
        return json.dumps(exhibits_dict)
        
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getUnavailablePieces')
def getUnavailablePieces():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getunavailablepieces',())
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Name': piece[1],
                    'Artist': piece[2]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getAvailablePieces')
def getAvailablePieces():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getavailablepieces',())
        pieces = cursor.fetchall()

        #return results
        pieces_dict = []
        for piece in pieces:
            piece_dict = {
                    'Id': piece[0],
                    'Name': piece[1],
                    'Artist': piece[2]}
            pieces_dict.append(piece_dict)
        return json.dumps(pieces_dict)
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/getActiveExhibits')
def getActiveExhibits():
    try:
        #make connection and call process
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('getActiveExhibits',())
        exhibits = cursor.fetchall()

        #return results
        exhibits_dict = []
        for exhibit in exhibits:
            exhibit_dict = {
                    'Id': exhibit[0],
                    'Name': exhibit[1],
                    'Location': exhibit[2]}
            exhibits_dict.append(exhibit_dict)
        return json.dumps(exhibits_dict)
    except Exception as ex:
    	return json.dumps({'error':str(ex)})

@app.route('/logDonation', methods=['POST'])
def logDonation():
    if session.get('user'):
        try:
            #get fields from serialized form
            _donor = request.form.get('donorSelectList')
            _notes = request.form['inputNotes']
            _pieceType = request.form['inputDonorPieceType']
            _artist = request.form['inputDonorArtist']
            _dateCreated = request.form['inputDonorDateCreated']
            _desc = request.form['inputDonorDesc']
            _name = request.form['inputDonorPieceName']

            #make connection and call process
            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('addDonation',(_donor, _notes, _pieceType, _artist, _dateCreated, _desc, _name))
            returned_data = cursor.fetchall()

            #return results
            if len(returned_data) == 0:
                con.commit()
                return json.dumps({'message':'Success in creating new piece'})
            else:
                return json.dumps({'error':str(returned_data)})
        except Exception as ex:
            return json.dumps({'error':str(ex)})
    else:
        return json.dumps({'error':'Unauthorized access, please log in'})

@app.route('/addCurator', methods=['POST'])
def addCurator():
	if session.get('user'):
        #get fields from serialized form
		_name = request.form['inputCuratorName']
		_expertise = request.form['inputExpertise']
		_startDate = request.form['inputCuratorStartDate']
		_endDate = request.form['inputCuratorEndDate']
	
		try:
            #make connection and call process
			con = mysql.connect()
			cursor = con.cursor()
			cursor.callproc('addcurator',(_name, _expertise, _startDate, _endDate))
			returned_data = cursor.fetchall()

            #return results
			if len(returned_data) == 0:
				con.commit()
				return json.dumps({'message':'Success in adding new curator'})
			else:
				return json.dumps({'error':str(returned_data)})
		except Exception as ex:
			return json.dumps({'error':str(ex)})
	else:
		return json.dumps({'error':'Unauthorized access, please log in'})

@app.route('/addDonor', methods=['POST'])
def addDonor():
    if session.get('user'):
        #get fields from serialized form
        _name = request.form['inputDonorName']
        _address = request.form['inputDonorAddress']
    
        try:
            #make connection and call process
            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('adddonor',(_name, _address))
            returned_data = cursor.fetchall()

            #return results
            if len(returned_data) == 0:
                con.commit()
                return json.dumps({'message':'Success in adding new donor'})
            else:
                return json.dumps({'error':str(returned_data)})
        except Exception as ex:
            return json.dumps({'error':str(ex)})
    else:
        return json.dumps({'error':'Unauthorized access, please log in'})

@app.route('/addPiece', methods=['POST'])
def addPiece():
	if session.get('user'):
        #get fields from serialized form
		_pieceType = request.form['inputPieceType']
		_artist = request.form['inputArtist']
		_dateCreated = request.form['inputDateCreated']
		_desc = request.form['inputDesc']
		_name = request.form['inputPieceName']
		try:
            #make connection and call process
			con = mysql.connect()
			cursor = con.cursor()
			cursor.callproc('addpiece',(_pieceType, _artist, _dateCreated, _desc, _name))
			returned_data = cursor.fetchall()

            #return results
			if len(returned_data) == 0:
				con.commit()
				return json.dumps({'message':'Success in creating new piece'})
			else:
				return json.dumps({'error':str(returned_data)})
		except Exception as ex:
			return json.dumps({'error':str(ex)})
	else:
		return json.dumps({'error':'Unauthorized access, please log in'})

@app.route('/addExhibit', methods=['POST'])
def addExhibit():
	if session.get('user'):
        #get fields from serialized form
		_exhibitStartDate = request.form['inputExhibitStartDate']
		_exhibitEndDate = request.form['inputExhibitEndDate']
		_location = request.form['inputLocation']
		_name = request.form['inputExhibitName']
		try:
            #make connection and call process
			con = mysql.connect()
			cursor = con.cursor()
			cursor.callproc('addexhibit',(_exhibitStartDate, _exhibitEndDate, _location, _name))
			returned_data = cursor.fetchall()

            #return results
			if len(returned_data) == 0:
				con.commit()
				return json.dumps({'message':'Success in creating new exhibit'})
			else:
				return json.dumps({'error':str(returned_data)})
		except Exception as ex:
			return json.dumps({'error':str(ex)})
	else:
		return json.dumps({'error':'Unauthorized access'})

@app.route('/signUp', methods=['POST'])
def signUp():
    #get fields from serialized form
	_username = request.form['inputUsername']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	try:
        #check that no fields are blank
		if _username and _email and _password:
            #make connection and call process
			con = mysql.connect()
			cursor = con.cursor()
			_hash_pw = generate_password_hash(_password)
			cursor.callproc('createUser',(_username, _email, _hash_pw))
			returned_data = cursor.fetchall()
            
            #return results
			if len(returned_data) == 0:
				con.commit()
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

	try:
        #get fields from serialized form
		_username = request.form['inputUsername']
		_password = request.form['inputPassword']
        
        #make connection and call process
		con = mysql.connect()
		cursor = con.cursor()
		cursor.callproc('signin', (_username,))
		returned_array = cursor.fetchall()
		data = returned_array[0]

        #check that the data returned is as long as we want
		if len(data) == 3:
			if check_password_hash(str(data[2]), _password):
				session['user'] = data[0]
				return json.dumps({'good':'logged in!'})
			else:
				return json.dumps({'error':'Wrong password or user name'})
		else:
			return json.dumps({'error':'Wrong password or user name'})
	except Exception as ex:
		return json.dumps({'error':str(ex)})

if __name__ == "__main__":
	app.debug = True
	threaded=True, 
	app.run(port=5000)



