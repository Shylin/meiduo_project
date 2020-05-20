from django.middleware.csrf import CsrfViewMiddleware


class MyCsrfViewMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):

        pass