from rest_framework import serializers
from spa_gastos.uploads.models import Documents
from spa_gastos.uploads.validators import validating_file

class FileSerializer(serializers.ModelSerializer):
  document = serializers.FileField(validators=[validating_file])

  class Meta():
    model = Documents
    fields = ('document',)
