from .interfaces import IMatrixRatelimit
class MatrixRatelimitService(IMatrixRatelimit):
    def execute(self):
        return 'enterprise_ready'
