# Built With Electron [![Build Status](https://magnum.travis-ci.com/ekonstantinidis/builtwithelectron.svg?token=9QR4ewbqbkEmHps6q5sq&branch=hello-npm)](https://magnum.travis-ci.com/ekonstantinidis/builtwithelectron)
Where awesome - made with electron - apps meet.

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
