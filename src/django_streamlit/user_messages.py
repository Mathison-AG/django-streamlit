import streamlit as st


def get_user_messages():
    if "user_messages" not in st.session_state:
        st.session_state["user_messages"] = {
            "info": [],
            "warning": [],
            "error": [],
        }
    return st.session_state["user_messages"]


def add_info_message(message):
    get_user_messages()["info"].append(message)


def add_warning_message(message):
    get_user_messages()["warning"].append(message)


def add_error_message(message):
    get_user_messages()["error"].append(message)


def show_user_messages():
    user_messages = get_user_messages()

    for message in user_messages["info"]:
        st.info(message)

    for message in user_messages["warning"]:
        st.warning(message)

    for message in user_messages["error"]:
        st.error(message)

    user_messages["info"] = []
    user_messages["warning"] = []
    user_messages["error"] = []
