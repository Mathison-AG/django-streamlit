import streamlit as st


pages = {
    "Examples": [
        st.Page("pages/views.py", title="Views"),
        st.Page("pages/forms.py", title="Forms"),
    ],
}
pg = st.navigation(pages)
pg.run()
