# Welcome to Game Dev Club Pass the Game challenge

This is a collaborative game dev experiment where one game gets passed around and evolves with every contributor. You take the game, add your twist, and pass it on. Simple as that.

## How it works

1. Clone or pull the repository  
2. Create a new branch for your changes (call it your name)  
3. Do your thing  
   - Add a feature (can range from something very simple to some enormous 2GBs of code)
   - Improve something  
   - Break something and fix it better  
   - Be creative  
4. Push your branch  
5. Open a pull request  
6. Once it is approved, it gets merged into the main game  
7. Pull again later and see how the game has changed  (optional)

That is it. Keep it fun and keep it moving.

For the practical "how do I actually open a PR" details, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Rules and guidelines

- Keep your changes reasonable so others can build on them  
- Write comments as if you are talking to the next person
- Make sure the game still runs  
- Do not overwrite someone else's work unless you are improving it  
- Have fun with it  
- Make a before-after video of how you evolved the game (*Completely optional, for fun purposes only*)

## Tech

- Language: Python 3.9+
- Library: pygame 2.5+

## How to run

```bash
# (optional but recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

## Farming notes
- Sprites are optional; the game draws placeholders if files are missing.
- Plant stats and sprite filenames live in `plants.py`.
- Item sell prices live in `items.py`.

## Adding a new plant
1. Add a new subclass in `plants.py` with its stats, icon, and phase sprites.
2. Register the plant by adding an instance to `Game.seeds` in `game.py`.
3. (Optional) Add its item price to `items.py` if it produces a new product.
4. Drop any new sprites into `props/` and list them in `props/README.md`.

## Customizing a plant
use following optional class attributes for your PlantType subclass
- harvest_yield — num of items produced per harvest (default is 1)
- regrow_to_stage — if set, plant resets to this stage after harvest instead of being cleared. Useful for re-fruiting plants (default is None)
- sprite_w, sprite_h — custom sprite width, height in px (default is None, falls back to `PLANT_SPRITE_W`/`PLANT_SPRITE_H` from settings.py)


## Controls
- Arrow keys: move first cloud
- WASD: move second cloud
- Click cloud: toggle rain
- Drag or click seed to plant
- Click harvestable plant to collect
- Click dead plant to clear
- P: pause / resume (animations keep playing)
- ESC: quit
- B: (cheat) toggle Storm Titan spawn / despawn
- C: (cheat) toggle Cyclone Titan spawn / despawn
- V: (cheat) force-spawn the chipmunk thief
- N: (cheat) force-spawn the snake thief
- Click a critter: scare it away

## Boss fights + critters

### Storm Titan
- Spawns **twice per in-game week** (cadence is tunable in `settings.py`).
- Targets a planted slot, shows a warning, then strikes lightning.
- **Block the strike** by moving any cloud to cover the target x-position. If blocked, the lightning reflects and damages the boss (**5 hits** defeats it).
- On defeat it lingers briefly, then leaves, and drops a **Storm Seed** (plantable reward).

### Cyclone Titan
- Spawns **once per in-game week**.
- Bigger boss with a bigger health bar.
- Unblocked strikes one-shot plants and also hit nearby slots (AoE).

### Plant thieves (critters)
- Chipmunk thief + snake thief can spawn from either side and try to eat a planted slot (then the plant is removed).
- Clicking a thief scares it into fleeing off-screen.

## Project structure

```
pass_the_game/
│
├── main.py          # entry point – init pygame, create Game, run loop
├── game.py          # Game class – main loop, update, draw
├── cloud.py         # Cloud sprite + RainDrop helper
├── sun.py           # Sun sprite
├── moon.py          # Moon sprite (appears at night)
├── stars.py         # Sparkling stars (appear at night)
├── farming.py       # PlantSlot state + rendering helpers
├── plants.py        # Plant type definitions (stats + sprite names)
├── items.py         # Item registry and sell prices
├── settings.py      # all tuneable constants live here
├── requirements.txt
│
└── props/           # drop your PNG images here
    ├── README.md    # lists expected filenames and sizes
    ├── your prop images    # if you use one
```

**Tip for contributors:** `settings.py` is the first place to look when you
want to tweak speeds, colours, or counts.  Add new sprites as their own files
and register them in `game.py`.


## Contributors log

Add your name and 1–2 lines about what you added below.

- **Nancy**  
  Created the base game: blue sky, a movable cloud, rain on click, and a sun that darkens the sky when covered.

- **Minh**  
  Added farming: buying/planting seeds, keep plant alive with rain and sun, sell products for profit.

- **Danel**
  Added night (transition to moon and stars), second cloud (WASD keys), "wind", pausing, apple tree that regrows to previous phase after harvesting apples

- **Yousef**
  Added Storm Titan + Cyclone Titan boss fights (timed spawns, health bars, blockable lightning) + chipmunk/snake plant-thief critters.

  Cheats (developer shortcuts):
  - **B**: toggle Storm Titan spawn / despawn
  - **C**: toggle Cyclone Titan spawn / despawn
  - **V**: force-spawn the chipmunk (squirrel) thief
  - **N**: force-spawn the snake thief

  Highlights of my contributions:
  - Implemented a Tools system (right-panel UI): `Compost`, `Scarecrow`, `Lightning Rod` with placement/use logic and UI buttons.
  - `Compost` is an inventory item; clearing dead plants yields Compost; Compost applies a time-limited growth boost to a slot.
  - Scarecrow: placeable on empty slots (protects nearby slots); drawn as an in-game placeholder if no sprite is provided.
  - Lightning Rod: placeable on planted slots; grants charges that prevent plant death from boss lightning.
  - Introduced Season/World time tracking (day/week/season) and applied season multipliers to plant growth, water loss, and sun gain.
  - Added a Market system: daily featured/discounted items (applies multipliers at sell-time) and HUD display for market state; added a Sell All confirmation overlay.
  - Added Weather framework and events (Heatwave, Drizzle, Gusts) and rain intensity modes (Off / Light / Heavy); heavy rain increases growth rate while drizzle provides water bonuses.
  - Registered new items in `items.py`: `Compost`, `Fur`, `Venom`, `Cyclone Crystal`, and new plant products (Mushroom, Cactus Fruit, Rice, Night Bloom, Pumpkin).
  - Implemented five new plants: `Mushroom`, `Cactus`, `Rice`, `Night Bloom`, and `Pumpkin`. Each has a sensible default `icon_filename` and `phase_filenames` so art can be added later.
  - Polished HUD feedback: market and boss hints, sell confirmation, and clearer status lines for boss timers and seasons.
  - Critters now can drop items (e.g., `Fur`, `Venom`) when they steal plants; the game collects those drops into inventory.
  - Cyclone Titan now drops `Cyclone Crystal` on defeat and requires a *raining* cloud to block its strikes.
  - Perfect-block mechanic: blocking within a short window before a strike deals bonus boss damage and is detected via recent cloud rain toggles.
  - Removed the optional audio subsystem (SFX loader) per request to keep the codebase minimal; placeholders remain where audio can be wired later.

  Notes for artists/contributors: add PNG or SVG assets into `props/` named to match the `icon_filename` and `phase_filenames` in `plants.py` (the game falls back to drawn placeholders when files are missing).

---

Let's see how wild this game becomes 👀
