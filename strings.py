import re
from string import punctuation

# removing urls
text = re.sub('https?\S+', 'URL', text)

# removing numbers
text = re.sub('[0-9]+','', text)

# removing punctuation
text = re.sub('[%s]*' % punctuation, '',text)
