#!/usr/bin/env python
from setuptools import find_packages, setup


project = "backend"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="Backend",
    author="Zilch",
    author_email="noreply@zilch.me",
    url="https://github.com/zilch-balmo/backend",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "microcosm>=2.6.0",
        "microcosm-flask>=1.22.0",
        "microcosm-logging>=1.5.0",
        "microcosm-postgres>=1.15.4",
        "microcosm-secretsmanager>=1.1.0",
        "pyOpenSSL>=19.0.0",
    ],
    entry_points={
        "console_scripts": [
            "createall = backend.main:createall",
            "migrate = backend.main:migrate",
            "runserver = backend.main:runserver",
        ],
    },
    extras_require=dict(
        deploy=[
            "gevent>=1.4.0",
            "gunicorn>=19.9.0",
        ],
        dist=[
            "bumpversion>=0.5.3",
            "pip>=19.0.3",
            "setuptools>=40.8.0",
            "twine>=1.13.0",
            "wheel>=0.33.1",
        ],
        lint=[
            "flake8>=3.7.7",
            "flake8-isort>=2.7.0",
            "flake8-print>=3.1.0",
        ],
        test=[
            "coverage>=4.5.3",
            "nose>=1.3.7",
            "PyHamcrest>=1.9.0",
        ],
        typehinting=[
            "mypy>=0.670.0",
        ],
    ),
)
