from .ollama_client import generate as ollama_generate


def build_prompt(product: str, style: str) -> str:
    return (
        f"Write a concise product description in {style} style. "
        f"Use 60–120 words, plain language, and 2–3 short sentences. "
        f"Data: {product}"
    )


async def generate_description(product: str, style: str) -> str:
    prompt = build_prompt(product, style)
    return await ollama_generate(prompt)
