import pytest
from src.enterprise.apex_reports.service import ApexReportsService
def test_apex_reports_service():
    assert ApexReportsService().execute() == 'enterprise_ready'
