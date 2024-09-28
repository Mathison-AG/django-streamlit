from django.conf import settings


def get_setting(name, default=None):
    return getattr(settings, name, default)


STREAMLIT_APP_PATH = get_setting("STREAMLIT_APP_PATH", "app.py")
STREAMLIT_APP_PORT = get_setting("STREAMLIT_APP_PORT", 8501)
