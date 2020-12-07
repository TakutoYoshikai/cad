from setuptools import setup, find_packages

setup(
    name = 'cad',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/cad.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "image format changer",
    install_requires = ['setuptools'],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "cad = cad.cad:main",
        ]
    }
)
