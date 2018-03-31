import unittest
import os


def all_case():
    case_path = os.path.join(os.path.dirname(__file__), "test")
    discover = unittest.defaultTestLoader.discover(
        case_path, pattern='test*.py', top_level_dir=None)
    print discover
    return discover


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())