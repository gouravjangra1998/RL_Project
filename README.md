# MSc Thesis: Reinforcement Learning for Autonomous SOC Defense

This repository contains the implementation, evaluation, and results of my MSc thesis project at the National College of Ireland. The project explores the use of **Reinforcement Learning (RL)** to build a **Digital Twin of a Security Operations Center (SOC)**, enabling autonomous defense against cyber threats.

## 🧠 Project Overview

- **Goal**: Compare PPO and A2C agents in defending a simulated SOC against various attacker profiles.
- **Environment**: Built on CybORG++, a modified version of CybORG for adversarial RL experimentation.
- **Prototype**: Includes a SOC-loop trace, action distribution analysis, and opponent pool evaluation.

## 📁 Contents

| File/Folder | Description |
|------------|-------------|
| `ppo_vs_a2c_results.ipynb` | Extracts key metrics: Detection Rate, Response Rate, MTTD, MTTR, Avg Reward |
| `final_graphs.ipynb` | Generates comparative plots and tables for thesis Section 5 |
| `soc_digital_twin_prototype.ipynb` | Simulates SOC-loop execution and evaluates robustness |
| `attacker_defender_demo.ipynb` | Demo of attacker-defender interaction loop |
| `models/` | Contains trained model ZIPs for PPO and A2C |
| `results/` | Screenshots, tables, and figures used in thesis documentation |

## 📊 Key Results

- **Detection Rate**: PPO outperforms A2C across attacker types
- **MTTD/MTTR**: PPO shows faster detection and recovery
- **Robustness**: PPO maintains stability against RandomRed and AggressiveRed, struggles with StealthyRed
- **Digital Twin SOC**: Successfully simulates defender response loop with traceable actions

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/gouravjangra1998/RL_Project.git
