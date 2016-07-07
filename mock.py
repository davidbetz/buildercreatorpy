from general.debug import log, logline, kwlog

from builder_creator import BuilderCreator, ProviderBase

class MockProviderBase():
    def execute(self, *args, **kwargs):
        raise NotImplementedError('execute is not implemented')

class BadMockProvider(ProviderBase, MockProviderBase):
    def execute_spelled_wrong(self, *args, **kwargs):
        pass

class MockProvider(ProviderBase, MockProviderBase):
    def execute(self, *args, **kwargs):
        param = ''
        if len(args) > 0:
            param = args[0]

        return "{}mock provider".format(param)

class MockAlternativeProvider(ProviderBase, MockProviderBase):
    def __init__(self, **kwargs):
        self.keyword_arguments = kwargs

    def execute(self, *args, **kwargs):
        arg = self.get_arg(0, *args)
        taco = self.get_kwarg('taco', **self.keyword_arguments)
        burrito = self.get_kwarg('burrito', **kwargs)
        result =  "{}{}alternative mock provider{}".format(arg, taco, burrito)
        return result

class MockProviderBuilder():
    def __init__(self):
        self.provider_type = type(MockProviderBase)

    def create(self, *args, **kwargs):
        kwlog(**kwargs)

        hint = None
        if len(args) > 0:
            hint = args[0].lower() 

        param = ''
        if len(args) > 1:
            param = args[1].lower() 

        example_provider_to_use_from_config_store = "mock" 

        provider = None

        name = (hint or example_provider_to_use_from_config_store or '').lower() 
        if name is None or len(name) == 0:
            return None 

        if name == "mock":
            provider = MockProvider() 
        elif name == "alt":
            provider = MockAlternativeProvider(**kwargs) 
        elif name == "bad":
            provider = BadMockProvider()
        else:
            raise ValueError("no") 

        return provider 