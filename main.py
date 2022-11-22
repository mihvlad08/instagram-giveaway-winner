import helper
url = 'https://realpython.com/python-class-constructor/'
twoFA = True  # or False if you don't have two-factor on

interface = helper.InstagramWinnerInterface(url, twoFA)
interface.login()
