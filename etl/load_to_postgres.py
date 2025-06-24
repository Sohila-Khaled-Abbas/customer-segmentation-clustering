{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "9d7cf11d-3f86-4c50-9df9-0fbbb8e604d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['CustomerID', 'Gender', 'Age', 'Annual_Income', 'Spending_Score',\n",
      "       'Age_Label', 'gender', 'gender_id', 'age_min', 'age_max', 'age_label',\n",
      "       'age_range_id'],\n",
      "      dtype='object')\n",
      "✅ FACT table loaded with proper foreign keys!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine, text\n",
    "\n",
    "engine = create_engine('postgresql://postgres:203010@localhost:5432/customer_bi')\n",
    "\n",
    "# Drop old tables\n",
    "with engine.begin() as conn:\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS fact_customers;\"))\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS dim_genders;\"))\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS dim_age_ranges;\"))\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv(\"customers_cleaned.csv\")\n",
    "\n",
    "# Make DIM: Gender\n",
    "genders = pd.DataFrame(df['Gender'].unique(), columns=['gender'])\n",
    "genders['gender_id'] = genders.index + 1\n",
    "genders.to_sql('dim_genders', engine, if_exists='replace', index=False)\n",
    "\n",
    "# Make DIM: Age Ranges\n",
    "bins = [0, 20, 30, 40, 50, 100]\n",
    "labels = [\"<20\", \"20-29\", \"30-39\", \"40-49\", \"50+\"]\n",
    "df['Age_Label'] = pd.cut(df['Age'], bins=bins, labels=labels)\n",
    "\n",
    "age_ranges = pd.DataFrame({\n",
    "    'age_min': bins[:-1],\n",
    "    'age_max': bins[1:],\n",
    "    'age_label': labels\n",
    "})\n",
    "age_ranges['age_range_id'] = age_ranges.index + 1\n",
    "age_ranges.to_sql('dim_age_ranges', engine, if_exists='replace', index=False)\n",
    "\n",
    "# Map IDs\n",
    "dim_gender = pd.read_sql('SELECT * FROM dim_genders', engine)\n",
    "dim_age = pd.read_sql('SELECT * FROM dim_age_ranges', engine)\n",
    "\n",
    "df = df.merge(dim_gender, left_on='Gender', right_on='gender', how='left')\n",
    "df = df.merge(dim_age, left_on='Age_Label', right_on='age_label', how='left')\n",
    "\n",
    "print(df.columns)\n",
    "\n",
    "# Now build FACT\n",
    "fact = df[['CustomerID', 'gender_id', 'age_range_id', 'Age', 'Annual_Income', 'Spending_Score']]\n",
    "fact.columns = ['customer_id', 'gender_id', 'age_range_id', 'age', 'annual_income', 'spending_score']\n",
    "\n",
    "fact.to_sql('fact_customers', engine, if_exists='replace', index=False)\n",
    "\n",
    "print(\"✅ FACT table loaded with proper foreign keys!\")"
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
