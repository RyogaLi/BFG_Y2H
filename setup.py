#!/usr/bin/env python3.7

# Author: Roujia Li
# email: Roujia.li@mail.utoronto.ca

import pathlib
from setuptools import setup, find_packages

########################################
# set up file for packaging the project
# 1. change the version of the project (pypi doesn't allow the same version number)
# 2. To build from source (also in tmp_update.sh)
#    * Run `python setup.py bdist_wheel`
#    * Run `python -m pip install dist/BFG-Y2H-0.***.tar.gz`
# 3. To upload to pypi
#    * Run `python setup.py bdist_wheel`
#    * Run `twine upload dist/BFG-Y2H-0.***.tar.gz`
# 4. Note: to prevent potential problems of the wheel file, remove the older version before building a new one
#     (remove build/ and dist/)
########################################

here = pathlib.Path(__file__).parent.resolve()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="BFG-Y2H",
    version="0.1.1",
    author="ROUJIA LI",
    author_email="roujia.li@mail.utoronto.ca",
    description="Analysis scripts for BFG-Y2H data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RyogaLi/BFG_Y2H",
	scripts=['bin/bfg', 'bin/rc'],
	package_data={'bfg_analysis': ['data/*']},
	# For a list of valid classifiers, see https://pypi.org/classifiers/
	classifiers=[  # Optional
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',

		# Pick your license as you wish
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate you support Python 3. These classifiers are *not*
		# checked by 'pip install'. See instead 'python_requires' below.
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
	packages=find_packages(),  # Optional
	install_requires=['pandas', 'seaborn', 'numpy', 'biopython'],
    python_requires='>=3.6',

	# # To provide executable scripts, use entry points in preference to the
	# # "scripts" keyword. Entry points provide cross-platform support and allow
	# # `pip` to create the appropriate form of executable for the target
	# # platform.
	# #
	# # For example, the following would provide a command called `sample` which
	# # executes the function `main` from this package when invoked:
	# entry_points={  # Optional
	# 	'console_scripts': [
	# 		'sample=sample:main',
	# 	],
	# },
)
