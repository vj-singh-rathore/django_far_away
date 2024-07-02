from django.urls import path
from .views import ItemCreateview, ItemListview, ItemRetrieveview, ItemDestroyview, ItemUpdateview ,TruncateDataview ,UserSignUpView,UserSignInView , signout
urlpatterns = [
    path('mainwork/create/', ItemCreateview.as_view()),
    path('mainwork/retrieve/<int:pk>/', ItemRetrieveview.as_view()),
    path('mainwork/listView/', ItemListview.as_view()),
    path('mainwork/update/<int:pk>/', ItemUpdateview.as_view()),
    path('mainwork/delete/<int:pk>/', ItemDestroyview.as_view()),
    path('mainwork/TruncateData/', TruncateDataview.as_view()),
    path('mainwork/UserSignUpView/', UserSignUpView.as_view()),
    path('mainwork/UserSignInView/', UserSignInView.as_view()),
    path ('signout', signout)
]
