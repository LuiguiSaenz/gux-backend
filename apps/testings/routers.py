# apps/daily_logs/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import TestingViewSet, StatusViewSet, PrevisionViewSet


# Create your routers here.
testings = (
    (r'testings', TestingViewSet),
    (r'status', StatusViewSet),
    (r'previsions', PrevisionViewSet),
)
