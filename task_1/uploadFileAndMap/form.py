from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField,StringField,SelectField,FieldList,FormField
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

class MapForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    product_type = StringField('Product Type', validators=[DataRequired()])
    map = SelectField('',choices=[
        (None,'<------ select ------>'),
        ('standard_rate', 'Standard Rate'),
        ('reverse_charge', 'Reverse charge'),
        ('gat_tax', 'GAT tax'),
    ],default=None,validators=[])

class MapUploadFileForm(FlaskForm):
    map = FieldList(FormField(MapForm),min_entries= 1)
    submit = SubmitField('Store Mapped Data')