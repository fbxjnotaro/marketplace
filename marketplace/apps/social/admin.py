from django.contrib import admin

from marketplace.apps.social.models import (Review,
                                       SocialProfile)


# Make the reviews and social profiles visible through Django Admin
admin.site.register(Review)
admin.site.register(SocialProfile)
