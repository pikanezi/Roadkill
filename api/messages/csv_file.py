__author__ = 'Vincent'
from protorpc import messages


class CsvFile(messages.Message):
    file = messages.BytesField(1, required=True)
    name = messages.StringField(2, required=False)