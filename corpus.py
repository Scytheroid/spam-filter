import os

class Corpus:
    '''FACILITATES WORK WITH FILES.'''
    def __init__(self, path_to_mails):
        self.path_to_mails = path_to_mails
        
    def emails(self):
        '''RETURNS FILE'S NAME AND CONTENT.'''
        for entry in os.scandir(self.path_to_mails):
            if entry.is_file() and not entry.name.startswith('!'):
                path = self.path_to_mails + '/' + entry.name
                with open(path, mode='r', encoding='utf-8') as mail:
                    yield entry.name, mail.read()