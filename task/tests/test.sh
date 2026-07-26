#!/bin/bash
set -u

verifier_dir="/logs/verifier"
if ! mkdir -p "$verifier_dir" 2>/dev/null; then
  verifier_dir="$(pwd)/.verifier"
  mkdir -p "$verifier_dir"
fi

pytest --ctrf "$verifier_dir/ctrf.json" /tests/test_outputs.py -rA > "$verifier_dir/pytest.log" 2>&1
status=$?
if [ "$status" -eq 0 ]; then
  echo 1 > "$verifier_dir/reward.txt"
else
  echo 0 > "$verifier_dir/reward.txt"
fi
exit 0
