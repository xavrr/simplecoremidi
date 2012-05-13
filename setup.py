from setuptools import setup, find_packages, Extension
import sys, os

version = '0.2'

install_requires = [
    # -*- Extra requirements: -*-
    ]

_scm_module = Extension(
    'simplecoremidi._simplecoremidi',
    sources=['simplecoremidi/_simplecoremidi.c'],
    extra_link_args=['-framework', 'CoreFoundation',
                     '-framework', 'CoreMIDI']
    )

setup(name='simplecoremidi',
      version=version,
      description="Simple OS X CoreMIDI interface",
      long_description=open("./README.md", "r").read(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        ],
      keywords='osx, CoreMIDI, MIDI, Mac OS X',
      author='Mike Verdone',
      author_email='mike.verdone+simplecoremidi@gmail.com',
      url='',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      ext_modules=[_scm_module],
      )
