from pathlib import Path
from typing import Any
import ujson as json
import os

ROOT = Path(__file__).resolve().parent.parent

os.makedirs(ROOT / "configs", exist_ok=True)

class CFG:
    def __init__(self):
        self.default = {
            "console_log_level": "debug",
            "file_log_level": "info",
            "enable_webui": True,
            "host": "127.0.0.1",
            "port": 8080,
            "bili_report_api": True,
            "reply_limit": 100,
            "enable_check_user": False,
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            }
        }
        self.content = self.read()

    def read(self) -> dict:
        try:
            with open(ROOT / "configs" / "main.json", "r", encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.default

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置项的值，如果不存在则返回默认值。

        :param key: 配置项的键
        :param default: 默认值
        :return: 返回配置项的值，类型是 Any
        """
        if default is not None:
            return self.content.get(key, default)
        return self.content.get(key, self.default.get(key))

    def update(self, key: str, value: Any) -> None:
        self.content[key] = value
        self.save()

    def save(self) -> None:
        with open(ROOT / "configs" / "main.json", "w", encoding='utf-8') as f:
            f.write(json.dumps(self.content, ensure_ascii=False, indent=4))

Config = CFG()