# BCTCI Java workspace

This directory currently contains `compile.sh`, `run.sh`, and `test/TestTemplate.java`.
No solution sources are committed, so compilation needs a solution added first.

## Add and run a solution

From this directory, create `src/` and add a Java file with a matching public class and a `main` method.
For example, after adding `src/Example.java`:

```sh
bash compile.sh
bash run.sh Example
```

A JDK and Bash are required.
The compiler helper writes classes from `src/*.java` to `bin/`.
The test template is a starting point for authored cases; the helpers do not execute it automatically.
