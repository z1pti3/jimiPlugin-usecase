from core import plugin, model

class _usecase(plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        model.registerModel("usecase","_usecase","_document","plugins.usecase.models.usecase")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("usecase","_usecase","_document","plugins.usecase.models.usecase")
        return True

    def upgrade(self,LatestPluginVersion):
        # if self.version < 0.5:
        #     pass
        return True
