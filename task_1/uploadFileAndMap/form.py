from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField,StringField,SelectField
from wtforms.validators import DataRequired, ValidationError

class UploadFileForm(FlaskForm):
    def validate_uploadFileField(self, field):
        if not field.data:
            raise ValidationError('No file chosen.')

        file_name = field.data.filename
        if not file_name.endswith('.xlsx'):
            raise ValidationError('File must be in xls format.')

    uploadFileField = FileField('Upload', validators=[DataRequired()])
    submit = SubmitField('Upload File')

class MapUploadFileForm(FlaskForm):
    object_id = StringField('object_id', validators=[DataRequired()])
    map = SelectField('Map To',choices=[
        ('Standard Rate Type', 'Standard Rate Type'),
        ('Reverse charge', 'Reverse charge'),
        ('GAT tax', 'GAT tax'),
    ],validators=[DataRequired()])
    submit = SubmitField('Upload')