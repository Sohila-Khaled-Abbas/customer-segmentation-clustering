{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4b8cc9fd-3e0e-4255-a761-8dfa5f8dc39d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Segments updated in DB\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HELAL\\anaconda3\\Lib\\site-packages\\sklearn\\cluster\\_kmeans.py:1446: UserWarning: KMeans is known to have a memory leak on Windows with MKL, when there are less chunks than available threads. You can avoid it by setting the environment variable OMP_NUM_THREADS=1.\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "os.environ[\"OMP_NUM_THREADS\"] = \"1\"\n",
    "\n",
    "import pandas as pd\n",
    "from sklearn.cluster import KMeans\n",
    "from sqlalchemy import create_engine, text\n",
    "\n",
    "engine = create_engine('postgresql://postgres:203010@localhost:5432/customer_bi')\n",
    "\n",
    "# Load FACT table\n",
    "df = pd.read_sql('SELECT * FROM fact_customers', engine)\n",
    "\n",
    "# Cluster on Annual Income & Spending Score\n",
    "X = df[['annual_income', 'spending_score']]\n",
    "\n",
    "kmeans = KMeans(n_clusters=4, random_state=42)\n",
    "df['segment'] = kmeans.fit_predict(X)\n",
    "\n",
    "# Store segments in temp table\n",
    "df[['customer_id', 'segment']].to_sql('tmp_segments', engine, if_exists='replace', index=False)\n",
    "\n",
    "# ✅ Correct way to update: use `text`\n",
    "with engine.begin() as conn:\n",
    "    conn.execute(text(\"\"\"\n",
    "        UPDATE fact_customers\n",
    "        SET segment = tmp_segments.segment\n",
    "        FROM tmp_segments\n",
    "        WHERE fact_customers.customer_id = tmp_segments.customer_id;\n",
    "    \"\"\"))\n",
    "\n",
    "print(\"✅ Segments updated in DB\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
