from flask.cli import FlaskGroup

from viessmann_exporter import create_app

cli = FlaskGroup(create_app())

if __name__ == "__main__":
    cli()
