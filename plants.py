from __future__ import annotations

from abc import ABC


class PlantType(ABC):
    name: str
    cost: int
    product_name: str
    growth_stages: int
    frames_per_stage: int
    water_min: float
    water_max: float
    sun_min: float
    sun_max: float
    base_color: tuple[int, int, int]
    icon_filename: str

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Carrot(PlantType):
    name = "Carrot"
    cost = 5
    product_name = "Carrot"
    growth_stages = 3
    frames_per_stage = 120
    water_min = 35.0
    water_max = 75.0
    sun_min = 35.0
    sun_max = 80.0
    base_color = (230, 140, 60)
    icon_filename = "carrot_icon.png"


class Lettuce(PlantType):
    name = "Lettuce"
    cost = 4
    product_name = "Lettuce"
    growth_stages = 3
    frames_per_stage = 100
    water_min = 45.0
    water_max = 85.0
    sun_min = 25.0
    sun_max = 70.0
    base_color = (90, 180, 90)
    icon_filename = "lettuce_icon.png"


class Tomato(PlantType):
    name = "Tomato"
    cost = 7
    product_name = "Tomato"
    growth_stages = 4
    frames_per_stage = 130
    water_min = 40.0
    water_max = 80.0
    sun_min = 40.0
    sun_max = 85.0
    base_color = (200, 70, 70)
    icon_filename = "tomato_icon.png"
