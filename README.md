<img src="https://user-images.githubusercontent.com/13003392/82924394-a4d86080-9f52-11ea-8b4c-32536bb6cc81.png" align="right" width="192px" height="192px"/>

# Tupperware <a href="https://github.com/flpStrri/tupperware/actions"><img alt="CI/CD" src="https://github.com/flpStrri/tupperware/workflows/test/badge.svg"></a> <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> <a href="https://github.com/psf/black"><img alt="Mypy: ready" src="https://img.shields.io/badge/mypy-ready-blue"></a>

Put your functions returns in a pot, please.

```
🍴 forked from https://github.com/dry-python/returns
💡 Insired by https://github.com/dbrattli/OSlash
```

## Features

- Provides an initial functional programming monads to Python land;
- Fully typed with annotations and checked with `mypy`;

## Installation

If you are using pip you can: `pip install tupperware`.

Otherwise, if you are using poetry you can: `poetry add tupperware` or add this to your `pyproject.tml`:
``` toml
[tool.poetry.dependencies]
tupperware = { git = "https://github.com/flpStrri/tupperware.git", tag = "v0.1.0" }
```

We also recommend to use the same `mypy` settings [we use](https://github.com/flpStrri/tupperware/blob/master/pyproject.toml).

## Contributing
If you want to help us building Tupperware, please start at our [CONTRIBUTING](.github/CONTRIBUTING.md) and [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) documents.


## Contents

- [Maybe container](#maybe-container) that allows you to write `None`-free code
- [Either container](#either-container) that let's you to get rid of exceptions

## Maybe container
The `Maybe` type encapsulates an optional value.
Its content can be a value (represented as `<Just a>`),
or it is empty (represented as `<Nothing>`).
This way you can map functions inside your value without having to test it 
explicitly (since the Maybe class will do it) every time it can return a `None` 
like in one of this [class tests][maybe tests]

```python
from functools import partial
from operator import add
from typing import Callable, Mapping, Optional
from tupperware.maybe import Just, Nothing

just_boris = Just({"name": "Boris"})
get_age: Callable[[Mapping], Optional[int]] = (
    lambda mapping: mapping.get("age")
)

assert (
    just_boris
    .map(get_age)
    .map(partial(add, 1))
) == Nothing()
```

## Either container

The `Either` type encapsulates a successful or failed computation.
Its content can be a successful computation value (represented as `<Right a>`),
or a a failed computation value (represented as `<Left a>`).
This way you can map and bind computations and have two different paths, errors
on the left and successful mapping and binding on the right as on this [class tests][either tests]

```python
from random import choice
from typing import Callable
from tupperware.either import Either, Left, Right


# Should return <Right 2> when binding to a <Right 1>
# given a function returning Right:

right_one = Right(1)
right_add_one: Callable[[int], Either[int, int]] = (
    lambda to_sum: Right(to_sum + 1)
)
assert right_one.bind(right_add_one) == Right(2)
assert right_one | right_add_one == Right(2)

# Should return <Left 1> when binding to a <Left 1>
# given any right typed function:

left_one = Left(1)
add_one: Callable[[int], Either[int, int]] = (
    lambda to_sum: choice(
        [Right(to_sum + 1), Left(to_sum + 1)]
    )
)
assert left_one.bind(add_one) == left_one
assert left_one | add_one == left_one
```

<p align="center">&mdash; ⚜️️ &mdash;</p>
<p align="center"><i>A blameless life, St. Joseph, may we lead; by your patronage from danger freed.</i></p>


[maybe tests]: https://github.com/flpStrri/tupperware/blob/master/tests/test_maybe
[either tests]: https://github.com/flpStrri/tupperware/blob/master/tests/test_either