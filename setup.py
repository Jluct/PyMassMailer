from setuptools import setup, find_packages
import PyMassMailer

setup(
    name='PyMassMailer',
    version=PyMassMailer.__version__,
    description='Package for send email',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='mail, sender, smtp',
    url='https://github.com/Jluct/PyMassMailer',
    author='Listopadov Serj',
    author_email='panaev02@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Jinja2==2.10',
        'ConfigParser==3.5',
        'smtplib==3.3'
    ],
    include_package_data=True,
    zip_safe=False
)
