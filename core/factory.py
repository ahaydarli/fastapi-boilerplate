from fastapi import FastAPI

from app import views as api_views
from core.config import settings
from core.database import db, db_connection


def register_extensions(app: object):
    """Register third part extensions."""
    db.initialize(db_connection)

    return None


def register_routers(app):
    """Register app routers."""
    app.include_router(api_views.router, prefix='/v1')

    return None


def create_app() -> FastAPI:
    """App factory. """
    app = FastAPI(title=settings.app_title,
                  description=settings.app_description,
                  version=settings.api_version)
    register_extensions(app)
    register_routers(app)

    return app
