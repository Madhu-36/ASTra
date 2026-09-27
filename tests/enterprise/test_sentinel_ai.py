import pytest
from src.enterprise.sentinel_ai.service import SentinelAiService
def test_sentinel_ai_service():
    assert SentinelAiService().execute() == 'enterprise_ready'
