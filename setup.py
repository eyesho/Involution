from setuptools import setup

setup(
    name="involution",
    version="0.2",
    url="https://github.com/eyesho/Involution",
    license="MIT License",
    author="Christoph Reich",
    author_email="ChristophReich@gmx.net",
    description="PyTorch 2d Involution",
    packages=["involution",],
    install_requires=["torch>=1.7.0"],
)
