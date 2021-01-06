import click

from . import app
from .model import db


@app.cli.command()
def create_db():
    """Create and nationalize database"""
    db.create_all(app=app)
    click.echo('Create and nationalize database')


@app.cli.command()
def base_data():
    """Insert base data"""
    click.echo('Insert base data')


@app.cli.command()
def mockup():
    """Insert mockup data"""
    click.echo('Insert mockup data')

