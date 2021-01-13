import nox, os

PYTHON_VERSION = os.environ.get('PYTHON_VERSION')

@nox.session(python=PYTHON_VERSION)
def tests(session):
    session.install("-r", "requirements.txt")
    session.install("pytest")
    session.run('python', '-m', 'pytest')
    