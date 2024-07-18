#!/bin/bash

# Check for an environment variable
if [ "$SKIP_MY_HOOK" == "true" ]; then
    echo "Skipping hook due to SKIP_MY_HOOK being set to true."
    exit 0
fi

# Run the actual hook command
exec  python repo_agent//runner.py