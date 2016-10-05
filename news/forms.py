from django import forms
# from datetimewidget.widgets import DateTimeWidget

from .models import News


STATUS_CHOICES = (
        ('unpublish', 'Unpublish',),
        ('publish', 'Publish'),
    )

class NewsAddForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    class Meta:
        model = News
        fields = ['title', 'author', 'image_news1', 'image_news2', 'body', 'status', 'publish']
        # dateTimeOptions = {
        #     'format': 'dd/mm/yyyy HH:ii P',
        #     'autoclose': True,
        #     'showMeridian': True
        # }
        # widgets = {
        #     'title': forms.TextInput(attrs={'placeholder': u'News title...'}),
        #     'body': forms.Textarea(attrs={'placeholder': u'Contant of news...'}),
        #     'publish': DateTimeWidget(usel10n = True, bootstrap_version=3, options = dateTimeOptions)
        # }
