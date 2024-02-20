#!/bin/sh
# vim:sw=4:ts=4:et

pnpm i
pnpm run build

exec "$@"
