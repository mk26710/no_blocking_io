from setuptools import setup

setup(
    name="no_blocking_io",
    descruoption="Simple package with just one decorator that wraps your blocking functions with asyncio.to_thread",
    url="https://github.com/howaitoreivun/no_blocking_io",
    license="MIT",
    author="howaitoreivun",
    keywords="asyncio blocking",
    packages=["no_blocking_io"],
    python_requires=">=3.9.0",
    version="0.0.1",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
