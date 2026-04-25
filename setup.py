import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "Beverage-Quality-Assessment"
AUTHOR_USER_NAME = "Sabbir Azim"
SRC_REPO = "Beverage"
AUTHOR_EMAIL = "fazley.azim.sabbir@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A project to assess the quality of beverages using machine learning techniques.",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)