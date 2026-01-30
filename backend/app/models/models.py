from app.extensions import db
from datetime import datetime
import uuid

class SupportTicket(db.Model):
    __tablename__ = 'support_tickets'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    std_name = db.Column(db.String(100), nullable=False)
    std_email = db.Column(db.String(100), nullable=False)
    reg_number = db.Column(db.String(50), nullable=False)
    issue_type = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='open', nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<SupportTicket {self.std_name} - {self.issue_type}>"
