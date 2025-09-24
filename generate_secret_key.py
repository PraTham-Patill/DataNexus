#!/usr/bin/env python
"""
Generate a secure Django secret key for production
"""

import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure secret key for Django"""
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Generated Django Secret Key:")
    print("=" * 60)
    print(secret_key)
    print("=" * 60)
    print("\nCopy this key and set it as your SECRET_KEY environment variable in production.")
    print("Keep this key secure and never commit it to version control!")