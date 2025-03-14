import streamlit as st 


def main():
    st.header("welcome to the streamlit cli!")

    components = ["api_connector", "document_parser"]

    st.multiselect(
        label="select a component",
        options=components,
        key="multi_select",
    )    

    st.button("build project", on_click=build_project)


def build_project():
    st.write(f" type of multi_select element: {st.session_state.multi_select} ")
    for component in st.session_state.multi_select:
        st.write (f" adding {component} to the project")



if __name__ == "__main__":
    main()