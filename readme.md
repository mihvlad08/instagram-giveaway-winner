# Instagram-Giveaway-Winner

Instagram-Giveaway-Winner is a Python library for automating the processes of joining (and winning!) giveaways hosted on Instagram. Built with Selenium.

## Installation

To start, clone the repo and then use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium
```bash
git clone https://github.com/mihvlad08/instagram-giveaway-winner
cd ./instagram-giveaway-winner
python3 -m pip install selenium
```
Then, create a new file in project root, credentials.py where you have to add
2 variables, username and password.
```python
username = 'your username here'
password = 'your password here'
```
In main.py, set the giveaway post URL and whether or not your account uses
two-factor authentication (Not using 2FA simplifies the login process)
```python
url = 'giveaway url goes here'
twoFA = True/False
```

Finally, run the script with the generic Python command
```bash
python3 main.py
```


