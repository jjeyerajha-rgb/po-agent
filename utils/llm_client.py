from openai import OpenAI
from config import settings


def get_client() -> OpenAI:
    kwargs: dict = {"api_key": settings.OPENAI_API_KEY}
    if settings.OPENAI_BASE_URL:
        kwargs["base_url"] = settings.OPENAI_BASE_URL
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
    response = client.chat.completions.create(
        model=model or settings.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature if temperature is not None else settings.TEMPERATURE,
        max_tokens=max_tokens or settings.MAX_TOKENS,
    )
    return response.choices[0].message.content or ""
