import peewee

database = peewee.SqliteDatabase("nli_images.db")

####################################################
class BaseModel(peewee.Model):
    """
    Base ORM model
"""
    class Meta:
        database = database


####################################################

class Portrait(BaseModel):
    """
    ORM model for the portrait images of nli
"""
    file_name = peewee.CharField(null=False, index=True)
    entity_id = peewee.CharField(null=False, index=True)
    image_path = peewee.CharField(null=False)
    portraite_bounding_box = peewee.BlobField()
