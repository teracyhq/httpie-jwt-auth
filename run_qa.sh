#!/usr/bin/env bash

set -e

#pip install -e .
make check-style
make test
