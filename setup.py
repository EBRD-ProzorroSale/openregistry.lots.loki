from setuptools import setup, find_packages
import os

version = '0.1'

entry_points = {
    'openregistry.lots.core.plugins': [
        'lots.ssp = openregistry.lots.ssp.includeme:includeme'
    ],
    'openregistry.tests': [
        'lots.ssp = openregistry.lots.ssp.tests.main:suite'
    ]
}

requires = [
    'setuptools',
    'openregistry.api',
    'openregistry.lots.core'
]

docs_requires = requires + [
    'sphinxcontrib-httpdomain',
]

setup(name='openregistry.lots.ssp',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      url='https://github.com/openprocurement/openregistry.lots.ssp',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openregistry', 'openregistry.lots'],
      include_package_data=True,
      zip_safe=False,
      extras_require={'docs': docs_requires},
      install_requires=requires,
      entry_points=entry_points,
      )
