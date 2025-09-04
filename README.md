# 📊 Student Grades Analysis Dashboard

An interactive **Streamlit** web application for analyzing student grades (out of 20) across **three academic terms**.  
The dashboard supports **multilingual interface** (English, Arabic, French, Romanian), automatic performance classification, and export/import of data.

---

## ✨ Features

- 📂 **Import student data** from CSV or Excel files  
- 📝 **Edit data interactively** inside the dashboard  
- 📊 **Visualizations**:  
  - Bar charts (grade distribution)  
  - Pie charts (performance category percentages)  
- 🧮 **Automatic classification of grades**:
  - **Excellent**: ≥ 18  
  - **Very Good**: 16–<18  
  - **Good**: 10–<16  
  - **Average**: < 10  
- 🌐 **Language switcher**: English, Arabic, French, Romanian  
- 💾 **Export results** back to CSV or Excel  
- 🎲 **Generate sample data** for quick demo  

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – Web app framework  
- [Pandas](https://pandas.pydata.org/) – Data handling  
- [Plotly Express](https://plotly.com/python/plotly-express/) – Interactive charts  
- [OpenPyXL](https://openpyxl.readthedostreamlit run app.py
cs.io/) & [XlsxWriter](https://xlsxwriter.readthedocs.io/) – Excel support  

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
2️⃣ Install dependencies
streamlit run app.py
3️⃣ Run the app
streamlit run app.py

git clone https://github.com/yourusername/student-grades-dashboard.git
cd student-grades-dashboard
