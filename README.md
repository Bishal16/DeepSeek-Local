# Run DeepSeek-R1 model Locally with Streamlit UI

This guide will walk you through setting up and running the **deepseek-r1:7b** locally using **Ollama** and accessing it via a **Streamlit-based web UI**.

---

## 🚀 Installation & Setup

### 1️⃣ Install Ollama
Ollama is required to run the DeepSeek model locally.

#### **For Linux:
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

#### **For Windows/macOs**:
Download and install Ollama from [here](https://ollama.com/download).

---

### 2️⃣ Pull the deepseek-r1:7b Model
Once Ollama is installed, run the following command to download the **deepseek-r1:7b** or any ohter perfered model:

```sh
ollama pull deepseek-r1:7b
```

> **Note:** This will download a large model (approx **4.7GB**). Ensure you have enough disk space.

---

### 3️⃣ Verify Model in Terminal
To confirm the model is installed correctly, test it in the terminal:

```sh
ollama run deepseek-r1:7b
```

Type any prompt to check if it's responding correctly.

---

## 🖥️ Running DeepSeek via Streamlit

### 4️⃣ Install Python & Virtual Environment (Optional but Recommended)

If you haven't installed Python, get it from [python.org](https://www.python.org/downloads/).

Then, create a virtual environment to keep dependencies clean:

```sh
python -m venv deepseek_env
source deepseek_env/bin/activate  # For Linux/macOS
# or
deepseek_env\Scripts\activate  # For Windows
```

---

### 5️⃣ Install Dependencies

Inside your activated virtual environment, install the required Python packages:

```sh
pip install streamlit requests
```

---

### 6️⃣ Clone This Repository (Optional)
If you're hosting this on GitHub and want to set it up quickly:

```sh
git clone https://github.com/Bishal16/DeepSeek-Local.git
cd deepseek-streamlit
```

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username.

---

### 7️⃣ Run the Streamlit App

Start the UI by running:

```sh
streamlit run app.py
```

This will launch the **DeepSeek Web UI** in your browser.

---

### 🤝 Contributing
Pull requests and improvements are always welcome! Feel free to fork and modify as needed.

---

🚀 **Enjoy running DeepSeek locally with a custom web UI!** 🚀
