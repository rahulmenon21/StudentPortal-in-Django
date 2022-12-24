from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.home,name='home'),
    path('notes',v.notes,name='notes'),
    path('delete_note/<int:pk>',v.delete_note,name='delete-note'),
    path('notes_detail/<int:pk>',v.NotesDetailView.as_view(),name='notes-detail'),

    path('homework',v.homework,name='homework'),
    # path('update_homework/<int:pk>',v.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',v.delete_homework,name='delete-homework'),

    path('youtube',v.youtube,name='youtube'),

    path('todo',v.todo,name='todo'),
    # path('update_todo/<int:pk>',v.update_todo,name='update-todo'),
    path('delete_todo/<int:pk>',v.delete_todo,name='delete-todo'),
]