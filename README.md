# 📊 Customer Segmentation & Clustering — Full BI Project

A complete, production-ready analytics project to segment customers, discover actionable clusters, and deliver insights through **Power BI**, a **Streamlit web app**, and a **Flask REST API** — all powered by an advanced PostgreSQL backend with CTEs and window functions.

---

## 🚀 **Project Overview**

- **Domain:** E-commerce / Retail Analytics
- **Goal:** Analyze customer purchasing power and behavior to segment them into clusters for targeted marketing and retention strategies.
- **Core Steps:**
  - ETL raw CSV data
  - Apply K-Means clustering
  - Create a clean star schema in PostgreSQL
  - Build an advanced SQL view using CTEs & window functions
  - Visualize insights with an executive Power BI dashboard
  - Serve data dynamically via Streamlit and Flask API

---

## 🗂️ **Project Structure**

```plaintext
customer-segmentation-clustering/
├── data/                # Raw & cleaned CSV data
├── etl/                 # Python scripts for cleaning & clustering
├── sql/                 # SQL files for schema & advanced view
├── api/                 # Flask REST API
├── streamlit/           # Streamlit web app
├── bi/                  # Power BI .pbix file
├── presentation/        # Slides or Gamma link
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---
## ⚙️ **Tech Stack**

| Layer                          | Tools                             |
| ------------------------------ | --------------------------------- |
| **Data Cleaning & Clustering** | Python (`pandas`, `scikit-learn`) |
| **Database**                   | PostgreSQL                        |
| **API Service**                | Flask + Flask-CORS                |
| **Web App**                    | Streamlit + Plotly                |
| **BI Dashboard**               | Microsoft Power BI                |
| **Advanced SQL**               | CTEs, Window Functions            |

---

## 📌 **Key Features**
- Clean star schema with dimensions
- Clustering with K-Means for real customer segments
- Advanced SQL view using CTEs & window functions for rank, percentiles, and income gaps
- Interactive Streamlit web app for ad-hoc exploration
- REST API serving JSON for flexibility and security
- Storytelling Power BI dashboard with smart DAX measures & dynamic visuals
- Complete slide deck for presenting insights to stakeholders

---

## 🚀 **How to Run**
1️⃣ **Clone & Install**
```bash
git clone https://github.com/yourusername/customer-segmentation-clustering.git
cd customer-segmentation-clustering
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
2️⃣ **Prepare Data & Database**
- Download `Mall_Customers.csv` from [Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python?resource=download)

→ Place it in `data/raw/`.

- Create a PostgreSQL database named `customer_bi`.

- Run the ETL scripts:
```bash
python etl/clean_customers.py
python etl/load_to_postgres.py
python etl/cluster.py
```
- Apply the SQL schema and advanced view:
```bash
psql -U postgres -d customer_bi -f sql/01_star_schema.sql
psql -U postgres -d customer_bi -f sql/02_advanced_view.sql
```
---
3️⃣ **Start the Flask API**
```bash
cd api
python app.py
```
Check it:
```bash
http://localhost:5000/customers
```

---

4️⃣ **Launch the Streamlit Web App**
```bash
cd streamlit
streamlit run app.py
```

---

5️⃣ **Open Power BI**
- Open the `.pbix` file in `bi/Customer_Segmentation.pbix`
- Connect it to your local PostgreSQL database and refresh.

---

## 📑 **Slides**
- Find the presentation in presentation/Slides.pptx
- Or use the Gamma link if you have it in presentation/.

Covers:
- Project goals
- Data pipeline
- Clustering & advanced SQL
- Power BI storytelling
- Streamlit app
- API architecture
- Business recommendations

---

## 🎓 **Data Lineage**
```pgsql
Raw CSV 
  ↓
ETL (clean + cluster)
  ↓
PostgreSQL star schema
  ↓
CTEs & window functions (advanced view)
  ↓
 ├─ Power BI Dashboard
 ├─ Streamlit Web App
 └─ Flask REST API
```
---

## ✅ **What You’ll Learn**
- Modern ETL & schema design
- Clustering & segmentation with Python
- Advanced SQL for ranking & percentiles
- DAX and Power BI storytelling best practices
- How to build an interactive Streamlit app
- How to expose a secure Flask API

---

## 📜 **License**
This project is open-source for educational and portfolio purposes only.

---

## 🤝 **Connect**
- [LinkedIn](http://www.linkedin.com/in/sohilakabbas)
- sohilakhaled811@gmail.com

---













