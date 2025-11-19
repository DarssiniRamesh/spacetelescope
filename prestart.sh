#!/bin/bash
# Pre-start script to ensure all dependencies are installed before the Django app starts

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}[Pre-start] Ensuring dependencies are installed...${NC}"

# Determine the correct Python and pip to use
if [ -d "venv" ]; then
    PYTHON="./venv/bin/python"
    PIP="./venv/bin/pip"
    echo -e "${GREEN}[Pre-start] Using virtual environment${NC}"
elif [ -d ".venv" ]; then
    PYTHON="./.venv/bin/python"
    PIP="./.venv/bin/pip"
    echo -e "${GREEN}[Pre-start] Using virtual environment (.venv)${NC}"
else
    PYTHON="python3"
    PIP="pip3"
    echo -e "${YELLOW}[Pre-start] No virtual environment found, using system Python${NC}"
fi

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}[Pre-start] Installing requirements from requirements.txt...${NC}"
    $PIP install -q -r requirements.txt || {
        echo -e "${YELLOW}[Pre-start] Warning: Some packages may have failed to install${NC}"
    }
else
    echo -e "${YELLOW}[Pre-start] No requirements.txt found${NC}"
fi

# Verify critical packages
echo -e "${GREEN}[Pre-start] Verifying critical packages...${NC}"
$PYTHON -c "import inflection" 2>/dev/null || {
    echo -e "${YELLOW}[Pre-start] inflection not found, installing...${NC}"
    $PIP install -q "inflection>=0.5.1,<0.6.0"
}

$PYTHON -c "import django" 2>/dev/null || {
    echo -e "${YELLOW}[Pre-start] Django not found, installing...${NC}"
    $PIP install -q "Django>=3.2,<5.0"
}

echo -e "${GREEN}[Pre-start] Dependency check complete!${NC}"
