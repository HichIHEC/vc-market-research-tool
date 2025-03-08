import json
import os
import pickle
import time

class Cache:
    def __init__(self, cache_dir='cache'):
        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def _get_cache_file_path(self, key):
        return os.path.join(self.cache_dir, f"{key}.pkl")

    def get(self, key):
        cache_file_path = self._get_cache_file_path(key)
        if os.path.exists(cache_file_path):
            with open(cache_file_path, 'rb') as f:
                return pickle.load(f)
        return None

    def set(self, key, value):
        cache_file_path = self._get_cache_file_path(key)
        with open(cache_file_path, 'wb') as f:
            pickle.dump(value, f)

    def clear(self):
        for filename in os.listdir(self.cache_dir):
            file_path = os.path.join(self.cache_dir, filename)
            os.remove(file_path)

    def cache_response(self, key, response, expiration_time=3600):
        self.set(key, {'response': response, 'timestamp': time.time()})
        self.expiration_time = expiration_time

    def get_cached_response(self, key):
        cached_data = self.get(key)
        if cached_data:
            if time.time() - cached_data['timestamp'] < self.expiration_time:
                return cached_data['response']
            else:
                self.clear()  # Clear expired cache
        return None