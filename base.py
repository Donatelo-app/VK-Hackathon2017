import redis 
import json
import os

class Base:
    def __init__(self):
        self.redis = redis.from_url(os.environ.get("REDIS_URL","redis://localhost:6379"))


    def set(self, key, value, **kwargs):
        value = json.dumps(value)
        key = "deforest:%s"%key
        self.redis.set(key, value, **kwargs)



    def get(self, field, default=None):
        key = "deforest:%s"%field
        value = self.redis.get(key)
        if type(value) is bytes: value = value.decode('utf-8')
            
        
        if value is None: value = default
        else: value = json.loads(value)
        
        return value