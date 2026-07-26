#!/usr/bin/env bash
set -euo pipefail

output_path="/workspace/output.txt"
if [ ! -d /workspace ]; then
  output_path="./output.txt"
fi

mkdir -p "$(dirname "$output_path")"
cat > "$output_path" <<'EOF'
project-dynamo task complete
EOF
