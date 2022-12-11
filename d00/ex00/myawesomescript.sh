#!/bin/sh

if [ -n "$1" ] 
then
curl -I -s $1 | grep Location | cut -c 11-
fi
