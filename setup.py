from distutils.core import setup

setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A library for assisting branch and bound operations',
  author = 'John Skeet',
  author_email = 'peterldowns@gmail.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
