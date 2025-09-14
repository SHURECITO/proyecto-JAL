from .session import SessionLocal
from ..models.admin import Admin
from ..services.security import get_password_hash
from sqlalchemy import select

def ensure_seed_admin(email: str, password: str):
    db = SessionLocal()
    try:
        exists = db.execute(select(Admin).where(Admin.email == email)).scalar_one_or_none()
        if not exists:
            admin = Admin(email=email, password_hash=get_password_hash(password))
            db.add(admin)
            db.commit()
    finally:
        db.close()
