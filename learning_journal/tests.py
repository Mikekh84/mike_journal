import pytest
from pyramid import testing


def test_detail_view_has_tittle():
    """Test detail view has title thingy."""
    from .views import detail_view
    request = testing.DummyRequest()
    info = detail_view(request)
    assert "Journal Entry One" in info


@pytest.fixture()
def testapp():
    from learning_journal import main
    return main
    app = main()
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'soemthig' in response.body