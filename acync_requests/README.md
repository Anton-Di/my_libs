# async_requests

A lightweight asynchronous HTTP request helper built on top of **httpx**.  
Provides simple `get` and `post` functions with automatic response parsing (JSON / text / bytes).

---

## 🚀 Features

- Asynchronous GET and POST requests  
- Automatic response format detection  
  - JSON → `dict`  
  - Text / HTML → `str`  
  - Other (images, PDFs, etc.) → `bytes`  
- Built-in error handling  
- Lightweight — only depends on `httpx`

---

## 📦 Installation

### Local installation
```bash
pip install -e .

### ⚙️ Requirements

- Python ≥ 3.10  
- httpx ≥ 0.28.0