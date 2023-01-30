import os
from environs import Env


class Settings:

    def __init__(self):
        env = Env()
        env.read_env()
        self.EVERNOTE_CONSUMER_KEY = env('EVERNOTE_CONSUMER_KEY')
        self.EVERNOTE_CONSUMER_SECRET = env('EVERNOTE_CONSUMER_SECRET')
        self.EVERNOTE_PERSONAL_TOKEN = env('EVERNOTE_PERSONAL_TOKEN')
        self.JOURNAL_TEMPLATE_NOTE_GUID = env('JOURNAL_TEMPLATE_NOTE_GUID')
        self.JOURNAL_NOTEBOOK_GUID = env('JOURNAL_NOTEBOOK_GUID')
        self.INBOX_NOTEBOOK_GUID = env('INBOX_NOTEBOOK_GUID')
