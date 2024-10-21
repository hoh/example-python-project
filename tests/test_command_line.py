import pytest
from typer.testing import CliRunner

from cool_project.__main__ import app


@pytest.fixture
def runner():
    return CliRunner()


def test_hello_with_valid_name(runner: CliRunner):
    """Test hello command with valid name."""
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice" in result.output


def test_do_sum_with_valid_inputs(runner: CliRunner):
    """Test do-sum command with valid inputs."""
    result = runner.invoke(app, ["do-sum", "10", "20"])
    assert result.exit_code == 0
    assert "Result: 30" in result.output


def test_do_sum_with_a_too_big(runner: CliRunner):
    """Test do-sum command with `a` too big."""
    result = runner.invoke(app, ["do-sum", "101", "20"])
    assert result.exit_code != 0
    assert "a is too big, must be smaller than 100" in result.output


def test_do_sum_with_b_too_big(runner: CliRunner):
    """Test do-sum command with `b` too big."""
    result = runner.invoke(app, ["do-sum", "10", "51"])
    assert result.exit_code != 0
    assert "b is too big, must be smaller than 50" in result.output


def test_do_sum_with_a_and_b_too_big(runner: CliRunner):
    """Test do-sum command with both `a` and `b` too big."""
    result = runner.invoke(app, ["do-sum", "101", "51"])
    assert result.exit_code != 0
    assert "a is too big, must be smaller than 100" in result.output
