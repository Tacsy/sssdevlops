#!/usr/bin/env python
#-*- coding: utf-8 -*-
import setuptools
import versioneer

if __name__ == "__main__":
    setuptools.setup(
        name='sssdevlops',
        version=versioneer.get_version(),
        description='summer school for python software development',
        author='Xuyan Ru',
        url="https://github.com/Tacsy/sssdevlops",
        license='',
        packages=setuptools.find_packages(),
        install_requires=[
            'sssdevlops',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'codecov'
            ],
            'develop': [
                'yapf',
                'versioneer'
                ]
        },

        tests_require=[
            'pytest',
        ],
        zip_safe=True,
    )
