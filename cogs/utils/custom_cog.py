from discord.ext.commands import Cog as OriginalCog

from cogs.utils.custom_bot import CustomBot


class Cog(OriginalCog):

    def __init__(self, bot:CustomBot, cog_name:str=None):
        self.bot = bot
        if cog_name:
            self.log_handler = bot.logger.getChild(cog_name)
        else:
            self.log_handler = bot.logger.getChild(self.get_class_name())


    def get_class_name(self, *prefixes, sep:str='.'):
        '''Gets the name of the class with any given prefixes, with sep as a seperator'''
        return sep.join(list(prefixes) + [self.__class__.__name__])
