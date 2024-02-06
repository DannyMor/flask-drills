from app import app
from database.db import db
from model.detector import Detector
from model.organization import Organization


def seed_db():
    with app.app_context():
        db.create_all()

        # Create Some organizations
        hunters = Organization(id=1, name='Hunters')
        google = Organization(id=2, name='Google')
        databricks = Organization(id=3, name='Databricks')
        amazon = Organization(id=4, name='Amazon')

        # Create some detectors
        suspicious_signin = Detector(name='suspicious_signin', organization_id=1)
        platform_alerts = Detector(name='platform_alerts', organization_id=3)

        # Insert organizations
        db.session.add(hunters)
        db.session.add(google)
        db.session.add(databricks)
        db.session.add(amazon)

        # Insert detectors
        db.session.add(suspicious_signin)
        db.session.add(platform_alerts)

        db.session.commit()


if __name__ == "__main__":
    seed_db()
