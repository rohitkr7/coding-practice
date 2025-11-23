#!/bin/bash
# Problem Learning Workflow - Quick Start Script
# Makes it easy to start learning a new problem with Cascade AI

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to display usage
usage() {
    echo -e "${BLUE}Problem Learning Workflow${NC}"
    echo ""
    echo "Usage:"
    echo "  ./start-problem.sh <problem_file>"
    echo "  ./start-problem.sh --complete <problem_file>"
    echo ""
    echo "Examples:"
    echo "  ./start-problem.sh problems/two-pointers/LND-30-2-contains-duplicate.md"
    echo "  ./start-problem.sh --complete problems/two-pointers/LND-29-1-two-sum.md"
    echo ""
    echo "Options:"
    echo "  --complete    Generate completion prompt for documenting solved problems"
    echo ""
    exit 1
}

# Check if no arguments provided
if [ $# -eq 0 ]; then
    usage
fi

# Run the Python script
python3 "$SCRIPT_DIR/start_problem.py" "$@"
