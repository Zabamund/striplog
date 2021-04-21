from striplog import Interval
from striplog import Lexicon

lexicon = Lexicon.default()

text = "wet silty fine sand with tr clay" 

interval = Interval._parse_description(text, lexicon=lexicon, max_component=3, abbreviations=True)

print(interval)
