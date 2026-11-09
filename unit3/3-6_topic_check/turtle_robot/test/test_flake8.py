"""패키지의 flake8 규칙을 검사합니다."""

from pathlib import Path

from ament_flake8.main import main


def test_flake8():
    """전체 패키지 검사를 통과해야 합니다."""
    root = Path(__file__).resolve().parents[1]
    result = main(argv=[str(root)])
    assert result == 0
