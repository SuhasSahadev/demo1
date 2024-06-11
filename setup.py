from setuptools import setup, find_packages

setup(
    name="demo1",
    version="0.1.1",
    author=" suhas",
    author_email="suhassahadevan02@gmail.com",
    description="A short description of your project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SuhasSahadev/demo1.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
)
