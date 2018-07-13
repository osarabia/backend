from django.core.management.base import BaseCommand
from django.conf import settings
from spa_gastos.uploads.models import Documents
from spa_gastos.gastos.serializers import GastosSerializer

class Command(BaseCommand):
    help = "Process Csv Files One by One"

    def get_unprocess_files(self):
        return Documents.objects.filter(process=False)

    def set_document(self, document):
        self._doc = document

    def process_file(self):
        filepath = "{}/{}".format(settings.MEDIA_ROOT, self._doc.document)
        with open(filepath, 'r') as f:
            line = f.readline()
            while line:
                line = f.readline().replace("\r", "").replace("\n", "")
                self._create_record(line)

        self._doc.process = True
        self._doc.save()

    def _create_record(self, line):
        values = line.split(",")
        if len(values) == 3:
            data = {"fecha":values[0], "concepto": values[1], "cantidad": values[2]}
            try:
                seria = GastosSerializer(data=data)
                if seria.is_valid():
                    seria.save(user_id=self._doc.upload_by)
            except Exception as e:
                print(e)

    def handle(self, *args, **kwargs):
        for doc in self.get_unprocess_files():
            self.set_document(doc)
            self.process_file()
