# In decorators.py
from functools import wraps
from django.shortcuts import redirect

def user_not_authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect authenticated users to a different page (e.g., home page).
            return redirect('home')  # Replace 'home' with your desired URL name or path.
        return view_func(request, *args, **kwargs)
    return _wrapped_view
