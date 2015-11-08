# Built With Electron [![Build Status](https://magnum.travis-ci.com/ekonstantinidis/builtwithelectron.svg?token=9QR4ewbqbkEmHps6q5sq&branch=hello-npm)](https://magnum.travis-ci.com/ekonstantinidis/builtwithelectron)
Where awesome electron apps meet

### Prerequisites

 - Postgres Database: `bwedb`
 - Python 3 (`brew install python3`)
 - Django
 - Django Rest Framework
 - React


### Setup (Development)

There is a build script, that will do all the work for you. Just run:

    scripts/build dev


### Development

First run the django server and then use npm to build and watch for changes.

    scripts/runserver dev
    npm start


### Tests

    scripts/runtests
