from .interfaces import IAegisAuth
class AegisAuthService(IAegisAuth):
    def execute(self):
        return 'enterprise_ready'
