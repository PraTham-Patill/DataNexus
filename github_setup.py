#!/usr/bin/env python3
"""
DataNexus GitHub Repository Setup
Creates GitHub repository and pushes code
"""

import os
import subprocess
import sys

def run_command(command, description=""):
    """Execute shell command and handle errors"""
    print(f"🔄 {description}")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success: {description}")
            if result.stdout.strip():
                print(f"Output: {result.stdout.strip()}")
            return True, result.stdout
        else:
            print(f"❌ Failed: {description}")
            if result.stderr.strip():
                print(f"Error: {result.stderr.strip()}")
            return False, result.stderr
    except Exception as e:
        print(f"❌ Exception in {description}: {str(e)}")
        return False, str(e)

def setup_github_repo():
    """Setup GitHub repository and push code"""
    
    print("🚀 DataNexus GitHub Repository Setup")
    print("=" * 50)
    
    # Check if GitHub CLI is available
    gh_available, _ = run_command("gh --version", "Check GitHub CLI availability")
    
    if gh_available:
        print("\n📦 Creating GitHub repository with GitHub CLI...")
        
        # Create repository
        success, output = run_command(
            'gh repo create datanexus-production --public --description "DataNexus Django Production Deployment"',
            "Create GitHub repository"
        )
        
        if success:
            # Set remote
            run_command("git remote remove origin", "Remove existing remote (if any)")
            run_command(
                "git remote add origin https://github.com/PraTham-Patill/datanexus-production.git",
                "Add GitHub remote"
            )
            
            # Push to GitHub
            success, _ = run_command("git push -u origin main", "Push code to GitHub")
            
            if success:
                print("\n🎉 GitHub repository created and code pushed successfully!")
                print("Repository: https://github.com/PraTham-Patill/datanexus-production")
                return True
            else:
                print("\n❌ Failed to push code to GitHub")
                return False
        else:
            print("\n❌ Failed to create GitHub repository")
            return False
    else:
        print("\n📋 Manual GitHub Setup Required:")
        print("1. Go to https://github.com/new")
        print("2. Repository name: datanexus-production")
        print("3. Set to PUBLIC")
        print("4. Don't initialize with README")
        print("5. Click 'Create repository'")
        print("\nThen run these commands:")
        print("git remote add origin https://github.com/PraTham-Patill/datanexus-production.git")
        print("git push -u origin main")
        return False

def main():
    """Main function"""
    try:
        success = setup_github_repo()
        
        if success:
            print("\n🎯 Next Steps:")
            print("1. Go to https://railway.app")
            print("2. Click 'Start a New Project'")
            print("3. Choose 'Deploy from GitHub repo'")
            print("4. Select 'datanexus-production' repository")
            print("5. Add PostgreSQL database")
            print("6. Set environment variables")
            print("7. Wait for deployment to complete")
        else:
            print("\n📝 Please complete GitHub setup manually, then proceed with Railway deployment.")
            
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()