# app.py
# -*- coding: utf-8 -*-
import io
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Student Grades Dashboard", layout="wide")

# ------------------------------
# الترجمات
# ------------------------------
translations = {
    "en": {
        "title": "📊 Student Grades Analysis Dashboard",
        "instructions": """
        - Upload grades file (CSV/XLSX) or use sample data.
        - Required columns: **Student**, **Term1**, **Term2**, **Term3**.
        - You can edit the table and export to CSV/Excel.
        - Categories:
            - Excellent: ≥ 18
            - Very Good: 16–<18
            - Good: 10–<16
            - Average: < 10
        """,
        "import_export": "📂 Import / Export",
        "upload": "Upload CSV or Excel",
        "sample": "Generate Sample",
        "sample_rows": "Sample rows",
        "download_template": "💡 Download template file:",
        "download_csv": "Download CSV Template",
        "download_excel": "Download Excel Template",
        "missing_cols": "Missing columns: {missing}. Please use the template.",
        "data_section": "📊 Data",
        "edit_caption": "You can edit grades then click **Refresh** below.",
        "refresh": "🔄 Refresh Analytics",
        "students_count": "Number of Students",
        "avg_term": "Average (Term {i})",
        "tab_term": "📚 Term {i}",
        "tab_avg": "📈 Average (All Terms)",
        "bar_title": "Grade Distribution – {term}",
        "pie_title": "Category Percentages – {term}",
        "export_data": "💾 Export Data",
        "download_results_csv": "⬇️ Download CSV",
        "download_results_excel": "⬇️ Download Excel",
        "student": "Student",
        "term": "Term{i}",
    },
    "ar": {
        "title": "📊 لوحة تحليل درجات الطلاب",
        "instructions": """
        - ارفع ملف الدرجات (CSV/XLSX) أو استخدم العينة الجاهزة.
        - الأعمدة المطلوبة: **Student**, **Term1**, **Term2**, **Term3**.
        - يمكنك تعديل الجدول وتصديره إلى CSV/Excel.
        - التصنيفات:
            - ممتاز: ≥ 18
            - جيد جدًا: 16–<18
            - جيد: 10–<16
            - متوسط: < 10
        """,
        "import_export": "📂 استيراد / تصدير",
        "upload": "رفع ملف CSV أو Excel",
        "sample": "إنشاء عينة",
        "sample_rows": "عدد صفوف العينة",
        "download_template": "💡 تنزيل قالب فارغ:",
        "download_csv": "تنزيل قالب CSV",
        "download_excel": "تنزيل قالب Excel",
        "missing_cols": "الأعمدة المفقودة: {missing}. يرجى استخدام القالب.",
        "data_section": "📊 البيانات",
        "edit_caption": "يمكنك تعديل الدرجات ثم الضغط على زر **تحديث** بالأسفل.",
        "refresh": "🔄 تحديث التحليلات",
        "students_count": "عدد الطلاب",
        "avg_term": "المتوسط (الفصل {i})",
        "tab_term": "📚 الفصل {i}",
        "tab_avg": "📈 المتوسط (جميع الفصول)",
        "bar_title": "توزيع الدرجات – {term}",
        "pie_title": "النسب المئوية حسب الفئات – {term}",
        "export_data": "💾 تصدير البيانات",
        "download_results_csv": "⬇️ تنزيل CSV",
        "download_results_excel": "⬇️ تنزيل Excel",
        "student": "الطالب",
        "term": "الفصل {i}",
    },
    "fr": {
        "title": "📊 Tableau d'analyse des notes des étudiants",
        "instructions": """
        - Importez un fichier de notes (CSV/XLSX) ou utilisez un échantillon.
        - Colonnes requises : **Student**, **Term1**, **Term2**, **Term3**.
        - Vous pouvez modifier le tableau et exporter en CSV/Excel.
        - Catégories :
            - Excellent : ≥ 18
            - Très Bien : 16–<18
            - Bien : 10–<16
            - Moyen : < 10
        """,
        "import_export": "📂 Import / Export",
        "upload": "Importer un fichier CSV ou Excel",
        "sample": "Générer un échantillon",
        "sample_rows": "Nombre de lignes d'échantillon",
        "download_template": "💡 Télécharger un modèle :",
        "download_csv": "Télécharger modèle CSV",
        "download_excel": "Télécharger modèle Excel",
        "missing_cols": "Colonnes manquantes : {missing}. Veuillez utiliser le modèle.",
        "data_section": "📊 Données",
        "edit_caption": "Vous pouvez modifier les notes puis cliquer sur **Actualiser**.",
        "refresh": "🔄 Actualiser l'analyse",
        "students_count": "Nombre d'étudiants",
        "avg_term": "Moyenne (Semestre {i})",
        "tab_term": "📚 Semestre {i}",
        "tab_avg": "📈 Moyenne (tous les semestres)",
        "bar_title": "Distribution des notes – {term}",
        "pie_title": "Répartition des catégories – {term}",
        "export_data": "💾 Exporter les données",
        "download_results_csv": "⬇️ Télécharger CSV",
        "download_results_excel": "⬇️ Télécharger Excel",
        "student": "Étudiant",
        "term": "Semestre {i}",
    },
    "ro": {
        "title": "📊 Panou de analiză a notelor studenților",
        "instructions": """
        - Încărcați fișierul de note (CSV/XLSX) sau folosiți un eșantion.
        - Coloane necesare: **Student**, **Term1**, **Term2**, **Term3**.
        - Puteți edita tabelul și exporta în CSV/Excel.
        - Categorii:
            - Excelent: ≥ 18
            - Foarte Bine: 16–<18
            - Bine: 10–<16
            - Mediu: < 10
        """,
        "import_export": "📂 Import / Export",
        "upload": "Încărcați CSV sau Excel",
        "sample": "Generați eșantion",
        "sample_rows": "Număr de rânduri eșantion",
        "download_template": "💡 Descărcați șablonul:",
        "download_csv": "Descărcați șablon CSV",
        "download_excel": "Descărcați șablon Excel",
        "missing_cols": "Coloane lipsă: {missing}. Utilizați șablonul.",
        "data_section": "📊 Date",
        "edit_caption": "Puteți modifica notele apoi apăsați **Reîmprospătați**.",
        "refresh": "🔄 Reîmprospătare analiză",
        "students_count": "Număr de studenți",
        "avg_term": "Medie (Semestrul {i})",
        "tab_term": "📚 Semestrul {i}",
        "tab_avg": "📈 Medie (toate semestrele)",
        "bar_title": "Distribuția notelor – {term}",
        "pie_title": "Procentaj pe categorii – {term}",
        "export_data": "💾 Exportați datele",
        "download_results_csv": "⬇️ Descărcați CSV",
        "download_results_excel": "⬇️ Descărcați Excel",
        "student": "Student",
        "term": "Semestrul {i}",
    }
}

