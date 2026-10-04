import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qzone_api",
    version="1.1.1",
    author="Huan Xin",
    author_email="mc.xiaolang@foxmail.com",
    description="QQ空间API封装",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HuanXinToolkit/qq_zone_api",
    project_urls={
        "Homepage": "https://github.com/HuanXinToolkit/qq_zone_api",
        "Issues": "https://github.com/HuanXinToolkit/qq_zone_api/issues",
        "Changelog": "https://github.com/HuanXinToolkit/qq_zone_api/blob/main/changes.md",
    },
    packages=setuptools.find_packages(),
    install_requires=['aiohttp>=3.12.0','lxml>=5.3.0','loguru>=0.7.3','requests>=2.32.4','pyzbar>=0.1.9','Pillow>=10.2.0','qrcode>=7.4.2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)