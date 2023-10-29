from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'A package that allows game developers to integrate quantum circuit in their pygame-based quantum games.'

# Setting up
setup(
    name="Quantum Circuit Game Engine",
    version=VERSION,
    author="Ashmit JaiSarita Gupta",
    author_email="ashmitgupta.social@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pygame', 'qiskit-terra', 'numpy'],
    keywords=['quantum circuit game engine', 'quantum circuit pygame', 'quantum circuit',
                'qcge', 'quantum game', 'pygame'],
    classifiers=[
        "Development Status :: 2 - Releasing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
