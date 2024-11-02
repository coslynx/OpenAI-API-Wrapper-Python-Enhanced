#!/bin/bash
set -euo pipefail

# Environment Setup
source .env

# Function Definitions
log_info() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - INFO: $*"
}
log_error() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - ERROR: $*" >&2
}
cleanup() {
  log_info "Cleaning up processes and files..."
  pkill -f "uvicorn main:app"
  rm -f /tmp/backend.pid
}

# Main Execution Flow
trap cleanup EXIT ERR

log_info "Starting AI Powered OpenAI Request Wrapper MVP..."

# Start Backend Server
log_info "Starting backend server..."
/usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 8000 &
store_pid "backend"

log_info "Backend server started successfully!"

# Startup Completion
log_info "AI Powered OpenAI Request Wrapper MVP started successfully!"

# Store PID
store_pid() {
  local service_name=$1
  echo $! > /tmp/${service_name}.pid
}