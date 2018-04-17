from setuptools import setup

setup(
    name='pysectrails',
    version='0.1.1',
    description='Python wrapper around the Security Trails API',
    url='https://github.com/Te-k/pysectrails',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='security',
    install_requires=['requests'],
    license='GPLv3',
    python_requires='>=3.5',
    packages=['pysectrails'],
)
