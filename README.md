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
