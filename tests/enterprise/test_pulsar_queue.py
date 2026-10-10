import pytest
from src.enterprise.pulsar_queue.service import PulsarQueueService
def test_pulsar_queue_service():
    assert PulsarQueueService().execute() == 'optimized'
