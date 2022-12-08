#!/bin/bash
mkdir day$1
cd day$1
curl -v --cookie $AOC https://adventofcode.com/2022/day/$1/input > "actual.txt"
touch "sample.txt" "sol.py"