# ------------------------------
# اختيار اللغة
# ------------------------------
with st.sidebar:
    lang = st.selectbox("🌐 Language / اللغة / Langue / Limba", ["en", "ar", "fr", "ro"], index=0)
T = translations[lang]

# ------------------------------
# دوال مساعدة
# ------------------------------
CAT_ORDER = ["Excellent", "Very Good", "Good", "Average",
             "ممتاز", "جيد جدًا", "جيد", "متوسط",
             "Excellent", "Très Bien", "Bien", "Moyen",
             "Excelent", "Foarte Bine", "Bine", "Mediu"]

def categorize(score: float, lang: str):
    if pd.isna(score):
        return "N/A"
    if score >= 18:
        return {"en":"Excellent","ar":"ممتاز","fr":"Excellent","ro":"Excelent"}[lang]
    if score >= 16:
        return {"en":"Very Good","ar":"جيد جدًا","fr":"Très Bien","ro":"Foarte Bine"}[lang]
    if score >= 10:
        return {"en":"Good","ar":"جيد","fr":"Bien","ro":"Bine"}[lang]
    return {"en":"Average","ar":"متوسط","fr":"Moyen","ro":"Mediu"}[lang]

def make_template(n=10):
    return pd.DataFrame({
        "Student": [f"Student {i+1}" for i in range(n)],
        "Term1": np.random.randint(6, 20, size=n),
        "Term2": np.random.randint(6, 20, size=n),
        "Term3": np.random.randint(6, 20, size=n),
    })

# ------------------------------
# الواجهة
# ------------------------------
st.title(T["title"])
st.markdown(T["instructions"])

with st.sidebar:
    st.header(T["import_export"])
    up = st.file_uploader(T["upload"], type=["csv", "xlsx", "xls"])
    sample_rows = st.number_input(T["sample_rows"], 5, 200, 30, step=5)
    make_sample = st.button(T["sample"])
    st.markdown("---")
    st.caption(T["download_template"])
    tmpl = make_template(10)
    st.download_button(T["download_csv"], tmpl.to_csv(index=False).encode("utf-8-sig"), file_name="template.csv")
    with io.BytesIO() as buf:
        with pd.ExcelWriter(buf, engine="xlsxwriter") as writer:
            tmpl.to_excel(writer, index=False)
        st.download_button(T["download_excel"], buf.getvalue(), file_name="template.xlsx")

# ------------------------------
# تحميل البيانات
# ------------------------------
if up is not None:
    if up.name.endswith(".csv"):
        df = pd.read_csv(up)
    else:
        df = pd.read_excel(up)
else:
    df = make_template(sample_rows if make_sample else 20)

# ------------------------------
# عرض البيانات
# ------------------------------
st.subheader(T["data_section"])
st.caption(T["edit_caption"])
df["Average"] = df[["Term1","Term2","Term3"]].mean(axis=1)
df["Category"] = df["Average"].apply(lambda x: categorize(x, lang))
st.dataframe(df)

# ------------------------------
# الرسوم البيانية
# ------------------------------
tabs = st.tabs([T["tab_term"].format(i=i) for i in range(1,4)] + [T["tab_avg"]])
terms = ["Term1","Term2","Term3"]

for idx,t in enumerate(terms):
    with tabs[idx]:
        st.plotly_chart(px.histogram(df, x=t, nbins=10, title=T["bar_title"].format(term=t)))
        st.plotly_chart(px.pie(df, names=df[t].apply(lambda x: categorize(x, lang)), title=T["pie_title"].format(term=t), hole=0.3))

with tabs[3]:
    st.plotly_chart(px.histogram(df, x="Average", nbins=10, title=T["bar_title"].format(term="Average")))
    st.plotly_chart(px.pie(df, names="Category", title=T["pie_title"].format(term="Average"), hole=0.3))

# ------------------------------
# تنزيل النتائج
# ------------------------------
st.subheader(T["export_data"])
st.download_button(T["download_results_csv"], df.to_csv(index=False).encode("utf-8-sig"), file_name="results.csv")
with io.BytesIO() as buf:
    with pd.ExcelWriter(buf, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)
    st.download_button(T["download_results_excel"], buf.getvalue(), file_name="results.xlsx")
