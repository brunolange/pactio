from functools import wraps


def pactio(fn):
    @wraps(fn)
    def view(request, *args, **kwargs):
        return fn(request, *args, **kwargs)

    return view
