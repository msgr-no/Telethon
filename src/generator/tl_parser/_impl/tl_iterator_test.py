from pytest import raises

from .tl_iterator import FunctionDef, TypeDef, iterate


def test_parse_bad_separator() -> None:
    with raises(ValueError) as e:
        for _ in iterate("---foo---"):
            pass
    e.match("bad separator")


def test_parse_file() -> None:
    items = list(
        iterate(
            """
            // leading; comment
            first#1 = t; // inline comment
            ---functions---
            second and bad;
            third#3 = t;
            // trailing comment
            """
        )
    )
    assert len(items) == 3
    assert isinstance(items[0], TypeDef) and items[0].id == 1
    assert isinstance(items[1], ValueError)
    assert isinstance(items[2], FunctionDef) and items[2].id == 3
