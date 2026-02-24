# 🧗 The Iron-Clad Data Science Ladder

> _"If it isn't in a repo, it doesn't exist."_

This repository documents a structured, no-shortcuts journey from **Python Engineer → Data Scientist → ML Engineer → Deep Learning → NLP → Computer Vision → Robotics**. The full plan is divided into 6 coding phases, each building directly on the last, and each ending with a real capstone project.

---

## 📋 The Daily Operating System (3–5 Hours/Day)

Every study day follows the same structure to fight the memory leak problem:

| Hour                             | Activity                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Hour 1** — The Intake          | Theory only. Watch videos / read docs. Hard stop at 1 hour.                                     |
| **Hours 2–3** — The Lab          | Write the code from scratch, without looking at the tutorial. If you peek, you reset the timer. |
| **Hour 4** — The Integration     | Add what you learned today to yesterday's project. Keep building.                               |
| **Hour 5** — Review _(optional)_ | Debugging and git commits. No code stays on your PC overnight.                                  |

---

## 🗺️ Full Learning Roadmap

### 🏗️ Phase 0 — The Python Engineer _(Weeks 1–4)_

**Goal:** Stop writing "Scripting Python" and start writing "Software Python." Data science pipelines are complex software systems.

| Topic                           | The Real Task                                                                                   | Retention Check                                                |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **1. Git**                      | Create a repo. Learn `init`, `add`, `commit`, `push`.                                           | Rule: No code stays on your PC overnight. Push everything.     |
| **2. Modular Python & Logging** | Create a `logger.py` module. Import it into a main script.                                      | Stop using `print()`. Use `logging.info()`.                    |
| **3. OOP & Exceptions**         | Create a `DataHandler` class. It must ingest a CSV and crash gracefully if the file is missing. | If your code crashes with a raw traceback, you fail. Catch it. |
| **4. SQLite & Persistence**     | Save your processed data to `data.db` via your class methods.                                   | Write a query to fetch the last 5 entries.                     |

🔥 **Capstone 1 — The "Life Logger" CLI**

> A terminal app to track your 3–5 hours of study.
>
> - **Input:** `python run.py --add "Studied Pandas" --hours 3`
> - **Logic:** A `StudySession` class validates input (no negative hours)
> - **Storage:** Saves to SQLite
> - **Output:** `logging` writes "Session saved" to `app.log`
> - **Git:** Push it.

📁 **Folder:** `Phase 0/` ← _You are here_

---

### 📊 Phase 1 — The Data Mechanic _(Weeks 5–9)_

**Goal:** You cannot model what you cannot clean.
**Focus:** Pandas, NumPy, Visualization, Statistics.

| Topic                      | The Real Task                                                                | Retention Check                                     |
| -------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------- |
| **5. NumPy & Vectors**     | Manually implement Mean Squared Error using numpy arrays — no loops allowed. | Speed test: Loop vs Vectorization.                  |
| **6. Pandas Core**         | Load a messy dataset. Fix dates, handle NaNs, filter rows.                   | Do it without opening the CSV in Excel.             |
| **7. EDA & Viz (Seaborn)** | Plot distributions. Find outliers. Write a paragraph explaining WHY.         | A chart without a conclusion is useless.            |
| **8. Probability & Stats** | Generate a Normal Distribution in code. Calculate Z-scores for your data.    | Use `scipy` to prove if two columns are correlated. |

🔥 **Capstone 2 — The "Automated Analyst"**

> A script that takes ANY raw CSV and generates a full report.
>
> - **Ingest:** `pd.read_csv()` on a generic file
> - **Clean:** Auto-fill missing values with column mean (using OOP skills from Phase 0)
> - **Visual:** Generate a `.png` histogram for every numeric column
> - **Stats:** Log the "Skewness" of every column to a file

📁 **Folder:** `Phase 1/`

---

### 🤖 Phase 2 — Machine Learning _(Weeks 10–18)_

**Goal:** Predict the future.
**Focus:** Scikit-Learn, Algorithms, Feature Engineering.

| Topic                             | The Real Task                                                 | Retention Check                                  |
| --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------ |
| **9. Linear/Logistic Regression** | Predict Housing Prices. Predict Diabetes.                     | Plot the Decision Boundary or Regression Line.   |
| **10. Trees & Forests**           | Visualize a single Decision Tree. Then train a Random Forest. | Compare accuracy. Why did RF win? Write it down. |
| **11. Boosting (XGBoost)**        | The holy grail of tabular data. Tune hyperparameters.         | Beat your Random Forest score.                   |
| **12. Unsupervised (K-Means)**    | Cluster customers based on spending.                          | Visualize the clusters in 2D using PCA.          |
| **13. Evaluation Metrics**        | Implement Precision/Recall manually.                          | Don't just trust `accuracy_score`.               |

