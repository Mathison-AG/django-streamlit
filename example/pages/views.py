import streamlit as st

from apps.demo.models import Country

st.set_page_config(page_title="Views", layout="wide")
st.title("Views")


st.dataframe(
    Country.objects.all().to_dataframe(),
    column_config=Country().column_config,
    height=1000,
    use_container_width=True,
)
