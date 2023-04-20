# These routes are an example of how to use data, forms and routes to create
# a forum where a posts and comments on those posts can be
# Created, Read, Updated or Deleted (CRUD)

from app import app
from app.utils.secrets import getSecrets
import requests
from flask import render_template, flash, redirect, url_for
import requests
from flask_login import current_user
from app.classes.data import Clinic
from app.classes.forms import ClinicForm
from flask_login import login_required
import datetime as dt


@app.route('/clinic/map')
@login_required
def clinicMap():

    clinics = Clinic.objects()

    return render_template('cliniclocator.html',clinics=clinics)

@app.route('/clinic/list')
@login_required
def clinicList():

    clinics = Clinic.objects()

    return render_template('clinics.html',clinics=clinics)


@app.route('/clinic/<clinicID>')
@login_required
def clinic(clinicID):

    thisClinic = Clinic.objects.get(id=clinicID)

    return render_template('clinic.html',clinic=thisClinic)


@app.route('/clinic/delete/<clinicID>')
@login_required
def clinicDelete(clinicID):
    deleteClinic = Clinic.objects.get(id=clinicID)

    deleteClinic.delete()
    flash('The Clinic was deleted.')
    return redirect(url_for('clinicList'))

def updateLatLon(clinic):
    # get your email address for the secrets file
    secrets=getSecrets()
    # call the maps API with the address
    url = f"https://nominatim.openstreetmap.org/search?street={clinic.streetAddress}&city={clinic.city}&state={clinic.state}&postalcode={clinic.zipcode}&format=json&addressdetails=1&email={secrets['MY_EMAIL_ADDRESS']}"
    # get the response from the API
    r = requests.get(url)
    # Find the lat/lon in the response
    try:
        r = r.json()
    except:
        flash("unable to retrieve lat/lon")
        return(clinic)
    else:
        if len(r) != 0:
            # update the database
            clinic.update(
                lat = float(r[0]['lat']),
                lon = float(r[0]['lon'])
            )
            flash(f"clinic lat/lon updated")
            return(clinic)
        else:
            flash('unable to retrieve lat/lon')
            return(clinic)

@app.route('/clinic/new', methods=['GET', 'POST'])
@login_required
def clinicNew():
    form = ClinicForm()

    if form.validate_on_submit():

        newClinic = Clinic(
            name = form.name.data,
            streetAddress = form.streetAddress.data,
            city = form.city.data,
            state = form.state.data,
            zipcode = form.zipcode.data,
            description = form.description.data,
            author = current_user.id,
            modifydate = dt.datetime.utcnow,
        )
        newClinic.save()

        newClinic = updateLatLon(newClinic)

        import requests

        return redirect(url_for('clinic',clinicID=newClinic.id))

    return render_template('clinicform.html',form=form)

@app.route('/clinic/edit/<clinicID>', methods=['GET', 'POST'])
@login_required
def clinicEdit(clinicID):
    editClinic = Clinic.objects.get(id=clinicID)

    if current_user != editClinic.author:
        flash("You can't edit a post you don't own.")
        return redirect(url_for('clinic',clinicID=clinicID))

    form = ClinicForm()
    if form.validate_on_submit():
        editClinic.update(
            name = form.name.data,
            streetAddress = form.streetAddress.data,
            city = form.city.data,
            state = form.state.data,
            zipcode = form.zipcode.data,            
            description = form.description.data,
            modifydate = dt.datetime.utcnow,
        )
        editClinic = updateLatLon(editClinic)
        return redirect(url_for('clinic',clinicID=clinicID))

    form.name.data = editClinic.name
    form.streetAddress.data = editClinic.streetAddress
    form.city.data = editClinic.city
    form.state.data = editClinic.state
    form.zipcode.data = editClinic.zipcode
    form.description.data = editClinic.description

    return render_template('clinicform.html',form=form)
