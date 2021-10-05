# apps/core/routers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter


# Local imports
from apps.testings.routers import testings


# Create your routers here.
routers_tuples = (
    testings,
)
routers_lists = sum([list(router_tuple) for router_tuple in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    prefix, viewset, *rest = router_list
    base_name = rest[0] if len(rest) == 1 else prefix

    router.register(prefix, viewset, base_name)
