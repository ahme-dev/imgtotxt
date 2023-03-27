from distutils.core import setup

setup(
    name="ImgToTxt",
    version="0.1.0",
    author="Ahmed K. A.",
    author_email="ahmadkabdullah@proton.me",
    packages=["imgtotxt"],
    include_package_data=True,
    url="https://github.com/ahmddots/imgtotxt",
    description="Native local OCR app",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=["easyocr", "toga"],
)
