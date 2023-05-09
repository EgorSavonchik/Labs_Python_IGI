from setuptools import setup, find_packages


setup(
    name="SavonchikSerializer",
    version="1.0",
    description="module for python serialization(JSON, XML)",
    url="https://github.com/EgorSavonchik/Labs_Python_IGI/tree/Lab3",
    author="Egor Savonchik",
    author_email="egorsavonchik1@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["Serializers"],
    include_package_data=True
)