from django.urls import path

from . import views

urlpatterns = [
    path('', views.opportunities, name='oportal'), # URL for opportunities page (function-based)
    #path('', views.OpportunityListView.as_view(), name='oportal') # URL for opportunities page (class-based)
    path('<int:pk>/', views.OpportunityDetailView.as_view(), name='opportunity'), # URL for every opportunity page

    path('create/', views.OpportunityCreateView.as_view(), name='opportunity-create'), # URL for creating an opportunity
    # path('<int:pk>/update', views.OpportunityUpdateView.as_view(), name='opportunity-update'), # URL for updating an opportunity (class-based)
    path('<int:pk>/update/', views.update_opportunity, name='opportunity-update'), # URL for updating an opportunity (function-based)
    path('<int:pk>/delete/', views.OpportunityDeleteView.as_view(), name='opportunity-delete'), # URL for deleting an opportunity
]