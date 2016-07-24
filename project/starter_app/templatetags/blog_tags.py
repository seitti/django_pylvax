from django import template
from ..models import Post

register = template.Library()

@register.inclusion_tag('starter_app/menu_in_blog.html')
def generate_menu(selected_post=None):
    return {
        'posts': Post.objects.all(),
        'selected_post': selected_post
        }
