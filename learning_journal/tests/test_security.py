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
