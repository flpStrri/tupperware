>First off, thank you for considering contributing to tupperware!

# Introduction

Hello! Are you here to help on Tupperware?
Awesome, feel welcome and read the following sections in order to know how to ask questions and how to help us make this software better.

All members of our community are expected to follow our [Code of Conduct][CodeOfConduct].
Please make sure you are welcoming and friendly in all of our spaces.

# How to contribute

## Tutorials

If you want to start working on this project,
you will need to get familiar with these concepts:

- http://learnyouahaskell.com/functors-applicative-functors-and-monoids
- https://github.com/dbrattli/OSlash/wiki/Functors,-Applicatives,-And-Monads-In-Pictures

## Dependencies

We use [`poetry`][poetry] to manage dependencies, to get started — after installing it — ensure you have a python@3.7 or python@3.8 environment.
If you don't you can install it with `brew install python3.7` or `brew install python3.8` respectively.  

After installing Python, find the `python3` file location (if you installed with brew it will be at `/usr/local/opt/python@3.7/bin/python3` or `/usr/local/opt/python@3.8/bin/python3`) and follow these steps:

```shell
git clone git@github.com:flpStrri/tupperware.git
cd tupperware
poetry env use <-- Python python3 path -->
make test
```

This will install all the dependencies (including development ones),
and run all static and unit tests.

## Tests

We use `pytest`, `mypy`, `flake8`, and `black` for quality control.

To run all tests:

```bash
make test
```

To run static tests (style, linting and typing):

```bash
make test-static
```

These steps are mandatory during the CI.

### Type tests

We also use `pytest-mypy-plugins`. Tests cases are located inside `./typesafety`
If you create new types or typed functions, it is required to test their types.
Here's [a tutorial](https://sobolevn.me/2019/08/testing-mypy-types) on how to do that.


## Type checks

We use `mypy` to run type checks on our code.
To use it:

```bash
make test-type
```

This step is mandatory during the CI.


## Submitting your code

We use [trunk based](https://trunkbaseddevelopment.com/) development (we also sometimes call it `github-flow`).

What the point of this method?

1. We use protected `master` branch, so the only way to push your code is via pull request
2. We use issue branches: to implement a new feature or to fix a bug create a new branch named `issue-$TASKNUMBER`
3. Then create a pull request to `master` branch
4. We use `git tag`s to make releases, so we can track what has changed since the latest release

So, this way we achieve an easy and scalable development process which frees us from merging hell and long-living branches.

In this method, the latest version of the app is always in the `master` branch.

### Before submitting

Before submitting your code please do the following steps:

1. Run `make test` to make sure everything was working before
2. Add any changes you want
3. Add tests for the new changes
4. Edit documentation if you have changed something significant
5. Update `CHANGELOG.md` with a quick summary of your changes
6. Run `make test` again to make sure it is still working


## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write a short article on how you are using this project.
You can also share your best practices with us.

[CodeOfConduct]: https://github.com/flpStrri/tupperware/blob/master/CODE_OF_CONDUCT.md
[poetry](https://github.com/python-poetry/poetry)