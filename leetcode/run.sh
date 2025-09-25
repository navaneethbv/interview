#!/bin/bash

# Run a specific Java class
if [ $# -eq 0 ]; then
    echo "Usage: $0 <ClassName>"
    echo "Example: $0 TwoSum"
    exit 1
fi

CLASS_NAME=$1

# Check if bin directory exists
if [ ! -d "bin" ]; then
    echo "bin directory not found. Please run ./compile.sh first."
    exit 1
fi

# Check if class file exists
if [ ! -f "bin/${CLASS_NAME}.class" ]; then
    echo "Class file bin/${CLASS_NAME}.class not found."
    echo "Make sure the class exists in src/ and you've compiled it."
    exit 1
fi

echo "Running ${CLASS_NAME}..."
java -cp bin $CLASS_NAME