#!/bin/bash
# Simple wrapper to update the problem tracker

cd "$(dirname "$0")"
python3 update_problem_tracker.py
