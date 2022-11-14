from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

def auth():

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
