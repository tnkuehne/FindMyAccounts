import os
from collections.abc import Set

from WhereDoIHaveAnAccount.scraper import scrape

TEST_EMAIl_USERNAME = os.environ['TEST_EMAIL_USERNAME']
TEST_EMAIL_PASSWORD = os.environ['TEST_EMAIL_PASSWORD']
TEST_EMAIL_IMAP_SERVER = os.environ['TEST_EMAIL_IMAP_SERVER']


def test_scrape():
    domains = scrape(TEST_EMAIl_USERNAME, TEST_EMAIL_PASSWORD, TEST_EMAIL_IMAP_SERVER)
    assert isinstance(domains, Set)
    assert len(domains) is not 0
