# 🧰 My Python Libraries

A collection of my personal Python packages and tools.  
Each library is self-contained and can be used independently.

---

## 📦 Included Packages

### 🔹 [async_requests](./async_requests)
Lightweight asynchronous HTTP helper built on top of **httpx**.

**Features:**
- Async GET and POST requests  
- Automatic response format detection (`JSON` → `dict`, `text` → `str`, etc.)  
- Built-in error handling  
- Lightweight and dependency-minimal  

📄 [README](./async_requests/README.md) | 🧩 [Source](./async_requests/async_requests)

---

### 🔹 [my_logger](./my_logger)
Colorized logger for Python with both **console** and **file** output.

**Features:**
- Colorized output with `colorama`  
- File and console handlers  
- Automatic `logs/` folder creation  
- Simple API: `setup_logger("app_name")`

📄 [README](./my_logger/README.md) | 🧩 [Source](./my_logger/my_logger)

---

## ⚙️ Installation (for local development)

Clone this repository:
```bash
git clone https://github.com/Anton-Di/my_libs.git
cd my_libs

Install any library locally:

pip install -e ./async_requests
pip install -e ./my_logger

Or install directly from GitHub:

pip install git+https://github.com/Anton-Di/my_libs.git@main#subdirectory=async_requests
pip install git+https://github.com/Anton-Di/my_libs.git@main#subdirectory=my_logger

