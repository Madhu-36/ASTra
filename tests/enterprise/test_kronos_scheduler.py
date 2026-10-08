import pytest
from src.enterprise.kronos_scheduler.service import KronosSchedulerService
def test_kronos_scheduler_service():
    assert KronosSchedulerService().execute() == 'optimized'
