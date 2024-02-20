"""
Created on Fri 2nc Feb 2024
@author: Thomas Alscher, NHMD
"""

from setuptools import setup

setup(
    name='dasscotest',
    packages=['dasscotest'],
    package_dir={'':'src'},
    package_data={"dasscotest": ["*.json"]},
    version='1.0.5',
    author='Thomas Alscher',
    author_email='',
    python_requires='>3.9.0',
    description='dassco test ',

    install_requires=[
        "numpy >= 1.26.3",

    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)







