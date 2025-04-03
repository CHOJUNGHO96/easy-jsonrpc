from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easy-jsonrpc",
    version="0.1.3",
    author="ChoJungHo",
    author_email="jo4186@naver.com",
    description="Easy JSON-RPC library for Python and Go interoperability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CHOJUNGHO96/easy-jsonrpc.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=[
        "jsonrpclib-pelix>=0.4.0",  # Python 3.5+ 호환성
    ],
    keywords="jsonrpc, rpc, api, golang, interoperability",
)
