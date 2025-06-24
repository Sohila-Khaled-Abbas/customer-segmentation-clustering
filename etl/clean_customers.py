{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "36650470-adb2-4acc-86ad-b8f655eb7bbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   CustomerID  Gender  Age  Annual Income (k$)  Spending Score (1-100)\n",
      "0           1    Male   19                  15                      39\n",
      "1           2    Male   21                  15                      81\n",
      "2           3  Female   20                  16                       6\n",
      "3           4  Female   23                  16                      77\n",
      "4           5  Female   31                  17                      40\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 200 entries, 0 to 199\n",
      "Data columns (total 5 columns):\n",
      " #   Column          Non-Null Count  Dtype \n",
      "---  ------          --------------  ----- \n",
      " 0   CustomerID      200 non-null    int64 \n",
      " 1   Gender          200 non-null    object\n",
      " 2   Age             200 non-null    int64 \n",
      " 3   Annual_Income   200 non-null    int64 \n",
      " 4   Spending_Score  200 non-null    int64 \n",
      "dtypes: int64(4), object(1)\n",
      "memory usage: 7.9+ KB\n",
      "None\n",
      "✅ Cleaned data saved as customers_cleaned.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load Kaggle data\n",
    "df = pd.read_csv(\"mall_customers.csv\")\n",
    "\n",
    "print(df.head())\n",
    "\n",
    "# Rename columns for convenience\n",
    "df.columns = ['CustomerID', 'Gender', 'Age', 'Annual_Income', 'Spending_Score']\n",
    "\n",
    "# Check missing values\n",
    "print(df.info())\n",
    "\n",
    "# There are none in this dataset!\n",
    "\n",
    "# Save cleaned version\n",
    "df.to_csv(\"customers_cleaned.csv\", index=False)\n",
    "\n",
    "print(\"✅ Cleaned data saved as customers_cleaned.csv\")"
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
