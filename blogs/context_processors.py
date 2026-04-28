from .models import Category
from social.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_link(request):
    social = SocialLink.objects.all()
    return dict(social=social)