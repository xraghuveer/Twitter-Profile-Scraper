import snscrape.modules.twitter as sns


def miniStr(o):
  return ' '.join(i for i in str(o).split() if i)


profileID = input("Enter username without '@':  ")
keysList = [
  'displayname', 'rawDescription', 'descriptionLinks', 'verified', 'created',
  'followersCount', 'friendsCount', 'statusesCount', 'favouritesCount',
  'listedCount', 'mediaCount', 'location', 'protected', 'link.tcourl',
  'profileImageUrl', 'profileBannerUrl'
]

tusRes, defVal = sns.TwitterUserScraper(profileID).entity, 'no such attribute'
print('\nfor ID', profileID, '\n')
for k in keysList:
  print('\t', k, ':', miniStr(getattr(tusRes, k, defVal)))
