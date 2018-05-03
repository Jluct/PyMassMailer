# PyMassMailer

**Package for send email**

Package for send emails. 

P.S. This is main first Python package :)

## Install

run

`
    python3 setup.py
`

## Using

For send one mail

`
 sender.send_one(example@email.com, 'test')
`

For mass mailing

Create *.json file and add path and type in **conf.ini**.Example:

`
    ["test@email.com","test1@email.com"]
`
and run
`
    sender.set_address(address).send_all('test')
`

###For using template

create *.html* file and add in code
`
    sender
    .set_address(address)
    .send_all(
        open(
            path.normpath('templates/test.html'),
            'r'
        )
        .read(),
        {'param': 'value', ...}
    )
`

In project use [Jinja2](http://jinja.pocoo.org/) (2.10)

## In project

* Add connect with DB (MySQL, SQLite) for read address
* Add documentation
* Create build *\*.tar.gz*
