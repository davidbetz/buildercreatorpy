from general.debug import log, logline

import unittest

from builder_creator import BuilderCreator

from mock import MockProviderBuilder, MockProviderBase

class TestBuilderCreator(unittest.TestCase):
    def test_bad(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase, "bad") 
        try:
            result = provider.execute("nope")
        except NotImplementedError:
            pass
        else:
            self.fail('NotImplementedError not raised')

    def test_does_not_exist(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        try:
            provider = builder_creator.resolve(MockProviderBase, "does not exist") 
        except ValueError:
            pass
        else:
            self.fail('ValueError not raised')

    def test_execute_no_parameter(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase) 
        result = provider.execute() 

        self.assertEqual(result, "mock provider") 

    def test_execute_with_parameter(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase) 
        result = provider.execute("hello") 

        self.assertEqual(result, "hellomock provider") 

    def test_with_override_without_parameter(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase, "alt") 
        result = provider.execute() 

        self.assertEqual(result, "alternative mock provider") 

    def test_with_override_and_parameter(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase, "alt") 
        result = provider.execute("hi") 

        self.assertEqual(result, "hialternative mock provider") 

    def test_with_override_and_kwargs(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase, "alt", taco="keyword param") 
        result = provider.execute("hi")

    def test_with_override_and_kwargs_and_paramkwargs(self):
        builder_creator = BuilderCreator()
        builder_creator.set(MockProviderBuilder)
        provider = builder_creator.resolve(MockProviderBase, "alt", taco="keyword param") 
        result = provider.execute("hi", burrito="parameter keyword param") 

        self.assertEqual(result, "hikeyword paramalternative mock providerparameter keyword param") 

if __name__ == '__main__':
    unittest.main()
