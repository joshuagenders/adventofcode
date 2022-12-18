#!/bin/bash
function run_v(){
    v ./1/$1.v
    ./1/$1
    rm ./1/$1.exe
}

python ./1/solution_1.py
deno run ./1/solution_1.ts
run_v solution_1