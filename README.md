[![Build Status](https://travis-ci.org/davidbetz/buildercreatorpy.svg?branch=master)](https://travis-ci.org/davidbetz/buildercreatorpy)

See test_provider.py unit test for usage.

Basically an implementation of an abstract factory pattern.

In one system where I use this, I create "Builder Creators" for each
type of thing in my system. So, SearchBuilderCreator, CloudStorageBuilderCreator,
QueueBuilderCreator, AristotleBuilderCreator, etc... These would implement
for ID interface like ICloudStorageProvider (in Python, it's just a class).

Each of these would have their own switch/case (or whatever) to create
the builder for it. So, for example, I may have config in a YAML file
specifying that I want to use Mongo for my Aristotle provider (
I'm never going to call it "NoSQL"; it's aristotelian!) Yet, I don't care.
My code using it SHOULD. NOT. CARE. ABOUT. MONGO. All I do is:

    some_provider = builder_creator.resolve(IAristotleProvider)


Also note that the resolver also accepts *args and **kwargs for extra
flexibility:

    provider = builder_creator.resolve(IAristotleProvider, "alternateConnectionString", collection="log") 

Despite what random bloggers say, service locators are awesome and provide
excellent decoupling.

Anyway, my explanation is lame. Just look at the unit test.

