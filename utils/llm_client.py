import os

from openai import OpenAI

from config import settings


def get_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY") or settings.OPENAI_API_KEY
    base_url = os.environ.get("OPENAI_BASE_URL") or settings.OPENAI_BASE_URL
    kwargs: dict = {"api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def chat(
    system_prompt: str,
    user_prompt: str,
    *,
    model: str | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
) -> str:
    client = get_client()
    model_name = os.environ.get("OPENAI_MODEL") or settings.OPENAI_MODEL
    response = client.chat.completions.create(
        model=model or model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature if temperature is not None else settings.TEMPERATURE,
        max_tokens=max_tokens or settings.MAX_TOKENS,
    )
    return response.choices[0].message.content or ""
