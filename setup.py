from setuptools import setup, find_packages


setup(
    name='jinx',
    version='0.1',
    license='Apache Software License (ASF)',
    packages=find_packages(),
    install_requires=[
        'bsddb3==6.2.6',
        'Click==7.0',
        'Sanic==0.8.3',
    ],
    entry_points='''
        [console_scripts]
        jinx=jinx.cli:cli
    ''',
)
