from .models import SocialLink


def social_links(request):
    print('Social Links')
    return {
        'social_links': SocialLink.objects.all()
    }