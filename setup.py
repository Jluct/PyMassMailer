from setuptools import setup, find_packages

setup(
    name='PyMassMailer',
    version='0.1',
    description='Package for send email',
    long_description='Package for send email. See README.md. This is main first Python package',
    classifiers=[
        'Development Status :: 3 - Alpha', 'License :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='mail, sender',
    url='https://github.com/Jluct/PyMassMailer',
    author='Flying Circus',
    author_email='panaev02@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['templating==0.5', 'ConfigParser==3.5'],
    include_package_data=True,
    zip_safe=False
)
