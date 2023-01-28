#!/bin/bash

BASE_DIR="$(dirname $0)"
AUTH_HOOK_PATH="$BASE_DIR/auth_hook.py"
CLEANUP_HOOK_PATH="$BASE_DIR/cleanup_hook.py"
DEPLOY_HOOK_PATH="$BASE_DIR/deploy_hook.sh"

certbot renew \
	--preferred-challenges dns \
	--manual \
	--manual-auth-hook "$AUTH_HOOK_PATH" \
	--manual-cleanup-hook "$CLEANUP_HOOK_PATH" \
	--deploy-hook "$DEPLOY_HOOK_PATH"
	$@
