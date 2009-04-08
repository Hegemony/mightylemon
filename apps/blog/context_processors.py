from django.conf import settings

def blog(request):
    
    blog = request.blog
    
    return {
        'blog': blog,
        'RSS_URL': blog.settings.rss_url,
        'RSS_TITLE': blog.settings.rss_title
    }

def stats(request):
    if not settings.DEBUG:
        return {
            'STATS_CODE': settings.STATS_CODE,
            }
    return {
        'STATS_CODE': "<!-- debug mode enabled / no stats tracking -->",
        }

