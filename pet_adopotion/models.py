from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
URL_IMAGE= 'https://www.petinsurancereview.com/sites/default/files/styles/large/public/default_images/default_pet.jpg.webp?itok=A0ba7FUA'                     

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(),
                     nullable=False)
    species = db.Column(db.String(),
                     nullable=False)
    photo_url = db.Column(db.String(),
                     nullable=False, 
                    
    age = db.Column(db.Integer,
                     nullable=True),
    notes = db.Column(db.String(),
                     nullable=True),
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    )                     
    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or URL_IMAGE