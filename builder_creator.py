from general.debug import log, logline

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

        log('resolve:kwargs', kwargs)
        return creator().create(*args, **kwargs) 

class ProviderBase():
    def get_kwarg(self, name, **kwargs):
        if name in kwargs:
            return kwargs[name]
        return ''

    def get_arg(self, name, *args):
        if len(args) > 0:
            return args[0]
        return ''

    def execute(self, required_parameter, *args):
        raise NotImplementedError('execute is not implemented')