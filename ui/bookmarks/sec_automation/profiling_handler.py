"""
profiling_handler.py
Keyword: sec_automation_profiling

Pomiar czasu wykonywania scrapingu, generowanie statystyk.
Można użyć cProfile / timeit. Tu - uproszczony stoper.
"""

import time

def profile_function(func, *args, **kwargs):
	"""
	Uruchamia func z podanymi argumentami, mierzy czas wykonania, zwraca (result, elapsed_time).
	"""
	start = time.time()
	result = func(*args, **kwargs)
	elapsed = time.time() - start
	return result, elapsed
