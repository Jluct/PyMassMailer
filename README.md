# PyMassMailer

**Package for send email**

Package for send emails. 

P.S. This is main first Python package :)

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

## In project

* Add mail template (https://wiki.python.org/moin/Templating)
* Add connect with DB (MySQL, SQLite) for read address
* Add documentation
* Create build *\*.tar.gz*
