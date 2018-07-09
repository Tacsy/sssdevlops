#!/usr/bin/env python
#-*- coding: utf-8 -*-
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='sssdevlops',
        version="1",
        description='summer school for python software development',
        author='',
        url="https://github.com/Tacsy/sssdevlops",
        license='',
        packages=setuptools.find_packages(),
        install_requires=[
            'sssdevlops',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',
                # autodoc
                # was
                # broken
                # in
                # 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
            ],
        },
        tests_require=[
            'pytest',
        ],
        zip_safe=True,
    )
