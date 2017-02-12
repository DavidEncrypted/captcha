from setuptools import setup

setup(name="captcha",
      version='0.1',
      description='Catptcha breaking',
      url='',
      author='David Schep',
      author_email="david.schep7@gmail.com",
      license="MIT",
      packages=['captcha'],
      install_requires=[
          'bs4',
          'numpy',
          'PIL'
      ],
      zip_safe=False)