import time
from datetime import datetime, timedelta

from flask import url_for

import pytest

from app import app, db
from app.helpers import less_than_day, pretty_date

def test_lessthanday():
  assert less_than_day(32) == "32 seconds ago"
  assert less_than_day(100) == "a minute ago"
  assert less_than_day(2645) == "44 minutes ago"
  assert less_than_day(5200) == "an hour ago"
  assert less_than_day(68500) == "19 hours ago"
  assert less_than_day(86401) == None
  


