from .interfaces import IPulsarQueue
class PulsarQueueService(IPulsarQueue):
    def execute(self):
        return 'optimized'
