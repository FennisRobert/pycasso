from setuptools import setup, find_packages

setup(
    name="pycasso",
    version="0.1.2",
    description="A description of your library",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # Add dependencies here
)
