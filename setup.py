from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pysectrails',
    version='0.1.2',
    description='Python wrapper around the Security Trails API',
    url='https://github.com/Te-k/pysectrails',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='security',
    install_requires=['requests', 'configparser'],
    license='GPLv3',
    python_requires='>=3.5',
    packages=['pysectrails'],
    entry_points= {
        'console_scripts': [ 'sectrails=pysectrails.cli:main' ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)
