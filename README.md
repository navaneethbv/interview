# Interview practice in Java

Small standalone Java exercises with shell helpers for compiling and running examples.
This repository is separate from the [Interview Practice website](https://github.com/navaneethbv/interview-practice).

## Collections

- [LeetCode](leetcode/README.md): `TwoSum` and `PalindromeNumber`, each with a `main` method containing sample cases.
- [BCTCI workspace](bctci/README.md): compile/run helpers and a test template; no solution sources are committed yet.

## Run an example

Install a JDK providing `javac` and `java`, plus Bash.
Run the helpers from the collection directory because their paths are relative to that directory.

```sh
cd leetcode
bash compile.sh
bash run.sh TwoSum
bash run.sh PalindromeNumber
```

The current examples use hard-coded cases rather than reading standard input.
The helpers compile `src/*.java` into `bin/`; they do not compile or run `test/TestTemplate.java`.
