import streamlit as st


from django.utils import timezone


class StreamlitListView:
    def __init__(
        self,
        model,
        filter_fields=[],
        column_config=None,
        height=None,
        use_container_width=True,
        **kwargs,
    ):
        self.model = model
        self.height = height
        self.use_container_width = use_container_width
        self.column_config = column_config
        self.kwargs = kwargs
        self.filter_fields = filter_fields

    def get_column_config(self):
        if self.column_config is None:
            return self.model().column_config

        return self.column_config

    def build_filters(self):
        filters = {}
        for field_name in self.filter_fields:
            try:
                field = self.model._meta.get_field(field_name)
                value = st.text_input(
                    label=field.verbose_name,
                    key=f"filter__{field_name}",
                    on_change=lambda: self.rerender(),
                )
                filters[field_name] = value

            except Exception:
                st.error(
                    f"Field '{field_name}' does not exist in {self.model.__name__}"
                )

        return filters

    def rerender(self):
        st.session_state.last_updated = timezone.now().isoformat()

    def get_queryset(self):
        filters = {}
        for field, value in st.session_state.items():
            if field.startswith("filter__"):
                if value:
                    field_name = field.replace("filter__", "")
                    filters = {f"{field_name}__icontains": value}

        return self.model.objects.filter(**filters)

    def to_dataframe(self):
        return self.get_queryset().to_dataframe()

    def render_table(self):
        st.session_state["queryset"] = self.get_queryset()

        st.dataframe(
            st.session_state.queryset.to_dataframe(),
            column_config=self.get_column_config(),
            height=self.height
            or min(
                700,
                ((st.session_state["queryset"].count() + 1) * 35 + 3),
            ),
            use_container_width=self.use_container_width,
            **self.kwargs,
        )

    def render_filters(self):
        self.build_filters()

    def render(self):
        st.title(self.model._meta.verbose_name_plural.capitalize())

        # For debugging purposes
        # st.write(f"Last Updated: {timezone.now().strftime("%d.%m.%Y %H:%M:%S")}")

        num_cols = [1]

        if self.filter_fields:
            num_cols = [10, 2]

        cols = st.columns(num_cols)

        with cols[0]:
            self.render_table()

        if self.filter_fields:
            with cols[1]:
                self.render_filters()
