from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pysecuritytrails',
    version='0.1.3',
    description='Python wrapper around the Security Trails API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Te-k/pysecuritytrails',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='security',
    install_requires=['requests', 'configparser'],
    license='GPLv3',
    python_requires='>=3.5',
    packages=['pysecuritytrails'],
    entry_points= {
        'console_scripts': [ 'securitytrails=pysecuritytrails.cli:main' ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]

)
