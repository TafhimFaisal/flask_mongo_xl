from flask import Flask, render_template, url_for, flash, redirect
from form import UploadFileForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/",methods=['GET','POST'])
def hello_world():
    form = UploadFileForm()
    if form.validate_on_submit():
        flash('success full','success')

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)