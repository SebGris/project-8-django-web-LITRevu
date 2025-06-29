from django import forms
from django.contrib.auth import get_user_model

from . import models
from .models import UserFollows

REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

User = get_user_model()


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'style': (
                        'border:2px solid #333; '
                        'width:100%; '
                        'text-align:center;'
                    )
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'style': 'border:2px solid #333; width:100%;',
                    'rows': 8
                }
            ),
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }
        widgets = {
            'rating': forms.Select(
                choices=[(i, f'{i} étoiles') for i in range(1, 6)]
            ),
            'headline': forms.TextInput(
                attrs={'style': 'border:2px solid #333; width:100%;'}
            ),
            'body': forms.Textarea(
                attrs={
                    'style': 'border:2px solid #333; width:100%;',
                    'rows': 8
                }
            ),
        }


class FollowUsersForm(forms.Form):
    username = forms.ChoiceField(
        label="Nom d'utilisateur",
        choices=[],
        widget=forms.Select(attrs={
            'class': 'form-control',
            'style': 'border:2px solid #333;'
        })
    )

    def __init__(self, *args, **kwargs):
        # Extraire l'utilisateur des kwargs avant d'appeler super()
        current_user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        User = get_user_model()

        # Exclure l'utilisateur courant et ceux déjà suivis
        users_qs = User.objects.all()
        if current_user:
            users_qs = users_qs.exclude(pk=current_user.pk)
            already_followed = UserFollows.objects.filter(
                user=current_user
            ).values_list('followed_user', flat=True)
            users_qs = users_qs.exclude(pk__in=already_followed)
        self.fields['username'].choices = [
            ('', '--- Sélectionnez un utilisateur ---')
        ] + [
            (user.username, user.username) for user in users_qs
        ]
