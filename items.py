from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    sell_price: int


ITEMS: dict[str, Item] = {
    "Carrot": Item(name="Carrot", sell_price=7),
    "Lettuce": Item(name="Lettuce", sell_price=10),
    "Tomato": Item(name="Tomato", sell_price=15),
    "Apple": Item(name="Apple", sell_price=3),
    "Storm Seed": Item(name="Storm Seed", sell_price=40),
    "Storm Crystal": Item(name="Storm Crystal", sell_price=120),
}
