import streamlit as st
from io import StringIO
import csv

from pathlib import Path
import json


from csv_profiler.io import *
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown


st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Week 01 • Day 04 — Streamlit GUI")

st.sidebar.header("Inputs")


rows = []
report = None


if "report" not in st.session_state:
    st.session_state["report"] = None
    
if "rows" not in st.session_state:
    st.session_state["rows"] = []


uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    raw_bytes = uploaded_file.getvalue()
    text = raw_bytes.decode("utf-8-sig")
    
    file_like = StringIO(text)
    
    rows = list(csv.DictReader(file_like))
    
    if not rows:
        st.error("The uploaded CSV file has no rows.")
        st.stop()
        
    if not rows[0]:
        st.warning("No columns detected. Make sure the CSV has headers.")
    
    st.session_state["rows"] = rows

    
    st.write(f"Uploaded: {uploaded_file.name}")
    st.write(rows[:5]) 

report_name = st.text_input(
    "Report name",
    value="report"
)


if st.session_state["rows"]:

    if st.button("Generate Report"):
    
        if st.session_state["report"] is None:
        
            report = profile_rows(st.session_state["rows"])

            st.session_state["report"] = report

if st.session_state["report"] is not None:
    report = st.session_state["report"]
    st.write("### Summary")
    cols = st.columns(2)
    cols[0].metric("Rows", report["n_rows"])
    cols[1].metric("Columns", report["n_cols"])
    
    st.subheader("Columns Analysis")
    st.dataframe(report["columns"]) 
    
    md_text = render_markdown(report)
    
    with st.expander("Preview Markdown Report", expanded=False):
        st.markdown(md_text)
        
    st.download_button(
        label="Download JSON",
        data=json.dumps(report, indent=2, ensure_ascii=False),
        file_name=f"{report_name}.json",
        mime="application/json"
    )
    
    st.download_button(
        label="Download Markdown",
        data=md_text,
        file_name=f"{report_name}.md",
        mime="text/markdown"
    )
    
    if st.button("Save to outputs/"):
        out_dir = Path("outputs")
        out_dir.mkdir(exist_ok=True)
    
        json_path = out_dir / f"{report_name}.json"
        md_path = out_dir / f"{report_name}.md"
    
        json_path.write_text(
            json.dumps(report, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    
        md_path.write_text(md_text, encoding="utf-8")
    
        st.success("Saved to outputs/")