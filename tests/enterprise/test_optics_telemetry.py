import pytest
from src.enterprise.optics_telemetry.service import OpticsTelemetryService
def test_optics_telemetry_service():
    assert OpticsTelemetryService().execute() == 'enterprise_ready'
