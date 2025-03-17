import streamlit as st


def set_state_from_dict(defaults: dict):
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def requires_states(defaults: dict):
    """
    Decorator to ensure that the state keys are present in the session state.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            set_state_from_dict(defaults)

            return func(*args, **kwargs)

        return wrapper

    return decorator
