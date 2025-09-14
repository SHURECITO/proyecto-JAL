from .session import Base, engine
from ..models.admin import Admin  # noqa: F401
from sqlalchemy import text
import time
import logging

logger = logging.getLogger(__name__)

def wait_for_db(max_attempts: int = 60, delay_seconds: float = 1.0):
    last_err: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Database is available")
            return
        except Exception as e:  # noqa: BLE001
            last_err = e
            logger.warning("DB not ready (attempt %s/%s): %s", attempt, max_attempts, e)
            time.sleep(delay_seconds)
    raise RuntimeError(f"Database not ready after {max_attempts} attempts: {last_err}")

def init_db():
    wait_for_db()
    Base.metadata.create_all(bind=engine)
