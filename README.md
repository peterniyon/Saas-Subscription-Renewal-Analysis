# Saas-Subscription-Renewal-Analysis
📌 Project Description
This project aims to analyze customer behaviour and identify key factors influencing subscription renewals for a SaaS (Software-as-a-Service) company. The company has provided three datasets—client details, subscription records, and economic indicators—which will be merged and analyzed to answer specific business questions.

The core objectives are:

Determine the number of clients in the Fintech and Crypto industries.

Identify which industry has the highest subscription renewal rate.

Calculate the average inflation rate at the time customers renewed their subscriptions.

Through data cleaning, merging, and statistical analysis, this project will uncover trends and insights that can help the company improve customer retention, enhance strategic planning, and boost long-term growth.

---

# 📘 SaaS Subscription Renewal Analysis — Full Project Breakdown

---

## 🔖 Executive Summary 
- **Project Objective**: Identify key factors influencing SaaS subscription renewals.
- **Datasets Used**: `client_details.csv`, `subscription_records.csv`, `economic_indicators.csv`.
- **Key Questions**:
  1. How many Fintech and Crypto clients does the company have?
  2. Which industry has the highest renewal rate?
  3. What is the average inflation rate at the time of renewal?

---

## 📊 Section 1: Data Overview and Initial Understanding 
### 1.1 Dataset Descriptions
- Outline each dataset with its schema and example rows.
- Use data dictionaries to interpret variables clearly.

### 1.2 Business Relevance
- Why understanding **renewal drivers** is important in SaaS.
- How these insights drive **marketing, customer success, and product strategy**.

---

## 🧹 Section 2: Data Cleaning & Preprocessing 
### 2.1 Cleaning Strategy
- Check for missing/null values.
- Standardize formats (e.g., date formats, text casing).
- Convert categorical values into proper types.

### 2.2 Preprocessing Tasks
- Ensure all dates are `datetime` objects.
- Strip and normalize industry names (e.g., whitespace, casing).
- Check for duplicate `client_id`s or overlapping subscriptions.

---

## 🔗 Section 3: Data Integration and Merging 
### 3.1 Merge Client and Subscription Records
- Use `client_id` as the key.
- Result: A master dataset of clients and their subscription behaviour.

### 3.2 Merge with Economic Indicators
- For each subscription, match the `start_date` or `end_date` with the relevant quarterly economic indicator (e.g., using interval joins).

---

## 🧮 Section 4: Exploratory Data Analysis 
### 4.1 General Statistics
- Count of clients per industry.
- Distribution of subscription types (Monthly/Yearly).
- Proportion of renewals overall.

### 4.2 Specific Explorations
#### Fintech & Crypto Clients
```python
total_fintech_crypto_clients = len(client_details[client_details['industry'].isin(['Fintech', 'Crypto'])])
```

#### Renewal Rate by Industry
- Group by industry → calculate `renewal_rate = sum(renewed) / count`.
- Store the industry with the highest rate:
```python
top_industry = merged_data.groupby('industry')['renewed'].mean().idxmax()
```

#### Inflation at Time of Renewal
- Filter renewed = True
- Merge with `economic_indicators` using date matching
- Average inflation:
```python
average_inflation_for_renewals = renewed_data['inflation_rate'].mean()
```

### 4.3 Visualizations
- Pie chart of industries.
- Bar chart of renewal rate by industry.
- Line graph of inflation vs renewal count over time.

---

## 🧠 Section 5: Advanced Analytics **
### 5.1 Feature Engineering
- Subscription length
- Time since start
- Renewal flag as target

### 5.2 Predictive Modeling
- Logistic regression or decision tree to predict renewal likelihood.
- Feature importance plot to highlight what influences renewals most.

---

## 📌 Section 6: Business Insights and Interpretation 
- Which industries are most loyal?
- How macroeconomic indicators (like inflation) correlate with churn?
- What customer segments are most vulnerable to churn?

---

## 💼 Section 7: Strategic Recommendations 
- Create **targeted renewal campaigns** for industries with lower renewal rates.
- Improve customer experience for small companies (if they're more likely to churn).
- Use predictive analytics to flag high-risk clients for customer success teams.

---

## 📈 Section 8: Dashboard and Monitoring Suggestions 
- Build a dashboard using Power BI, Tableau, or Python Dash.
- Key KPIs:
  - Monthly Renewal Rate
  - At-Risk Clients
  - Renewal by Industry
  - Economic context (Inflation & GDP vs Renewal)

---

## 📂 Appendix
- Code snippets (Python / SQL)
- Data dictionaries
- Merged dataset schema
- Assumptions and limitations

---

## Tools You Might Use
| Task | Tool |
|------|------|
| Data wrangling | Python (Pandas), SQL |
| Modeling | scikit-learn |
| Visuals | Seaborn, Matplotlib, Plotly |
| Reporting | Word, LaTeX, Google Docs |
| Dashboard | Power BI, Tableau, Streamlit |

---
** gadstodoit
