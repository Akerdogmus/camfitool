import sys
import types

# Provide a minimal stub for gui_restart_app to satisfy imports in extras
stub = types.ModuleType('gui_restart_app')
stub.restart_program = lambda: None
sys.modules['gui_restart_app'] = stub

from extras import list_substractor, str_splitter


def test_list_substractor_returns_unique_items():
    norm = ["a", "b", "c", "d"]
    faulty = ["b", "d"]
    assert list_substractor(norm, faulty) == ["a", "c"]


def test_str_splitter_returns_last_segment():
    assert str_splitter("/path/to/file.txt") == "file.txt"
    assert str_splitter("single") == "single"
