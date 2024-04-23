import os
import pickle
from datetime import datetime

def log_message(log_file, message):
    with open(log_file, 'a') as log:
        log.write(f"{message} at {datetime.now()}\n")

def create_user(name, data, password, log_file='logs.txt'):
    user_file_path = f"{name}.pkl"
    log_message(log_file, f"Attempt to create user '{name}'")
    if os.path.exists(user_file_path):
        log_message(log_file, f"Attempt to create existing user '{name}'")
    else:
        user_data = {'name': name, 'data': data, 'password': password, 'last_changed': datetime.now()}
        with open(user_file_path, 'wb') as user_file:
            pickle.dump(user_data, user_file)
        log_message(log_file, f"User '{name}' created successfully")

def login(name, password, log_file='logs.txt'):
    user_file_path = f"{name}.pkl"
    log_message(log_file, f"Attempted login for user '{name}'")
    if os.path.exists(user_file_path):
        with open(user_file_path, 'rb') as user_file:
            user_data = pickle.load(user_file)
        if user_data['password'] == password:
            log_message(log_file, f"Login successful for user '{name}'")
            return user_data['data']
        else:
            log_message(log_file, f"Login failed for user '{name}'")
            return None
    else:
        log_message(log_file, f"Attempted login for non-existent user '{name}'")
        return None

def change_password(name, old_password, new_password, log_file='logs.txt'):
    user_file_path = f"{name}.pkl"
    log_message(log_file, f"Attempted password change for user '{name}'")
    if os.path.exists(user_file_path):
        with open(user_file_path, 'rb') as user_file:
            user_data = pickle.load(user_file)
        if user_data['password'] == old_password:
            user_data['password'] = new_password
            user_data['last_changed'] = datetime.now()
            with open(user_file_path, 'wb') as user_file:
                pickle.dump(user_data, user_file)
            log_message(log_file, f"Password changed successfully for user '{name}'")
        else:
            log_message(log_file, f"Failed password change for user '{name}'")
    else:
        log_message(log_file, f"Attempted password change for non-existent user '{name}'")
