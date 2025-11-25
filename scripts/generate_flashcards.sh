#!/bin/bash
# Generate flashcards for all completed problems

cd "$(dirname "$0")"
python3 generate_flashcard.py --all
