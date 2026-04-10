from unittest.mock import MagicMock, patch
import pytest
from api_client import create_client, send_message, stream_message, APIError


def test_create_client_with_valid_key():
    client = create_client("sk-ant-test-key")
    assert client is not None


def test_create_client_with_empty_key_raises():
    with pytest.raises(APIError, match="API key"):
        create_client("")


def test_send_message_returns_text():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Hello from Claude")]
    mock_client.messages.create.return_value = mock_response

    result = send_message(
        client=mock_client,
        system="You are helpful.",
        messages=[{"role": "user", "content": "Hi"}],
        model="claude-sonnet-4-6",
        max_tokens=1024,
    )
    assert result == "Hello from Claude"
    mock_client.messages.create.assert_called_once()


def test_send_message_propagates_api_error():
    mock_client = MagicMock()
    mock_client.messages.create.side_effect = Exception("Connection failed")

    with pytest.raises(APIError, match="Connection failed"):
        send_message(
            client=mock_client,
            system="You are helpful.",
            messages=[{"role": "user", "content": "Hi"}],
            model="claude-sonnet-4-6",
            max_tokens=1024,
        )


def test_stream_message_yields_text_chunks():
    mock_client = MagicMock()
    mock_stream_context = MagicMock()
    mock_stream = MagicMock()
    mock_stream.text_stream = iter(["Hello", " from", " Claude"])
    mock_stream_context.__enter__ = MagicMock(return_value=mock_stream)
    mock_stream_context.__exit__ = MagicMock(return_value=False)
    mock_client.messages.stream.return_value = mock_stream_context

    chunks = list(stream_message(
        client=mock_client,
        system="You are helpful.",
        messages=[{"role": "user", "content": "Hi"}],
        model="claude-sonnet-4-6",
        max_tokens=1024,
    ))
    assert chunks == ["Hello", " from", " Claude"]


@pytest.mark.integration
def test_live_api_call():
    """Requires ANTHROPIC_API_KEY env var. Run with: pytest -m integration"""
    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        pytest.skip("ANTHROPIC_API_KEY not set")

    client = create_client(api_key)
    result = send_message(
        client=client,
        system="Reply with exactly: PONG",
        messages=[{"role": "user", "content": "PING"}],
        model="claude-sonnet-4-6",
        max_tokens=16,
    )
    assert "PONG" in result
