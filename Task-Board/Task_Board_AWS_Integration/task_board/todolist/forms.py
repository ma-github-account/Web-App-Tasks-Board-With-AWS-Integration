from django import forms


class TodoListForm(forms.Form):
    name = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' :'Enter task name', 'aria-label' :'Todo', 'aria-describeby' : 'add-btn'}))
    description = forms.CharField(max_length=300,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' :'Enter task description', 'aria-label' :'Todo', 'aria-describeby' : 'add-btn'}))

