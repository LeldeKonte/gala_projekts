import streamlit as st

from planner import create_plan
from executor import process_plan_item
from report import generate_report

st.title("TMDB AI Dashboard")

if st.button("Run Analysis"):

    plan = create_plan()

    results = []

    for i, item in enumerate(plan):

        result = process_plan_item(item, i)

        results.append(result)

        st.subheader(result["title"])

        st.image(result["image"])

        # TABULA
        st.dataframe(result["data"])

        # SQL
        st.code(result["sql"])

    generate_report(results)

    st.success("Report generated!")