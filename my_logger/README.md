# 🧾 my_logger

Simple colorized logger with both console and file output.

---

## ⚙️ Features
- Colorized output using `colorama`
- File and console logging
- Automatic log directory creation
- Customizable log file names
- Works perfectly with async or sync apps

---

## 🧠 Example

```python
from my_logger import setup_logger

logger = setup_logger("my_app", "my_app.log")

logger.info("App started successfully!")
logger.warning("Low memory!")
logger.error("Something went wrong!")
