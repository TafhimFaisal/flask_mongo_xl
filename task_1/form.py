from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError

class UploadFileForm(FlaskForm):
    def validate_uploadFileField(self, field):
        if not field.data:
            raise ValidationError('No file chosen.')

        file_name = field.data.filename
        if not file_name.endswith('.csv'):
            raise ValidationError('File must be in CSV format.')

    uploadFileField = FileField('Upload', validators=[DataRequired()])
    submit = SubmitField('Upload File')