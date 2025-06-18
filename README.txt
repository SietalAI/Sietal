Sietal Agent

This module handles encrypted user data submission, retrieval, and permission management
for the Sietal decentralized data platform. It includes:

- agent.py: Main class that processes and stores data securely.
- encryption_utils.py: Uses Fernet encryption to protect sensitive data.
- activity_logger.py: Records each action a user performs for transparency.
- permissions.py: Controls access to data types per user.

Usage:
- Create a SietalAgent instance with a user ID and encryption key.
- Use submit_data() and retrieve_data() to interact with secure storage.

Dependencies:
- cryptography