import json
from encryption_utils import encrypt_data, decrypt_data
from activity_logger import log_activity
from permissions import check_permission

class SietalAgent:
    def __init__(self, user_id, encryption_key):
        self.user_id = user_id
        self.encryption_key = encryption_key
        self.data_store = {}

    def submit_data(self, data_type, data):
        if check_permission(self.user_id, data_type):
            encrypted = encrypt_data(data, self.encryption_key)
            self.data_store[data_type] = encrypted
            log_activity(self.user_id, f"Submitted data of type {data_type}")
        else:
            raise PermissionError("User not permitted to submit this type of data")

    def retrieve_data(self, data_type):
        if data_type in self.data_store:
            decrypted = decrypt_data(self.data_store[data_type], self.encryption_key)
            log_activity(self.user_id, f"Retrieved data of type {data_type}")
            return decrypted
        else:
            return None