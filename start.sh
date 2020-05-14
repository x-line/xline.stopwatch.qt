#!/bin/bash

if [[ -z "$VIRTUAL_ENV" ]]; then
    . env-act
fi

python mainwindow.py