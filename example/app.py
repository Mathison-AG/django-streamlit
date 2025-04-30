import streamlit as st

import os
import sys
from pathlib import Path

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
current_path = Path(__file__).parent.parent.resolve()
sys.path.append(str(current_path))
django.setup()

pages = {
    "Examples": [
        st.Page("pages/views.py", title="Views"),
        st.Page("pages/forms.py", title="Forms"),
    ],
}
pg = st.navigation(pages)
pg.run()
