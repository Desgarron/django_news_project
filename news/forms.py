from django import forms
from news.models import Category, News


# First option
# class NewsForm(forms.Form):
#     title = forms.CharField(
#         max_length=150,
#         label="Title",
#         widget=forms.TextInput(
#             attrs={"class": "form-control"}
#         )
#     )
#     content = forms.CharField(
#         label="Content news",
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "rows": 5,
#             }
#         )
#     )
#     is_published = forms.BooleanField(label="Is publish", initial=True)
#     category = forms.ModelChoiceField(
#         empty_label="Select category",
#         queryset=Category.objects.all(),
#         label="Category",
#         widget=forms.Select(
#             attrs={"class": "form-control"}
#         )
#     )

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = "__all__"
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }