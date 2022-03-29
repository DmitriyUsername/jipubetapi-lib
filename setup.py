from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    'aiohttp==3.8.1',
    'aiosignal==1.2.0',
    'async-timeout==4.0.2',
    'asyncio==3.4.3',
    'attrs==21.4.0',
    'charset-normalizer==2.0.12',
    'frozenlist==1.3.0',
    'idna==3.3',
    'multidict==6.0.2',
    'typing==3.7.4.3',
    'yarl==1.7.2'
]

setup(
    name="jipubetapi",
    version="0.0.5",
    author="Dmitrii Kazanin",
    author_email="dmitriikazanin@gmail.com",
    description="This library makes it easier to access the API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/DmitriyUsername/jipubetapi-lib",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)