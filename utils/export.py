import json
from datetime import datetime


def to_markdown(title: str, content: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"# {title}\n\n_Generated: {timestamp}_\n\n{content}"


def to_json(data: dict) -> str:
    return json.dumps(data, indent=2, default=str)


def get_download_filename(prefix: str, extension: str = "md") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"
