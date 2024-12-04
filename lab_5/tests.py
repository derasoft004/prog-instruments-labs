import pytest
import pygame
from objects import Road


@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_road_initialization():
    road = Road()
    assert road.x == 30
    assert road.y1 == 0
    assert road.y2 == -512
