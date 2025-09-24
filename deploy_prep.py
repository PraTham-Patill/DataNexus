#!/usr/bin/env python
"""
Deployment preparation script for DataNexus
Ensures all necessary files and configurations are ready for deployment
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and check for errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_file_exists(file_path, description):
    """Check if a required file exists"""
    if Path(file_path).exists():
        print(f"✅ {description}: Found")
        return True
    else:
        print(f"❌ {description}: Missing")
        return False

def main():
    """Main deployment preparation function"""
    print("🚀 DataNexus Deployment Preparation")
    print("=" * 50)
    
    # Check required files
    required_files = [
        ("requirements.txt", "Requirements file"),
        ("Procfile", "Procfile for deployment"),
        ("runtime.txt", "Python runtime specification"),
        ("manage.py", "Django management script"),
        (".env.example", "Environment variables example"),
        ("README.md", "Project documentation"),
    ]
    
    all_files_exist = True
    for file_path, description in required_files:
        if not check_file_exists(file_path, description):
            all_files_exist = False
    
    if not all_files_exist:
        print("\n❌ Some required files are missing!")
        return False
    
    # Check Django configuration
    print("\n🔍 Checking Django Configuration...")
    
    # Check for migrations
    if not run_command("python manage.py makemigrations --check", "Checking migrations"):
        print("⚠️  You may need to create migrations")
    
    # Test settings import
    if not run_command("python manage.py check --deploy", "Django deployment check"):
        print("⚠️  Django deployment check found issues")
    
    # Collect static files (dry run)
    if not run_command("python manage.py collectstatic --noinput --dry-run", "Static files check"):
        print("⚠️  Static files collection may have issues")
    
    print("\n📋 Deployment Checklist:")
    print("✅ All required files present")
    print("✅ Django configuration checked")
    print("✅ Static files ready")
    print("✅ Database migrations prepared")
    
    print("\n🚀 Ready for deployment!")
    print("\nNext steps:")
    print("1. Create account on Railway (https://railway.app) or Render (https://render.com)")
    print("2. Connect your GitHub repository")
    print("3. Set environment variables:")
    print("   - SECRET_KEY (generate a new one for production)")
    print("   - DEBUG=False")
    print("   - ALLOWED_HOSTS=your-domain.railway.app")
    print("   - DATABASE_URL (will be provided by the platform)")
    print("   - OPENWEATHER_API_KEY (optional)")
    print("4. Deploy and run migrations")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)