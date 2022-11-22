import helper
url = 'https://www.instagram.com/p/ClF2kBcIyVY/'
twoFA = True  # or False if you don't have two-factor on

interface = helper.InstagramWinnerInterface(url, twoFA)
interface.login()
interface.goToGiveawayPost()
interface.likePost()
