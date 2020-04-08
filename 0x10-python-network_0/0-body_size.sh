#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sD - -o /dev/null "$1" | grep Content-Length: | cut -d' ' -f2
