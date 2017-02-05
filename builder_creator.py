from provider_base import ProviderBase

class BuilderCreator():
    def __init__(self):
        self.creator = {}

    def set(self, creator):
        instance = creator()

        if not hasattr(instance, 'provider_type'):
            raise ValueError('creator required provider type')

        self.creator[instance.provider_type] = creator

    def remove(self, creator):
        self.creator.remove(creator)

    def resolve(self, provider, *args, **kwargs):
        provider_type = type(ProviderBase)

        if provider_type not in self.creator:
            return None

        creator = self.creator[provider_type]

        if creator is None:
            return None

        return creator().create(*args, **kwargs) 