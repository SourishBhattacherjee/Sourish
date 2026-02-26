import streamlit as st

st.set_page_config(page_title="Sourish Bhattacherjee", layout="wide")

st.title("👋 Welcome to My Portfolio")

st.markdown("""
## 🎓 About Me
Aspiring M.Tech Software Engineer at VIT Vellore with expertise in:
- Full-Stack Development (MERN Stack)
- Machine Learning & Deep Learning
- Systems Programming (C/C++, Linux Kernel)
- Cloud & DevOps

---
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📚 Experience")
    st.write("**Frontend Developer Intern** - Valsco Technologies (July - Oct 2025)")
    st.write("**SDE Intern** - Acceleron Solutions (May - July 2025)")

with col2:
    st.subheader("🎯 Projects")
    st.write("- Music Genre Classification (91.3% accuracy)")
    st.write("- QR Visitor Management System")
    st.write("- LaTeX Resume Builder")

st.markdown("---")
st.write("🔗 [GitHub](https://github.com/SourishBhattacherjee) | 💼 VIT Vellore")
