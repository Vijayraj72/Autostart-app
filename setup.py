from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Autostart_app",
    version="1.0.0.3",
    description="A Python package to autostart your desktop application when your system turn-on",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Vijayraj72/Autostart-app",
    author="vijay saw",
    author_email="imvijayraj72@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Autostart_app"],
    include_package_data=True,
    install_requires=[""],
    entry_points={
            "console_scripts": [
                'Autostart-app=Autostart_app.autostart_create:main',
            ]
        }
)
