from setuptools import setup, find_packages
import os

version = "0.5"

setup(name='collective.prettyalbum',
      version=version,
      description="Extension for collective.prettyphoto",
      long_description="",
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      url='https://github.com/collective/collective.prettyalbum',
      keywords='web zope plone theme',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          'collective.prettyphoto',
          'plone.app.jquerytools',
      ],
      )
