from setuptools import setup, find_packages

setup(
    name="async-requests",
    version="0.1.0",
    description="Lightweight asynchronous GET/POST HTTP helper built on httpx.",
    author="Anton Didenko",
    author_email="didenko85.2014@gmail.com",
    packages=find_packages(where="async_requests"),
    package_dir={"": "async_requests"},
    install_requires=["httpx>=0.28.0"],
    python_requires=">=3.10",
    license="MIT",
)
