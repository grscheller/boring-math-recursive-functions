# Copyright 2016-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Recursive functions examples
============================

Example implementations for various recursive functions.

"""

from collections.abc import Iterator

__all__ = ['ackermann_list', 'fibonacci_generator', 'rev_fibonacci_generator']


def ackermann_list(m: int, n: int) -> int:
    """Ackermann's Function.

    .. note::

        This implementation models the recursion with a Python list
        instead of Python's "call stack". It then evaluates the
        innermost ackermann function first. To naively use call stack
        recursion would result in the loss of stack safety.

    :param m: First argument to Ackermann's function.
    :param n: Second argument to Ackermann's function.
    :returns: A very hard to calculate useless value.

    """
    acker = [m, n]

    while len(acker) > 1:
        mm, nn = acker[-2:]
        if mm < 1:
            acker[-1] = acker.pop() + 1
        elif nn < 1:
            acker[-2] = acker[-2] - 1
            acker[-1] = 1
        else:
            acker[-2] = mm - 1
            acker[-1] = mm
            acker.append(nn - 1)
    return acker[0]


def fibonacci_generator(fib0: int = 0, fib1: int = 1) -> Iterator[int]:
    """
    Generate a Fibonacci sequence instead of recursively evaluating it.

        Beginning: ``fib0, fib1, fib0+fib1, ...``

        Defaults yield: ``0, 1, 1. 2, 3, 5, 8, 13, ...``

    :param fib0: Zeroth element of sequence.
    :param fib1: Next element of sequence.
    :returns: Iterator iterating over a Fibonacci sequence.

    """
    while True:
        yield fib0
        fib0, fib1 = fib1, fib0 + fib1


def rev_fibonacci_generator(fib0: int = 0, fib1: int = 1) -> Iterator[int]:
    """
    Generate a reverse Fibonacci sequence instead of recursively evaluating it.

        Beginning ``fib1, fib0, fib1-fib0, ...``

        Defaults yield: ``0, 1, -1, 2, -3, 5, -8, 13, ...``

    :param fib0: Zeroth element of sequence.
    :param fib1: Next element of sequence.
    :returns: Iterator iterating over a Fibonacci sequence in reverse order.

    """
    while True:
        fib0, fib1 = fib1, fib0 - fib1
        yield fib0
