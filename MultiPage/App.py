import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🛐")
page_2 = st.Page("page_2.py", title="Page 2", icon="😁")
page_3 = st.Page("page_3.py", title="Page 3", icon="🗿")

# Set up navigation (Basic)
# pg = st.navigation([main_page, page_2, page_3])

# Set up navigation (Section)
pg = st.navigation({
    "Section 1": [main_page],
    "Section 2": [page_2],
})

# Run the selected page
pg.run()