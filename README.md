# 🎯 Face Punching — Automatic Attendance System using OpenCV

> A real-time face recognition based attendance system built with Python and OpenCV. Just look at the camera — attendance ho jaata hai! 📸✅

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Setup & Installation](#-setup--installation)
- [Usage](#-usage)
- [Known Issues & Fixes](#-known-issues--fixes)
- [File Descriptions](#-file-descriptions)
- [Screenshots](#-screenshots)

---

## 🧠 About the Project

**Face Punching** is a smart attendance management system that uses your **webcam** to detect and recognize faces in real-time. Once a face is recognized, it automatically marks the person as **Present (P)** in a CSV file with the date as column.

No more manual roll calls. No proxy. Just your face. 👤

---

## ⚙️ How It Works

```
Step 1 → Register your face (Face.ipynb)
           └── Enter ID & Name
           └── Webcam captures 50+ face samples
           └── Saves to /faces folder

Step 2 → Train the model (train.ipynb)
           └── LBPH Face Recognizer reads all face images
           └── Trains on them and saves model to trainningData.yml

Step 3 → Mark Attendance (show.ipynb)
           └── Webcam opens in real-time
           └── Detects faces using Haar Cascade
           └── Predicts ID using trained model
           └── Matches ID → Name from Book1.csv
           └── Marks 'P' in the attendance sheet for today's date
```

---

## 📁 Project Structure

```
Face Punching - Open CV/
│
├── Face.ipynb                          # Step 1: Register face & capture samples
├── train.ipynb                         # Step 2: Train LBPH face recognizer
├── show.ipynb                          # Step 3: Real-time attendance marking
├── Date.ipynb                          # Utility: Date-related helpers
│
├── haarcascade_frontalface_default.xml # Haar Cascade for face detection
├── trainningData.yml                   # Saved trained model (generated)
├── Book1.csv                           # Attendance sheet (ID, Name, Dates...)
│
└── faces/                              # Captured face images
    ├── User.1.1.jpg
    ├── User.1.2.jpg
    └── ...
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| `Python 3.x` | Core language |
| `OpenCV (opencv-contrib-python)` | Face detection & recognition |
| `Haar Cascade Classifier` | Face detection |
| `LBPH Face Recognizer` | Face recognition (cv2.face module) |
| `Pandas` | Reading/writing CSV attendance data |
| `NumPy` | Image array processing |
| `Pillow (PIL)` | Image loading for training |

---

## 🔧 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/face-punching-attendance.git
cd face-punching-attendance
```

### 2. Install Dependencies

> ⚠️ **Important:** You must install `opencv-contrib-python` — NOT `opencv-python`. The `cv2.face` module (LBPH Recognizer) is only in the contrib version.

```bash
pip install opencv-contrib-python
pip install pandas numpy pillow
```

If you're using **conda/Miniconda**:

```bash
conda install -c conda-forge opencv
pip install opencv-contrib-python
```

### 3. Create Required Folders

```bash
mkdir faces
```

### 4. Download Haar Cascade XML

Download `haarcascade_frontalface_default.xml` from the [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project folder.

---

## 🚀 Usage

### Step 1 — Register a New Person

Open and run `Face.ipynb`:

```
Enter your id   → e.g., 1
Enter your name → e.g., Krishna
```

The webcam will open and capture **50 face samples** automatically. They get saved in the `faces/` folder as `User.{id}.{sampleNum}.jpg`.

---

### Step 2 — Train the Model

Open and run `train.ipynb`:

- Reads all images from `faces/` folder
- Trains the LBPH Face Recognizer
- Saves the model to `trainningData.yml`

> Training window will show each face as it processes. Press any key to skip or wait for it to finish.

---

### Step 3 — Take Attendance

Open and run `show.ipynb`:

```
Enter the date: → e.g., 2025-06-04
```

- Webcam opens and starts detecting faces
- Recognized faces get marked **P** under today's date in `Book1.csv`
- Press `q` to quit

---

## 🐛 Known Issues & Fixes

### ❌ `AttributeError: module 'cv2' has no attribute 'face'`

**Cause:** You installed `opencv-python` instead of `opencv-contrib-python`.

**Fix:**
```bash
pip uninstall opencv-python opencv-python-headless -y
pip install opencv-contrib-python
```

If using conda:
```bash
conda remove opencv
pip install opencv-contrib-python
```

---

### ❌ `KeyError: 'Id'`

**Cause:** Column name mismatch — CSV has `id` (lowercase) but code looks for `Id`.

**Fix:** Make sure your `Book1.csv` columns are exactly:
```
id, Name
```
And in `show.ipynb`, update the lookup to match:
```python
name = df[df['id'] == id]['Name'].values
```

---

### ❌ Webcam not opening / Black screen

- Check if another app is using the camera
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`

---

## 📄 File Descriptions

| File | Description |
|------|-------------|
| `Face.ipynb` | Registers a new user. Captures face samples via webcam and saves them. |
| `train.ipynb` | Trains the LBPH recognizer on captured face images. Saves model as `.yml`. |
| `show.ipynb` | Main attendance script. Detects & recognizes faces, marks attendance in CSV. |
| `Date.ipynb` | Helper notebook for date utilities. |
| `Book1.csv` | Attendance register — columns: `id`, `Name`, and one column per date. |
| `trainningData.yml` | Pre-trained LBPH model file. Auto-generated after running `train.ipynb`. |

---

## 📸 Sample Attendance CSV

| id | Name | 2025-06-01 | 2025-06-02 | 2025-06-04 |
|----|------|------------|------------|------------|
| 1  | Krishna | P | P | P |
| 2  | Rahul | P | | P |
| 3  | Priya | | P | P |

---

## 🙋 Author

Made with ❤️ by **Krishna**

> *"Ek baar face dikhao, attendance khud ho jaayegi."*

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).
