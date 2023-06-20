# UnifiedFediverseObserver
A fediverse client designed to give you access to raw federation.

Stuff coming soon, highly experimental.


## Installation
&TLDR; `git clone https://github.com/JustusW/UnifiedFediverseObserver.git`, make a virtual env using `python -m venv ./venv`, then `pip install flask pywebview requests` and then use `python app.py`

### Windows
In order to install this application first download or checkout this repository to your computer. If you are running on windows you will have to install python. You can find further information on this topic on https://www.python.org/downloads/windows/
You may also want to install git in order to be able to access this repository directly, you can do so here: https://git-scm.com/download/win

### Linux
Depending on your distribution you should be familiar with this process, you will need python 3, preferably 3.11 as that is what I'm using to develop this package. Everything else can and should be installed via pip in the virtual environment we're gonna create.

### Actually installing the thing
First off we will open a console of our choice (Windows users probably want to use PowerShell) and in there we navigate to a directory we want to use for this project.

```shell
cd C:/Users/<Your-Username>/Documents/
```
Note: If your username contains a space you will have to put the entire thing after `cd` in airquotes!

We can now create a new folder for our purpose like this:
```shell
mkdir UFO
cd UFO
```

Now we can use git to download the repository:
```shell
git clone https://github.com/JustusW/UnifiedFediverseObserver.git
cd UnifiedFediverseObserver```

If you come back to this project after some time you may wish to use the `pull` command to download any changes I made to this project in the meantime.
```shell
git pull
```

Congratulations, you have now downloaded all of the things you will need to proceed to installation. If you followed these steps you can now create a virtual environment for the project:
```shell
python -m venv ./venv
```

To use it you will also need to activate it, this is may happen automatically upon initial installation but for future use you will have to do this:
```shell
cd C:/Users/<Your-Username>/Documents/UFO/UnifiedFediverseObserver
./venv/Scripts/activate
```
You can see that you were successfull when your console is now prefixed with `(venv)`.

In order to use this application you will have to install some packages manually, as automation takes time this will sadly be added much later to this client. We do this using pip, pythons package manager.
```
pip install pywebview flask requests
```

After that you should be able to simply do this:
```
python app.py
```

This should open the application and you can now proceed with your experimentation! Happy Hacking!
If you have any trouble you can poke me on @JustusWingert@mastodon.social
