import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Everyone, Authenticated, Allow
from passlib.apps import custom_app_context as pwd_context


def includeme(config):
    """Security config for app."""
    auth_password = os.environ.get('AUTH_PASSWORD', 'seekrit')
    auth_policy = AuthTktAuthenticationPolicy(
        secret=auth_password,
        hashalg='sha512'
    )
    config.set_authentication_policy(auth_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_default_permission('view')
    config.set_root_factory(MyRoot)


class MyRoot(object):
    """Security Root ACL."""

    def __init__(self, request):
        """Initialize myroot with request."""
        self.request = request

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'secured'),
    ]


def check_cred(username, password):
    """Check credentials of user."""
    stored_username = os.environ.get('AUTH_USERNAME', '')
    stored_password = os.environ.get('AUTH_PASSWORD', '')
    is_authenticated = False
    if username == stored_username:
        try:
            return pwd_context.verify(password, stored_password)
        except ValueError:
            pass
    return is_authenticated
