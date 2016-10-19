import pytest
import os
from passlib.apps import custom_app_context as pwd_context


@pytest.fixture()
def testapp():
    """Setup a testapp."""
    from webtest import TestApp
    from learning_journal import main
    app = main({})
    return TestApp(app)


PASSWORD = 'password'
ENCRYPTED = pwd_context.encrypt(PASSWORD)


@pytest.fixture(scope='function')
def auth_env():
    """Setup authenticated user environ."""
    username = 'test'
    os.environ['AUTH_USERNAME'] = username
    os.environ['AUTH_PASSWORD'] = ENCRYPTED
    return username, PASSWORD


@pytest.fixture(scope='function')
def authenticated_app(testapp, auth_env):
    """Setup authenticated app."""
    actual_username, actual_password = auth_env
    auth_data = {
        'username': actual_username,
        'password': actual_password,
    }
    testapp.post('/login/', auth_data, status='3*')
    return testapp


def test_public_view(testapp):
    """Test access to a public view."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_private_view(testapp):
    """Test access to a private view."""
    response = testapp.get('/new-entry/', status='4*')
    assert response.status_code == 403


def test_login_view(testapp):
    """Test access to login view is 200 public."""
    response = testapp.get('/login/')
    assert response.status_code == 200


def test_login_view_has_username(testapp):
    """Test login page has username."""
    response = testapp.get('/login/')
    assert 'username' in response


def test_private_view_after_secured(authenticated_app):
    """Test 200 after logging in."""
    response = authenticated_app.get('/new-entry/')
    assert response.status_code == 200
