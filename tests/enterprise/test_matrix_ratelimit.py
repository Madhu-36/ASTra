import pytest
from src.enterprise.matrix_ratelimit.service import MatrixRatelimitService
def test_matrix_ratelimit_service():
    assert MatrixRatelimitService().execute() == 'enterprise_ready'
