"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app
from app import db
from app.models import PropertyInfo
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import newPropertyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/property', methods=['POST', 'GET'])
def property():
    #create a new property

    #Instantiate form class
    newProp = newPropertyForm()

    #Validate form in submit
    if request.method == 'POST' and newProp.validate_on_submit():
        #Get photo file name | Save photo to propertyPhotos folder
        propPhoto = newProp.photo.data 
        filename = secure_filename(propPhoto.filename)

        propPhoto.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        #Get form data and save it to database
        prop = PropertyInfo(title=request.form['title'], numberOfBedrooms=request.form['numberOfBedrooms'], numberOfBathrooms=request.form['numberOfBathrooms'], 
                    location=request.form['location'], price=(int((request.form['price']).replace(',',''))), ptype=request.form['pType'], description=request.form['description'], 
                    photoFilename=filename)

        db.session.add(prop)
        db.session.commit()
        flash('New property successfully added')

        #Get all the properties and pass them to the Properties page
        # propertiesInfo = get_properties_info()

        return redirect(url_for('properties'))

    return render_template('newProperty.html', newPropertyForm=newProp)

@app.route('/propPhotos/<filename>')
def getPropPhoto(filename):
    rootDir = os.getcwd()
    print("here " + filename)
    return send_from_directory(os.path.join(rootDir, app.config['UPLOAD_FOLDER']), filename)
    

@app.route('/properties')
def properties():
    #show all properties

    #Get all the properties and pass them to the Properties page
    # propertiesInfo = get_properties_info()
    propertiesInfo = db.session.query(PropertyInfo).all()

    return render_template('properties.html', propertiesInfo=propertiesInfo)

@app.route('/property/<propertyid>')
def indivProperty(propertyid):
    #show property matching ID provided
    return render_template('indivProperty.html', propertyid=propertyid)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
