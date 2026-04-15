# 🌐 DNS Benchmark

A **data-driven DNS benchmarking suite** that evaluates resolvers based on latency, stability, and reliability — delivering statistically grounded recommendations for real-world network conditions.

---

## 🎯 Objective

This project measures real DNS performance from the **user’s actual network**, helping answer:

* Which DNS is faster *here and now*?
* Which is more stable under real conditions?
* Which has the lowest tail latency?

---

## ⚙️ Methodology

Each resolver is tested using three query types:

### 🟢 Cached

* Queries to popular domains
* Expected cache hit
* Represents **real-world usage (majority of traffic)**

### 🔵 Uncached

* Randomized subdomains (forces recursion)
* Measures resolver + upstream performance

### 🟡 DotCom (NS)

* Queries to TLD nameservers
* Evaluates DNS infrastructure connectivity

---

## 📊 Metrics

The system computes:

* **Mean latency**
* **Min / Max**
* **Standard deviation**
* **P95 (tail latency)**
* **Coefficient of Variation (CV)** → stability
* **Failure rate**

---

## 🧠 Why this matters

DNS is not deterministic.

A resolver can have:

* low average latency ❌ but
* terrible tail latency ❌❌

This project focuses on:

> **consistency, reliability, and real-world performance**

---

## 🚀 Current Features

* Async DNS benchmarking engine
* Multiple samples per resolver
* Retry mechanism
* Separation by query type
* Statistical analysis (mean, std, p95, CV)
* Terminal output

---

## 🧪 Example Output

```
1.1.1.1 (cached)   | avg=82 ms | p95=83 ms | cv=0.01
8.8.8.8 (cached)   | avg=47 ms | p95=51 ms | cv=0.07
9.9.9.9 (cached)   | avg=84 ms | p95=87 ms | cv=0.02
```

---

## 🧾 Interpretation

* Lower latency = faster
* Lower P95 = fewer spikes
* Lower CV = more stable
* Failure rate > 0% = unreliable

---

## 🛠️ Installation

```bash
git clone https://github.com/<your-user>/dns-benchmark
cd dns-benchmark
python -m venv .venv
.venv\\Scripts\\activate
```

---

## ▶️ Usage

```bash
$env:PYTHONPATH="src"
python -m dns_benchmark.cli
```

---

## 📌 Important Notes

* Results depend on:

  * network conditions
  * ISP routing
  * time of day
* Always benchmark in your **actual usage environment**

---

## 🧭 Roadmap

* Composite scoring system (automatic recommendation)
* JSON export & historical comparison
* TUI interface (rich/textual)
* Advanced statistics (confidence intervals, outliers)
* DoH / DoT support
* Long-running monitoring mode

---

## 📡 Real-world context

This benchmark was tested on:

* Wired connection (Ethernet)
* Personal router (not ISP-provided)
* ONU + custom routing setup

→ Results reflect a controlled, low-interference environment.

---

## ⚖️ Philosophy

> “Measure reality. Don’t assume performance.”

---

## 📄 License

MIT
