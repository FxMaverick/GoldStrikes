# GoldStrikes

GoldStrikes is a Python tool that processes options chain CSV data (Barchart-compatible) to extract key structural metrics for trading.

The output is optimized for direct use in **MetaTrader 5 (MQL5)**.

---

## ⚙️ What it does

* Parses raw options chain data (calls and puts)
* Computes:

  * **Total Exposure** (Open Interest × Premium)
  * **Dominance Log** (call vs put imbalance)
* Exports a clean **CSV dataset ready for MT5**

---

## 📥 Input

CSV file containing options data with:

* Strike (e.g. `4,320.00C`, `4,320.00P`)
* Open Interest
* Premium

---

## 📤 Output (MT5-ready)

```text
Strike,Total_Exposure,Dominance_Log
4400.00,114419200,2.27
4350.00,18076500,2.41
4320.00,441070,-3.55
```

### Format rules

* Comma-separated (`,`)
* Dot decimals (`.`)
* No thousands separators
* Sorted by **Strike (descending)**

---

## 🚀 Usage

```bash
python goldstrikes.py input.csv
```

Optional output name:

```bash
python goldstrikes.py input.csv GoldStrikes.csv
```

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

## 🎯 Use Cases

* Key level detection
* Market structure analysis
* Integration with MetaTrader indicators (MQL5)

---

## 📜 License

MIT License
