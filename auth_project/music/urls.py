from lib2to3.pgen2 import token
from django.urls import path
from .views import MusicListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('music-list', MusicListView.as_view(), name="music_list"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk0MTgxMiwiaWF0IjoxNjUzODU1NDEyLCJqdGkiOiI2NzFkYjliZjIwZTY0MWY2YjZkNGZmMmE2NmExMWVmNSIsInVzZXJfaWQiOjF9.iV9mSlIp9wneKlgQyY1LskYoeYErCIR2BDpeGirtO7Q",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzODU1NzEyLCJpYXQiOjE2NTM4NTU0MTIsImp0aSI6Ijg1ZDE2ZTI5MzJiZDRiZTNhMjZmN2QzYWQ3MWI3ODQyIiwidXNlcl9pZCI6MX0.kBXadz4IcexBsf5-7uYTlYs0OUNfPg7VW5SW_D8_mSM"
# }


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk0MjU0MiwiaWF0IjoxNjUzODU2MTQyLCJqdGkiOiJmYTRmZWYzZDlhMjI0MmFkOTEzNTk2NTY2ODJkMTg2NyIsInVzZXJfaWQiOjF9.8dL6Pmpv6yuW3s93KVW9QGUhcCw_tksyM82q5daEDUk",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzODU2NDQyLCJpYXQiOjE2NTM4NTYxNDIsImp0aSI6IjExYjE2YjI5OTE2ZDRhZDM5MWQ0NjA2MmIyMjE5N2I0IiwidXNlcl9pZCI6MX0.CBO48ZezUj2AG2p9oTELA56wr_rhGlEYqPUCPRAuIMs"
# }


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk0NDQ1NiwiaWF0IjoxNjUzODU4MDU2LCJqdGkiOiJiMWVlODJmODVhMDE0Yzc5OTFhMTNjZThkMzhhNWFlMyIsInVzZXJfaWQiOjF9.YpQuta1uIFzYbIp-VORGJrkNXi_HP5h_hbpUoRsfBuM",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzODU4MzU2LCJpYXQiOjE2NTM4NTgwNTYsImp0aSI6IjNjMTY3YWM4ZDAyMTQ4NzQ5MTYyZWYzZWYxNzQxNDhkIiwidXNlcl9pZCI6MX0.23Db6A7dQGQyJHWLadoOzxFdphBZOO3uKpFxXJG73lM"
# }