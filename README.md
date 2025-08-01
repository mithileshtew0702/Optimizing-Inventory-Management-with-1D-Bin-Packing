# 📦 Optimizing Inventory with 1D Bin Packing

This project tackles the **1D Bin Packing Problem (1D-BPP)** in the context of inventory management using a **hybrid heuristic + genetic algorithm approach**. The solution was developed as part of the COMP2051 – *Artificial Intelligence Methods* module at the **University of Nottingham Ningbo China**.

> ✍️ Author: Mithilesh Tew  
> 🆔 Student ID: 20509703  

---

## 📚 Problem Overview

The **1D Bin Packing Problem** involves packing items of varying sizes into the fewest number of bins of fixed capacity `V`, without exceeding any bin’s limit.

This problem is **NP-hard**, which means exact solutions are impractical for large datasets. Instead, the focus is on building **metaheuristics** that can deliver high-quality solutions efficiently.

---

## 🔍 Project Objectives

- Implement an efficient algorithm to solve 1D-BPP for inventory optimization.
- Balance between solution quality and execution time (≤ 5 mins for 30 instances).
- Analyze performance compared to greedy and other metaheuristic methods.

---

## ⚙️ Methodology

### 🧠 Hybrid Strategy
- **Phase 1: Heuristic Initialization**
  - Used First-Fit (FF), First-Fit Decreasing (FFD), Best-Fit (BF), and Best-Fit Decreasing (BFD).
- **Phase 2: Genetic Algorithm Optimization**
  - Individuals = item order permutations
  - Operators: Tournament selection, Order Crossover (85%), Swap Mutation (20%)
  - Fitness: Number of bins used (lower is better)
  - Early stopping when no improvement within 20% of time limit

### 💻 Implementation
- **Language**: Python 3.10
- **Architecture**: Modular (IO handler, heuristics, GA optimizer)
- **Input**: JSON file with item sizes and bin capacities
- **Output**: JSON with bin configuration and performance stats
- **Runtime**: ~60–65 seconds for all 10 benchmark instances

---

## 📊 Results Summary

| Instance        | Best Known | My Result | Gap |
|----------------|------------|-----------|-----|
| instance 1     | 52         | 52        | 0   |
| instance 2     | 59         | 59        | 0   |
| instance 3     | 24         | 24        | 0   |
| instance 4     | 27         | 27        | 0   |
| instance 5     | 47         | 47        | 0   |
| instance 6     | 49         | 49        | 0   |
| instance 7     | 36         | 36        | 0   |
| instance 8     | 52         | 52        | 0   |
| instance 9     | 417        | 417       | 0   |
| instance 10    | 375        | **373**   | ✅ -2 |

**Total Bins Used:** 1136 (vs 1138 best known)  
**Speed:** All instances solved under 65 seconds  
**Highlight:** Outperformed best-known result on largest instance

---

## 🧠 Critical Analysis

- ✅ Hybrid approach outperforms pure heuristics, GA, and simulated annealing
- 🔁 Heuristic phase gives quick base solutions
- 🧬 GA phase improves quality while managing runtime
- 🏆 Beat best-known solution for instance 10 by using only 373 bins

---

## 🛠️ Files Included

- `main.py` – Hybrid heuristic + GA implementation
- `CW_ins.json` – Input problem instances
- `solution.json` – Output bin configurations
- `report.pdf` – Full write-up (submitted coursework)

---

## 🧠 Future Improvements

- Add **adaptive mutation and population sizing**
- Integrate **Tabu Search** or **Simulated Annealing** in GA loop
- Explore **machine learning** for parameter tuning

---

## 📌 Declaration of AI Usage

> This project used AI assistance (ChatGPT) for coding support and report writing under declared guidelines.

---

## 🧾 Lecturer Feedback

**Solution (30):** 33  
**Code (30):** 25  
**Note:**  
**Comment:** Outstanding (21-30) near perfect design of program/data structure. Variables/functions formats are excellently named and chosen. Excellent balance of brievty and clarity in comments.  

**Report (40):** 33  
**Note:** zip file uploaded, -5  
**Comment:** This is an exemplary report: it is exceptionally well-structured, uses precise academic language, and covers all required elements with technical clarity and professional presentation. The introduction defines the problem, its mathematical foundation, and strong real-world relevance with clear referencing. Methodology is highly detailed and justified, clearly explaining hybrid approaches, encoding strategies, parameter choices, and technical implementation. Results are benchmarked, tabulated, and analyzed, with clear critical comparison between methods and genuine reflection on strengths and limitations. Conclusions are concise, insightful, and forward-looking, with ambitious, practical recommendations. Overall, this is a top-band submission demonstrating technical depth, originality, and excellent academic standards.
