from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
from form import UploadFileForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/",methods=['GET','POST'])
def hello_world():
    form = UploadFileForm()
    fresh_produce_data = None
    electronics_data = None
    games_and_toys = None

    if request.method == 'POST' and form.validate_on_submit():
        flash('successfull','success')
        uploaded_file = request.files['uploadFileField']
        if uploaded_file:
            file_path = 'uploads/' + uploaded_file.filename
            uploaded_file.save(file_path)
            df = pd.read_csv(file_path)

            fresh_produce_data = df[df['Type of Product'] == 'Fresh Produce']
            electronics_data = df[df['Type of Product'] == 'Electronics']
            games_and_toys = df[df['Type of Product'] == 'Games and Toys']

            return render_template('index.html', 
                    fresh_produce_data=fresh_produce_data.to_dict('records'),
                    electronics_data=electronics_data.to_dict('records'),
                    games_and_toys=games_and_toys.to_dict('records'),
                    form=form
                )
        
    return render_template('index.html', 
                fresh_produce_data=None,
                electronics_data=None,
                games_and_toys=None,
                form=form
            )

if __name__ == '__main__':
    app.run(debug=True)