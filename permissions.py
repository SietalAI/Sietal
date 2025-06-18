PERMISSIONS = {
    "user123": ["preferences", "browsing_data"],
    "user456": ["analytics", "usage"]
}

def check_permission(user_id, data_type):
    return data_type in PERMISSIONS.get(user_id, [])