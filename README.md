---

# 🧠 YOLOv8 Custom Object Detection Project

## 📘 Overview

This project demonstrates how to **create a custom object detection model using YOLOv8**.
It covers:

* Annotating a dataset in **Roboflow**
* Exporting it in a **YOLOv8-compatible format**
* Fine-tuning the YOLOv8 model on your custom dataset
* Integrating the model with a **webcam** for real-time detection using `webcam_test.py`

The goal is to provide a **generic and reusable template** for building and deploying YOLOv8-based detection systems (e.g., head detection or similar vision tasks).

---

## ⚙️ Prerequisites

* **Python 3.8+**

* **Roboflow account** (Free tier available at [roboflow.com](https://roboflow.com))

* **Libraries:**

  ```bash
  pip install ultralytics opencv-python
  ```

* **Webcam** (for real-time testing)

* *(Optional)* **GPU** for faster training (requires CUDA setup)

### 🧩 Setup Virtual Environment

```bash
python -m venv yolov8_env
source yolov8_env/bin/activate  # On Linux/Mac
# Or on Windows:
yolov8_env\Scripts\activate
pip install -r requirements.txt
```

**Sample `requirements.txt`:**

```text
ultralytics
opencv-python
numpy
torch  # if not already installed by ultralytics
```

---

## 🖼️ Step 1: Annotate Dataset in Roboflow

1. **Sign up or log in** at [app.roboflow.com](https://app.roboflow.com)
2. **Create a new project:**
   Choose **"Object Detection"** and provide a name (e.g., `Custom-Head-Detection`).
3. **Upload images:**
   Aim for **500–1000 images** with diverse conditions.
4. **Annotate images:**

   * Use the **Bounding Box (B)** or **Polygon** tool.
   * Label each object (e.g., `head`).
   * Optionally use **AI-assisted labeling** to speed up the process.
5. **Split dataset:**
   Default split — 70% train / 20% validation / 10% test.
6. **Apply preprocessing/augmentations:**
   Resize, auto-orient, flip, rotate, etc.

> Roboflow Annotate supports **bounding boxes, polygons**, and **AI-assisted tools** for faster labeling.

---

## 📦 Step 2: Download Dataset for YOLOv8

YOLOv8 expects datasets in this structure:

```
train/
   ├── images/
   └── labels/
valid/
test/
data.yaml
```

### 🔽 Export from Roboflow

1. In your Roboflow project, click **"Generate Version"**
2. Choose **"YOLOv8"** as the export format
3. Click **"Download ZIP"** or use Python SDK

### 🧰 Programmatic Download (Python)

```bash
pip install roboflow
```

```python
from roboflow import Robof
```

---