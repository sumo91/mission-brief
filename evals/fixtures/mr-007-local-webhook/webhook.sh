#!/bin/sh
# Synthetic local acceptance fixture; no production credentials or network.
set -eu
payload=$1
signature=$2
ledger=$3
case "$payload" in settlement:*) ;; *) exit 2 ;; esac
event_id=${payload#settlement:}
case "$event_id" in ''|*[!a-zA-Z0-9_-]*) exit 2 ;; esac
expected=$(printf '%s' "$payload" | /usr/bin/openssl dgst -sha256 -hmac fixture-only-key | /usr/bin/awk '{print $NF}')
[ "$signature" = "$expected" ] || exit 3
[ -f "$ledger" ] || : > "$ledger"
if /usr/bin/awk -v id="$event_id" '$0 == id { found=1 } END { exit !found }' "$ledger"; then
    printf 'duplicate:%s\n' "$event_id"
else
    printf '%s\n' "$event_id" >> "$ledger"
    printf 'accepted:%s\n' "$event_id"
fi
