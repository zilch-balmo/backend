"""
Entrypoint module for WSGI containers.

"""
from backend.app import create_app


app = create_app().app
