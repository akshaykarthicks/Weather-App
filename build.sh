#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Print current directory and list files
echo "Current directory: $(pwd)"
ls -la

# Install dependencies
pip install -r requirements.txt

# Debug: List files after installation
echo "Files after pip install:"
ls -la

# Check if weathers directory exists
if [ -d "weathers" ]; then
  echo "Found weathers directory"
  cd weathers
  echo "Inside weathers directory: $(pwd)"
  ls -la
  
  # Run Django commands
  if [ -f "manage.py" ]; then
    echo "Found manage.py"
    python manage.py collectstatic --no-input
    python manage.py migrate
  else
    echo "ERROR: manage.py not found in $(pwd)"
    # Try to find manage.py elsewhere
    echo "Searching for manage.py:"
    find / -name manage.py -type f 2>/dev/null | head -n 10
    exit 1
  fi
else
  echo "ERROR: weathers directory not found in $(pwd)"
  # List all directories in current path
  echo "Available directories:"
  ls -la
  exit 1
fi
