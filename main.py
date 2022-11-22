import helper
url = 'https://www.instagram.com/p/ClF2kBcIyVY/'
twoFA = False  # or False if you don't have two-factor on

interface = helper.InstagramWinnerInterface(url, twoFA)

interface.login()
interface.go_to_giveaway_post()
interface.like_post()
interface.comment_on_post()
