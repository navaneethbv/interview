#!/bin/bash

# Compile all Java files in the src directory
echo "Compiling Java files..."

# Create bin directory if it doesn't exist
mkdir -p bin

# Compile all Java files from src to bin
javac -d bin src/*.java

if [ $? -eq 0 ]; then
    echo "Compilation successful!"
else
    echo "Compilation failed!"
    exit 1
fi