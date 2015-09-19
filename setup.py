from setuptools import setup, find_packages

import solo


setup(
    name='django-solo-grappelli',
    keywords=['django', 'solo', 'singleton', 'grappelli'],
    version=solo.__version__,
    description=solo.__doc__,
    packages=find_packages(),
    url='http://github.com/gbezyuk/django-solo-grappelli',
    author='Grigoriy Bezyuk',
    author_email='me@gbezyuk.ru',
    long_description=open('README.md').read(),
    include_package_data=True,
    license='Creative Commons Attribution 3.0 Unported',
    download_url='https://github.com/gbezyuk/django-solo-grappelli/tarball/1.1.1'
)
