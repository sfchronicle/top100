# 2016 Top 100 Restaurants
Description TK

## Requirements
- Python 2.7.x
- Node.js 0.12
  - uglifyjs (`npm install -g uglifyjs`)
  - clean-css (`npm install -g clean-css`)
  - Bower and Grunt (`$ npm install -g grunt-cli bower`)

## Installation
First time with the project? Here's how you set everything up:
```bash
$ git clone git@github.com:sfchronicle/top100.git
$ cd top100
$ mkvirtualenv top100
$ pip install -r requirements.txt && npm install && bower install
```

## Activate
Already have the project installed? Here's how you re-activate for development:
```bash
$ cd top100  # change into the directory
$ workon top100  # activate virtual environment
$ git pull  # pull down latests
$ bower install # install new frontend dependencies
$ grunt serve # start server
```

### Start app
```bash
$ grunt serve
```

## Explore ORM
Interact with the SQLite database by running the shell.py file:
```bash
$ ./shell.py
```

## Build and deployment
Create a `local_settings.py` file in the `settings` directory. Add the following env variables:
```python
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
```

Now run `build.py` and specify if its for `production` or `staging` to compress assets for upload.
```bash
$ python build.py production
```

## Troubleshooting
If you run into a problem when installing bower at the SF Chronicle office, its due to a firewall issue. Run the following to install bower through SSL and then install bower again:
```bash
$ git config --global url."https://".insteadOf git://
```