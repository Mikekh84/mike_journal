import pytest


@pytest.fixture()
def testapp():
    """Setup a testapp."""
    from webtest import TestApp
    from learning_journal import main
    app = main({})
    return TestApp(app)


def test_public_view(testapp):
    """Test access to a public view."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_private_view(testapp):
    """Test access to a private view."""
    response = testapp.get('/new-entry/', status='4*')
    assert response.status_code == 403
