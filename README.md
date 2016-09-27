# Built With Electron [![Build Status](https://travis-ci.org/manosim/builtwithelectron.svg?branch=master)](https://travis-ci.org/manosim/builtwithelectron)
[www.builtwithelectron.com](http://www.builtwithelectron.com/): Where awesome - made with electron - apps meet.

### Prerequisites

 - Postgres Database: `bwedb`
 - Python 3 (`brew install python3`)
 - Django
 - Django Rest Framework
 - React


### Setup (Development)

There is a build script, that will do all the work for you. Just run:

    scripts/build


### Development commands
There are several helper methods to run the project locally:

    # Build the project
    ./scripts/build

    # Run migrate
    ./scripts/migrate

    # Run the server
    ./scripts/runserver

    # Bring the Django shell
    ./scripts/shell

    # Run other commands using the environment - ./scripts/run echo "Hello Oleous!"
    ./scripts/run


### Tests

    scripts/runtests
