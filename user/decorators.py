from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

# def group_required(group_name):
#     def decorator(view_func):
#         def wrapper(request, *args, **kwargs):
#             if request.user.groups.filter(name=group_name).exists():
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponseForbidden()
#         return wrapper
#     return decorator


def group_required(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.groups.filter(name__in=groups).exists():
                    return view_func(request, *args, **kwargs)
                else:
                    if request.user.groups.filter(name='super').exists():
                        return redirect('super')
                    elif request.user.groups.filter(name='vendor').exists():
                        return redirect('dash')
                    elif request.user.groups.filter(name='customers').exists():
                        return redirect('home')
                    else:
                        return redirect('home')
            else:
                return redirect('login')
        return wrapper
    return decorator