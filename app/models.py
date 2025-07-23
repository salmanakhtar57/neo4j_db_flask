from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom

class Token(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

class Project(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    files = RelationshipTo('File', 'HAS_FILE') 

class File(StructuredNode):
    filename = StringProperty(required=True)
    width = IntegerProperty(required=True)
    uploaded_by = RelationshipFrom('User', 'UPLOADED')

class User(StructuredNode):
    google_id = StringProperty(unique_index=True, required=True)
    uploads = RelationshipTo('File', 'UPLOADED')
