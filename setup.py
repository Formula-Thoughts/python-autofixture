from setuptools import setup, find_packages

DESCRIPTION = 'A Version of C#s AutoFixture but for python'
LONG_DESCRIPTION = 'Allows creating of fake test data that autogenerates both primitive and deep object graph types'

# Setting up
setup(
    name="python-autofixture",
    version="{{VERSION_PLACEHOLDER}}",
    author="GanTheMan",
    author_email="aidanwilliamgannon@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: Who Fucking Knows",
        "Intended Audience :: Anyone who can be bothered to install it",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix"
    ]
)