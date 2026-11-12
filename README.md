# Chicken Disease Classification

End-to-end CNN web app that classifies chicken fecal images as **Healthy** or **Coccidiosis**.

**Live Demo:** *Add your Render URL here after deploy*  
*(Example: `https://chicken-disease-classifier.onrender.com`)*

**Tech stack:** TensorFlow/Keras · Flask · Docker · Render · DVC-ready ML pipeline

## How it works

1. Upload a fecal image in the browser.
2. The Flask API receives a base64 image and runs a trained CNN (`model/model.h5`).
3. The app returns **Healthy** or **Coccidiosis**.

Training runs locally via `main.py`. The deployed app exposes **inference only** (`/` and `/predict`).

## Local setup

### Clone

```bash
git clone https://github.com/KrupiRajendraPangam/End_To_End_Chicken_Disease_Classification.git
cd End_To_End_Chicken_Disease_Classification
```

### Create environment

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### Install and run (full training + app)

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:7860` (or the port shown in the terminal).

### Deploy-only deps (inference)

```bash
pip install -r requirements-deploy.txt
python app.py
```

## Deploy on Render (free)

1. Push this repo to **GitHub** (must include `model/model.h5`, `Dockerfile`, `app.py`).
2. Go to [https://render.com](https://render.com) → sign up with GitHub.
3. **New +** → **Web Service** → select this repository.
4. Settings:
   - **Language / Runtime:** Docker
   - **Branch:** `main` (or your default branch)
   - **Instance type:** Free
5. Click **Create Web Service** and wait for the build (TensorFlow image can take 10–20+ minutes).
6. Open the public URL Render gives you, upload an image, and test prediction.
7. Paste that URL into the **Live Demo** line above.

Notes:
- Free services **sleep** when idle; the first visit after sleep can take ~1 minute.
- If the free instance runs out of memory (TensorFlow is heavy), upgrade that one service to the cheapest paid instance, or ask for help shrinking the image.

Resume bullet:

> Built an end-to-end deep learning chicken disease classifier (CNN + Flask) and deployed a live inference demo on Render to detect Healthy vs Coccidiosis from fecal images.

## Docker (optional local)

Only if Docker Desktop is available:

```bash
docker build -t chicken-disease-classifier .
docker run -p 7860:7860 chicken-disease-classifier
```

## ML pipeline workflow (local)

1. Update `config/config.yaml`
2. Update `params.yaml`
3. Update entity / configuration manager / components / pipelines
4. Run `python main.py`
5. (Optional) `dvc repro` / `dvc dag`

## Optional: AWS / Azure container CI/CD

Optional if you already have a Render demo URL. Keep cloud credentials in secrets only — do not commit passwords to this README.
