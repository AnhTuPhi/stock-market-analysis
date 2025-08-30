# Stock Market Analysis

## 📋 Table of Contents

- [📖 Description](#-description)
- [📦 Boilerplate](#-boilerplate)
- [🕵️ Features](#-features)
- [⚙️ How it works?](#-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📖 References](#-references)
- [📄 License](#-license)

## 📖 Description

The Stock Market Analysis project focuses on collecting, processing, and analyzing stock market data to provide insights
into market trends, performance, and investment opportunities. The system integrates data from reliable financial APIs (
such as VNStock, stock company securities APIs) and applies statistical methods and visualization techniques to make raw
market data more understandable.

This project can serve as a decision-support tool for traders, investors, or researchers by transforming complex stock
data into actionable insights.

<!--
- Data Collection & Preprocessing: Fetch real-time and historical stock prices, indices, and trading volumes; clean and
normalize datasets for analysis.
- Visualization: Present stock trends through interactive dashboards, candlestick charts, moving averages, and sector-wise
comparisons.
- Exploratory Data Analysis (EDA): Identify patterns, correlations, and anomalies within stock data using descriptive
statistics and charts.
- Performance Evaluation: Analyze market indices (e.g., VNIndex, VN30) and individual stocks against benchmarks.
- Predictive Modeling (Optional): Use machine learning techniques (time series forecasting, regression, or deep learning
models like LSTM) to predict future price movements.
- Reporting & Insights: Generate automated reports summarizing daily/weekly market performance, highlighting opportunities
and risks.
-->

## 📦 Boilerplate

Fork from original
repo [clean architecture python boilerplate](https://github.com/AnhTuPhi/clean-architecture-python-boilerplate)

## 🕵️ Features

- Data Collection & Preprocessing: Fetch real-time and historical stock prices, indices, and trading volumes; clean and
  normalize datasets for analysis. (in developing)
- Visualization: Present stock trends through interactive dashboards, candlestick charts, moving averages, and
  sector-wise comparisons. (in developing)
- Exploratory Data Analysis (EDA): Identify patterns, correlations, and anomalies within stock data using descriptive
  statistics and charts. (in developing)
- Performance Evaluation: Analyze market indices (e.g., VNIndex, VN30) and individual stocks against benchmarks. (in
  developing)
- Predictive Modeling (Optional): Use machine learning techniques (time series forecasting, regression, or deep learning
  models like LSTM) to predict future price movements. (in developing)
- Reporting & Insights: Generate automated reports summarizing daily/weekly market performance, highlighting
  opportunities and risks. Also fetching report summarizing from multiple sources watchlist. (in developing)

## ⚙️ How it works?

### 🤖 Automated Data Collection

This project runs completely automatically using **Github Actions** - no server required - aiming to be serverless!

- ⏰ Schedule: Runs daily via **GitHub Actions workflow**
- 🔄 Process: Fetches latest results → Processes data → Commits to repository
- 📊 Analysis: Generates statistics and updates /data automatically

### 🕵️ Data Crawling Method

The data collection works by:

- 🔍 Network Analysis: Inspecting browser-server communication
- 🐍 Python Replication: Recreating the data fetch logic in Python
- 📋 Structured Storage: Saving results in JSONL format for easy analysis
- 🔄 Continuous Updates: Daily automated runs ensure fresh data

> **Note:** This is purely for educational and research purposes. No gambling advice is provided.

## 🚀 Installation & Usage

### Virtual environment

Create virtual enviroment

```sh
uv venv
```

Generate uv.lock

```sh
uv lock -v -U
```

Active environment

```sh
source .venv/Scripts/activate
```

Install main dependencies for prod

```sh
uv sync --frozen
```

Install main + dev dependencies

```sh
uv sync --group tools --group linting --group testing

```

Run service

```sh
uv run python xxx.py
```

> **Note:** In order to prevent conflicts in the production environment, it is important to utilize fixed versions of
> the main dependencies. If there are any packages that require updating, we will handle the process manually.

## 📖 References

Document references in [this]()

## 📄 License

This project is licensed under the MIT License - see
the [LICENSE](https://github.com/AnhTuPhi/stock-market-analysis/blob/master/LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>
