import pytest

from cool_project.calculus import sum_small_numbers


def test_sum_small_numbers_with_valid_inputs():
    """Test valid inputs."""
    assert sum_small_numbers(10, 20) == 30


def test_sum_small_numbers_with_a_too_big():
    """Test when `a` is too big."""
    with pytest.raises(ValueError, match="a is too big, must be smaller than 100"):
        sum_small_numbers(101, 20)


def test_sum_small_numbers_with_b_too_big():
    """Test when `b` is too big."""
    with pytest.raises(ValueError, match="b is too big, must be smaller than 50"):
        sum_small_numbers(10, 51)


def test_sum_small_numbers_with_a_and_b_too_big():
    """Test when both `a` and `b` are too big."""
    with pytest.raises(ValueError, match="a is too big, must be smaller than 100"):
        sum_small_numbers(101, 51)
