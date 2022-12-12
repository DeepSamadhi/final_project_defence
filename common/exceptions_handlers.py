from django.shortcuts import render


def handler_server_error(request):
    return render(request, 'server-error.html')

