from .interfaces import IPlasmaCompiler
class PlasmaCompilerService(IPlasmaCompiler):
    def execute(self):
        return 'optimized'
