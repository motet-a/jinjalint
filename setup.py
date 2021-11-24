from setuptools import setup
from pathlib import Path
import versioneer


_CURRENT_DIRECTORY: str = Path(__file__).parent

with (_CURRENT_DIRECTORY / "README.md").open("r") as f:
    long_description: str = "\n" + f.read()


setup(
    name="jinjalint",
    author="JDSC, Co., Ltd.",
    url="https://github.com/jdsc/jinjalint",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A linter for Jinja-like templates",
    long_description=long_description,
    packages=["jinjalint"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        "console_scripts": ["jinjalint=jinjalint.cli:main"],
    },
)
