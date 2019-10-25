# Alpaca Setup Tutorial

[Return to main page](index.md)

This tutorial is designed to help you start paper trading with Alpaca. I’ll assume that you’re on a Windows machine. If you’re using MacOS/Linux, this process should be more streamlined for you, and I’ll bet you can fill in any of the gaps here.

Don’t be alarmed by the number of steps. I made this tutorial pretty granular so it’s easy to follow. I’ll definitely try to revisit this to clear up any misleading steps or errors. Please let me know of any improvements I could make. Alternatively, feel free to make your own edits as long as they are accurate and appropriate.

**Step 1:** Create a paper trading account on Alpaca’s [website](https://app.alpaca.markets/signup).

**Step 2:** Install the latest version of [pip](https://pip.pypa.io/en/stable/installing/) (if you’re using Python 3.xx, as you should be by now, then you should have pip installed already). Try `py -m pip install --upgrade pip` to ensure that you’re using the latest version. If you get a funny error, try this and any following command with `pip3` instead.

*Note:* Path issues are common when dealing with initial installations. If you’re currently using Anaconda or PyCharm, you should be able to solve your issue after searching Stack Overflow. If not, let me know, and I’ll try my best to help. Here’s an easy way to check your environment variables: Windows Button > type “path” > select “Edit the system environment variables” > “Environment Variables” 

**Step 3:** We want to work in a closed workspace that will house all of our code. You can read more about the philosophy [here](https://docs.python.org/3/library/venv.html) if you like. We need to set up a virtual environment that will act as our own Python microcosm. The preferred tool, `venv`, should be included with your Python 3.xx distribution. Try `py -m venv -h` as a check.

**Step 4:** We want to create a new project directory. This is where our virtual environment will live, and so this is ultimately where all our code will live. Make sure that you build your project directory in a convenient place like your home directory. After you’ve selected a parent directory, run the command `mkdir name && cd name`. Then create a virtual environment: `py -m venv name`.

**Step 5:** We can activate or enter the virtual environment with the following command: `cd name\Scripts && activate`. Now you may pip install any and all packages you want to use. Creating an isolated workspace where we can freely install different Python modules is the beauty of venv. If you get stuck, be sure to read more [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

**Step 6:** In your activated virtual environment, run `pip install alpaca-trade-api` to install the Alpaca trading API. This is how we’ll communicate with Alpaca to feed in data and execute our orders. I also recommend using Jupyter notebooks to organize your work: `pip install jupyter`. Run `jupyter notebook` in your venv, and you should be redirected to a browser GUI where you may create a new Python 3 notebook.

**Step 7:** I’ll add more later, but this should be a solid enough start for you to start playing with Alpaca's API, and you have more support from [here](https://github.com/alpacahq/alpaca-trade-api-python) on their github page. You should now be prepared to [give their examples a shot](https://github.com/alpacahq/alpaca-trade-api-python/tree/master/examples).