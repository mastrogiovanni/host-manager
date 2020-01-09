import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='host-manager',  
    version='0.1',
    scripts=['host-manager'] ,
    author="Michele Mastrogiovanni",
    author_email="michele.mastrogiovanni@gmail.com",
    description="Management CLI of /etc/hosts file to add and remove mappings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mastrogiovanni/host-manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)