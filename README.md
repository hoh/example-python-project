# Example Python project with tests

This is a simple project that demonstrates how to test a Python project 
using `pytest`.

Install in developer mode with: 
```shell
pip install -e .
```

Run with:
```shell
cool hello SomeName
```

## Testing

Run tests using `pytest`:
```shell
hatch run testing:test
```

Check code quality using:
```shell
hatch run testing:lint
```

Automatically format code using:
```shell
hatch run testing:format
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