🔥 **Capstone 3 — The "Streamlit Predictor"**

> Your first web app.
>
> - **Model:** Train an XGBoost model on the Titanic or Heart Disease dataset
> - **Pipeline:** Use `sklearn.pipeline` to bundle cleaning + modelling
> - **UI:** Build a Streamlit app with sliders for user input and a "Predict" button
> - **Deployment:** Run locally. _(Bonus: deploy to Streamlit Cloud)_

📁 **Folder:** `Phase 2/` _(coming soon)_

---

### 🧠 Phase 3 — Deep Learning _(Weeks 19–22)_

**Goal:** Beyond tabular data. Understanding complexity.
**Focus:** PyTorch, Neural Nets. _(We switch to PyTorch here — it is the language of Research and Robotics.)_

| Topic                       | The Real Task                                           | Retention Check                                 |
| --------------------------- | ------------------------------------------------------- | ----------------------------------------------- |
| **14. Tensors & Gradients** | Manual Backpropagation (Micrograd style).               | Understand `requires_grad=True`.                |
| **15. ANN — The Basics**    | Build a Feed-Forward net for MNIST (Digit recognition). | Plot the Loss Curve over epochs.                |
| **16. Optimization**        | SGD vs Adam. Experiment with Learning Rates.            | Break the model (make it diverge), then fix it. |

🔥 **Capstone 4 — The "Digit Recognizer" from Scratch**

> Build a neural network **without** a high-level API wrapper first, then rebuild it properly with `PyTorch nn.Module`.

📁 **Folder:** `Phase 3/` _(coming soon)_

---

### 🗣️ Phase 4 — NLP _(Weeks 23–30)_

**Goal:** Teaching machines to read.
**Focus:** Text, RNNs, Transformers.

| Topic                | The Real Task                             | Retention Check                                    |
| -------------------- | ----------------------------------------- | -------------------------------------------------- |
| **17. Embeddings**   | Word2Vec. Visualizing words in 3D space.  | Find the closest word to "King" − "Man" + "Woman". |
| **18. RNN/LSTM/GRU** | Text Classification (Sentiment Analysis). | Why does Vanishing Gradient happen? Simulate it.   |
| **19. Transformers** | The Attention Mechanism. HuggingFace.     | Fine-tune BERT on a custom dataset.                |

🔥 **Capstone 5 — The "Context Chatbot"**

> A bot that answers questions based on a PDF you upload.
>
> - **Tech:** HuggingFace Transformers + FAISS (Vector DB)
> - **Task:** RAG (Retrieval Augmented Generation)

📁 **Folder:** `Phase 4/` _(coming soon)_

---

### 👁️ Phase 5 — Computer Vision _(Weeks 31–38)_

**Goal:** Teaching machines to see.
**Focus:** CNNs, Images, Object Detection. _(This is the bridge to Robotics.)_

| Topic                     | The Real Task                                                    | Retention Check                                      |
| ------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| **20. CNNs**              | Build a ConvNet for CIFAR-10 (Image classification).             | Visualize the "Feature Maps" (what the filter sees). |
| **21. Transfer Learning** | Use ResNet50. Fine-tune it to classify "Hot Dog vs Not Hot Dog". | Freeze layers vs Unfreeze layers.                    |
| **22. Object Detection**  | YOLO (You Only Look Once). Detect cars in video.                 | Draw bounding boxes in real-time.                    |

🔥 **Capstone 6 — The "Vision Security System"**

> Webcam integration with real-time detection.
>
> - **Input:** OpenCV reads webcam feed
> - **Model:** YOLOv8 detects "Person"
> - **Logic:** If "Person" detected, log timestamp to SQLite _(using Phase 0 skills!)_

📁 **Folder:** `Phase 5/` _(coming soon)_

---

### 🤖 Final Frontier — Robotics Prep

**Goal:** Apply everything to the physical world.

- **ROS2** (Robot Operating System) — The middleware of robotics
- **SLAM** — Simultaneous Localization and Mapping
- **Reinforcement Learning** — Teaching a robot to walk (simulated)

---

## ⚠️ The "Senior Dev" Retention Protocols

> These rules apply to **every single day** of the journey:

1. **The 20-Minute Rule** — Stuck? Debug for 20 minutes. Read the error. Print the variables. _Then_ ask AI.
2. **Spiral Learning** — Every project must use a **database** (Phase 0 skill) and a **visualization** (Phase 1 skill). Never drop the basics.
3. **Code Reviews** — Once a week, ask ChatGPT: _"Roast my code. Tell me why it is not production ready."_ Then fix it.

---

---
