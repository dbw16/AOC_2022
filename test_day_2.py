from unittest import TestCase
import pytest

from day_2 import Move


class TestMove(TestCase):
    def test_win_loss(self):
        assert Move.rock > Move.scissors
        assert Move.paper > Move.rock
        assert Move.scissors > Move.paper

    def test_draw(self):
        assert Move.rock == Move.rock
        assert Move.paper == Move.paper
        assert Move.scissors == Move.scissors
