# GoldStrikes

GoldStrikes is a data processing tool designed to extract structural information from options chains (Barchart-compatible).

It converts raw CSV data into a simplified dataset containing key metrics used for market structure analysis.

---

## ⚙️ What it does

* Parses options chain data (calls and puts)
* Computes:

  * **Total Exposure** (Open Interest × Premium)
  * **Dominance Log** (call vs put imbalance)
* Outputs a clean dataset ready for visualization or trading systems

---

## 📥 Input

CSV file containing options data with:

* Strike (e.g. 4,320.00C / 4,320.00P)
* Open Interest
* Premium

---

## 📤 Output

Structured dataset:

| Strike | Total_Exposure | Dominance_Log |
| ------ | -------------- | ------------- |

---

## 🧠 Metrics

### Total Exposure

Represents capital concentration at each strike.

### Dominance Log

Measures directional imbalance:

* Positive → call dominance
* Negative → put dominance
* Near zero → equilibrium

---

## 🔄 Typical Workflow

1. Upload CSV
2. Process data
3. Export structured dataset
4. Use in trading platforms (e.g. MetaTrader)

---

## 🎯 Use Cases

* Key level detection
* Market regime analysis
* Quantitative trading tools

---

## 📜 License

MIT License
