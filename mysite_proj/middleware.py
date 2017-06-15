from notes_app.models import RequestStat
from django.utils import timezone


class RequestStatMiddleware(object):

    def process_request(self, request):
        time_request = timezone.now()
        line_request = str(request.method) + " " \
            + str(request.get_full_path()) + " " \
            + str(request.META['SERVER_PROTOCOL'])

        request_stat = RequestStat(
            line=line_request,
            time=time_request,
            is_new=True,
        )
        request_stat.save()
        return None
