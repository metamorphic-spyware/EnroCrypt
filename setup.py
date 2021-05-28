from setuptools import setup,find_packages
file = open('README.md','r').read()
setup(
    name="enrocrypt",
    version="1.0.2",
    author="Morgan-Phoenix",
    author_email="mikebrain61@gmail.com",
    description="This is a Python Module For Encryption, Hashing And Other stuff",
    long_description=file,
    long_description_content_type="text/markdown",
    url="https://github.com/Morgan-Phoenix/EnroCrypt",
    project_urls={
        "Bug Tracker": "https://github.com/Morgan-Phoenix/EnroCrypt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
)