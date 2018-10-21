import os
from app import create_app
from flask_script import Manager
import coverage
import pytest


app = create_app(env=os.environ.get('APP_SETTING', "Development"))
manager = Manager(app)

@manager.command
def test():
    pytest.main(['-x', '-v', '-s', 'tests'])

if __name__ == "__main__":
    app.run(debug=True)
