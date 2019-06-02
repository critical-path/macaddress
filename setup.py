from setuptools import (
    find_packages,
    setup
)


setup(
    name="macaddress",
    version="0.8.0",
    description="The macaddress library makes it easy to work with media access control (MAC) addresses.",
    url="https://github.com/critical-path/macaddress",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords="python media-access-control mac mac-address networking",
    packages=find_packages(),
    extras_require={
        "test": [
            "coveralls",
            "flake8",
            "pytest>=3.6",
            "pytest-cov"
        ]
    }
)
