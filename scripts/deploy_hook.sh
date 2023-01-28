#!/bin/bash

cd $RENEWED_LINEAGE

if [ -f "copy" ]; then
    cat "copy" | while read SOURCE TARGET; do
        cp "$SOURCE" "$TARGET"
    done
fi

if [ -f "init.d" ]; then
    cat "init.d" | while read DAEMON; do
        "/etc/init.d/$DAEMON" restart -q
    done
fi

if [ -f "systemctl" ]; then
    cat "systemctl" | while read DAEMON COMMAND; do
        "systemctl" ${COMMAND:-restart} $DAEMON
    done
fi

if [ -f "docker" ]; then
    cat "docker" | while read CONTAINER; do
        OUTPUT="$(docker restart "$CONTAINER")"
        if [ "$OUTPUT" != "$CONTAINER" ]; then
            echo "$OUTPUT"
        fi
    done
fi
