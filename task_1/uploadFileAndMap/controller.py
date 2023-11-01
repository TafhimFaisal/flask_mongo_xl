from flask import render_template, request, flash,redirect,url_for
import pandas as pd
from uploadFileAndMap.form import UploadFileForm,MapUploadFileForm
from uploadFileAndMap import app,db
from bson import ObjectId

@app.route("/update/mapping",methods=['POST'])
def update_mapping():
    collection = db['product_collection']
    form_data = request.form.to_dict()
    collection.update_one({"_id": ObjectId(form_data['object_id'])}, {"$set": {'map':form_data['map']}})
    flash('Record updated successfully.', 'success')
    return redirect(url_for('home'))
    
@app.route("/",methods=['GET','POST'], endpoint='home')
def upload_file_and_map():
    form = UploadFileForm()
    mapform = MapUploadFileForm()
    data = None

    if request.method == 'POST' and form.validate_on_submit():
        flash('successfull','success')
        uploaded_file = request.files['uploadFileField']

        if uploaded_file:
            file_path = 'uploads/' + uploaded_file.filename
            uploaded_file.save(file_path)
            df = pd.read_excel(file_path)

            collection = db['product_collection']
            records = df.to_dict('records')
            collection.insert_many(records)

    if 'product_collection' not in db.list_collection_names():
        db.create_collection('product_collection')
    else:
        collection = db['product_collection']
        data = collection.find()

    return render_template('index.html', 
                data=data,
                form=form,
                mapform=mapform
            )
