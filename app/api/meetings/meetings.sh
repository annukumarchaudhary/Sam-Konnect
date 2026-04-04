#!/bin/bash

API_KEY_SECRET="sam_konnect_secret_2026"
MIROTALK_URL="https://p2p.mirotalk.com/api/v1/meetings"
#MIROTALK_URL="http://localhost:3000/api/v1/meetings"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request GET
