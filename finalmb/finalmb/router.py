from students.api.viewsets import StudentViewSet, StudentMarkPresenceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('markandpresence', StudentMarkPresenceViewSet)