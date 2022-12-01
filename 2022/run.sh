#!/bin/bash
function run_v(){
    v ./$1.v
    ./$1
    rm ./$1.exe
}

python ./solution_1.py
deno run ./solution_1.ts
run_v solution_1