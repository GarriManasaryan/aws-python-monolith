#!/bin/bash

echo "🎨 Alembic create revision"

# Prompt for comment if not provided
if [ -z "$1" ]; then
  read -p "Enter revision comment: " comment
else
  comment="$1"
fi

alembic revision -m "$comment"

