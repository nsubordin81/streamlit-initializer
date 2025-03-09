import streamlit as st 


def main():
    st.header("welcome to the streamlit cli!")



    st.multiselect(
        label="select a component",
        options=[1, 2, 3],
    )    

    st.button("build project", on_click=build_project)


def build_project():
    st.write("I glot clicked")



if __name__ == "__main__":
    main()