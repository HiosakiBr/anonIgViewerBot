# anon ig viewer

"Anon ig viewer" is a bot for you see stories of instagram of peoples (except private profiles) in a way totally anonymous! 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all necessary libraries .

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Documentation

### Configuration variables
for to use you need make a bot in the telegram by [BotFather](https://t.me/BotFather), after create your bot, set in the file "config.py" the information necessary for the code to work normally.

### Create session cookie of intagram

I left the *cookies.py* file commented out explaining what
 you should do, when running the code with ```python cookie.py```
, the program will ask you to enter your instagram account login information to generate the session cookie. the cookie is important because instagram does not give you access to stories if you are not logged in.

### Use on local machine

to do this you must change in the file *instagram.py* on line 39 how the browser should be started, then change this:

```python
39: driver = Browser.deploy()
```
for that:


```python
39: driver = Browser.local()
```

## Roadmap

some changes I want to make are taking the user's profile picture, downloading photo and video from the posts feed and even figuring out a way to run without the need for the session cookie. If you have an idea, don't hesitate to open a pull request, I'll be happy to see you helping the project!

## License
[MIT](https://github.com/HiosakiBr/anonIgViewerBot/blob/main/LICENSE)
