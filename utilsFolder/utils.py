import random
from utilsFolder.info_template import defaultIntro, askIntro, fancyIntro, slayIntro

def getRandomIntroTemplate():
    return random.choice([defaultIntro, askIntro, fancyIntro, slayIntro])