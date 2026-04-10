import anthropic


class APIError(Exception):
    """Raised when an API call fails."""
    pass


def create_client(api_key: str) -> anthropic.Anthropic:
    if not api_key or not api_key.strip():
        raise APIError(
            "API key is required. Get one at https://console.anthropic.com/settings/keys"
        )
    return anthropic.Anthropic(api_key=api_key)


def send_message(
    client: anthropic.Anthropic,
    system: str,
    messages: list[dict],
    model: str,
    max_tokens: int,
) -> str:
    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        )
        return response.content[0].text
    except Exception as e:
        raise APIError(str(e)) from e


def stream_message(
    client: anthropic.Anthropic,
    system: str,
    messages: list[dict],
    model: str,
    max_tokens: int,
):
    try:
        with client.messages.stream(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        ) as stream:
            yield from stream.text_stream
    except Exception as e:
        raise APIError(str(e)) from e
