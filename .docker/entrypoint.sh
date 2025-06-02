#!/bin/sh

# Replace placeholder in runtime-config.js with actual value
API_URL=${NEXT_PUBLIC_API_BASE_URL:-http://localhost:8000}

echo "Injecting API URL into runtime config: $API_URL"

sed -i "s|PLACEHOLDER|$API_URL|g" /app/public/runtime-config.js

# Start the app
exec npm start
