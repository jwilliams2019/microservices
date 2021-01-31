from datetime import datetime, timedelta
import time
import pytest
from app import app
from app.helpers import less_than_day, pretty_date

def test_LessThanDay():
  assert less_than_day(32) == "32 seconds ago"
  assert less_than_day(100) == "a minute ago"
  assert less_than_day(2645) == "44 minutes ago"
  assert less_than_day(5200) == "an hour ago"
  assert less_than_day(68500) == "19 hours ago"
  assert less_than_day(86401) == None

def test_PrettyDate():
  assert pretty_date() == "just now"
  assert pretty_date(int(time.time()) - 86400) == "Yesterday"
  assert pretty_date(int(time.time()) - 43 + 8*3600) == "43 seconds ago" 
  now = datetime.utcnow() - timedelta(hours=8)
  assert pretty_date(now - timedelta(days = 1)) == "Yesterday"
  assert pretty_date(now + timedelta(days = 1)) == "just about now"
  assert pretty_date(now - timedelta(days = 4)) == "4 days ago"
  assert pretty_date(now - timedelta(weeks = 3, days = 1)) == "3 weeks ago"
  assert pretty_date(now - timedelta(days = 8*31)) == "8 months ago"
  assert pretty_date(now - timedelta(days = 10*366)) == "10 years ago"

