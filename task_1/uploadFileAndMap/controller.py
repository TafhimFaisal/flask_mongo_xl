from flask import render_template, request, flash,redirect,url_for
import pandas as pd
from uploadFileAndMap.form import UploadFileForm,MapUploadFileForm
from uploadFileAndMap import app,db
from bson import ObjectId
from pathlib import Path

def get_all_error_messages(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            error_messages.append(f"{form[field].label.text}: {error}")
    return ', '.join(error_messages)

def get_data(type = None):
    data = None
    if 'product_collection' not in db.list_collection_names():
        db.create_collection('product_collection')
    else:
        collection = db['product_collection']
        result = collection.find({'map':type})
        data = result

    return data

@app.route("/upload_mapped_data",methods=['POST'])
def upload_mapped_data():
    collection = db['product_collection']
    mapform = MapUploadFileForm()
    if mapform.validate_on_submit(): 
        data = [ field.data for field in mapform.map if field.data['map'] != "None"]
        collection.insert_many(data)
        flash('stored successfully.', 'success')
    elif request.method == 'POST':
        error_messages = get_all_error_messages(mapform)
        flash('Form submission failed. Please correct the errors: {}'.format(error_messages), 'danger')

    return redirect(url_for('home'))

@app.route("/list/<type>",methods=['GET'])
def data_list(type):
    data = get_data(type)
    return render_template('mapped_data.html',data=data)

@app.route("/",methods=['GET','POST'], endpoint='home')
def upload_file_and_show():
    form = UploadFileForm()
    mapform = MapUploadFileForm()
    data = None

    if request.method == 'POST' and form.validate_on_submit():
        uploaded_file = request.files['uploadFileField']

        if uploaded_file:
            df = pd.read_excel(uploaded_file)
            records = df.to_dict('records')
            expected_header = ['Product Name', 'Description', 'Type of Product'] 
            missing_columns = [col for col in expected_header if col not in df.columns]

            if missing_columns:
                flash(f"Expected columns are missing: {missing_columns}",'danger')
                data = None
            else:
                flash('successfull','success')
                data = records

    return render_template('index.html', 
                data=data,
                form=form,
                mapform=mapform
            )
