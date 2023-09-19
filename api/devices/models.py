from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Device(Model):
    class Meta:
        table_name = 'task_devices' 

    id = UnicodeAttribute(hash_key=True)
    deviceModel = UnicodeAttribute()
    name = UnicodeAttribute()
    note = UnicodeAttribute()
    serial = UnicodeAttribute()
