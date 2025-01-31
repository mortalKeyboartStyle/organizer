"""
rate_limiter_handler.py
Keyword: fuzzscrap_rate_limiter

Ograniczenie prędkości scrapowania/fuzzingu, by nie przeciążać serwerów.
Prosty token bucket.
"""

import time

class RateLimiter:
    def __init__(self, requests_per_second=1):
        self.interval = 1 / requests_per_second
        self.last_time = time.time()

    def acquire(self):
        """
        Czeka, aż minie odpowiedni czas od poprzedniego acquire.
        """
        now = time.time()
        diff = self.interval - (now - self.last_time)
        if diff > 0:
            time.sleep(diff)
        self.last_time = time.time()
