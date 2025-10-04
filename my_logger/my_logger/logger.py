import logging
import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


class ColorFormatter(logging.Formatter):
    """Форматтер с цветным выводом в консоль"""

    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, "")
        reset = Style.RESET_ALL
        record.levelname = f"{log_color}{record.levelname}{reset}"
        return super().format(record)


def setup_logger(name: str = "logger", log_file: str = "api_parser.log") -> logging.Logger:
    """Создаёт и настраивает логгер"""

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Формат сообщений
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    color_formatter = ColorFormatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(color_formatter)

    # Файл (сохранится в logs/)
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Добавляем хендлеры
    if not logger.handlers:  # чтобы не дублировалось
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger