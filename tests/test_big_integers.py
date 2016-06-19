# pylint: disable=missing-docstring

"""Big Integers"""

import pytest

from basic_problems.big_integers import power

EXAMPLES = (
    ('number', 'degree', 'expected'),
    [
        (2, 0, 1),
        (2, 2, 4),
        (3, 3, 27),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, degree, expected):
    assert power(number, degree) == expected
