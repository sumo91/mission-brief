#!/bin/sh
set -eu
work=$(mktemp -d "${TMPDIR:-/tmp}/mission-webhook.XXXXXX")
trap 'rm -rf "$work"' EXIT
signature=$(printf '%s' settlement:evt1 | /usr/bin/openssl dgst -sha256 -hmac fixture-only-key | /usr/bin/awk '{print $NF}')
script=$(dirname "$0")/webhook.sh
[ "$(/bin/sh "$script" settlement:evt1 "$signature" "$work/ledger")" = accepted:evt1 ]
[ "$(/bin/sh "$script" settlement:evt1 "$signature" "$work/ledger")" = duplicate:evt1 ]
if /bin/sh "$script" settlement:evt2 invalid "$work/ledger"; then exit 1; fi
[ "$(wc -l < "$work/ledger" | tr -d ' ')" = 1 ]
printf 'PASS: valid signature, invalid signature, replay deduplication; local fixture only\n'
