import pytest
from src.enterprise.omni_indexer.service import OmniIndexerService
def test_omni_indexer_service():
    assert OmniIndexerService().execute() == 'optimized'
