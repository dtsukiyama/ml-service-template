#!/bin/bash

# Check for Homebrew and install it if missing
if ! command -v brew >/dev/null 2>&1; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check if Lefthook is already installed
if ! command -v lefthook >/dev/null 2>&1; then
    echo "Lefthook is not installed. Installing Lefthook via Homebrew..."
    brew install lefthook
else
    echo "Lefthook is already installed."
fi

# Sync Lefthook config with Git hooks (Assuming lefthook.yml already exists)
echo "Installing Git hooks with Lefthook..."
lefthook install

echo "Lefthook installation and setup complete."