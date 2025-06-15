import datetime
from django.template import RequestContext, Context


def year(request):
    """Добавляет переменную с текущим годом."""
    return {'year': datetime.datetime.now().year}
