# ─── Window ───────────────────────────────────────────────────────────────────
TITLE        = "Pass the Game - Farm Patch"
SCREEN_W     = 1200
SCREEN_H     = 600
FPS          = 60

# ─── Sky colours ──────────────────────────────────────────────────────────────
SKY_DAY      = (135, 206, 235)   # clear-day blue
SKY_DARK     = (40,  55,  90)    # overcast / sun-covered

# ─── Sun ──────────────────────────────────────────────────────────────────────
SUN_X        = 520
SUN_Y        = 100
SUN_RADIUS   = 55
SUN_COLOR    = (255, 220, 50)

# ─── Moon ──────────────────────────────────────────────────────────────────────
MOON_X        = 520
MOON_Y        = 100
MOON_RADIUS   = 55
MOON_COLOR    = (235, 230, 200)
BITE_OFFSET_X = 18
BITE_OFFSET_Y = -6
BITE_RADIUS_RATIO = 0.85 #relative to MOON_RADIUS

# ─── Stars ──────────────────────────────────────────────────────────────────────
STAR_COLOR        = (240, 240, 220)
STAR_COUNT        = 60
SPARKLING_SPEED     = 2 #rad/sec

# ─── Cloud ────────────────────────────────────────────────────────────────────
CLOUD_START_X    = 700
CLOUD_START_Y    = 150
CLOUD2_START_X   = 200
CLOUD2_START_Y   = 120
CLOUD_SPEED      = 4          # pixels per frame when arrow key held
CLOUD_USE_IMAGE  = True       # set False to fall back to drawn cloud
WIND_SPEED       = 0.4        # wind moves clouds even when player isn't pressing any keys
                              # WIND_SPEED is a delta of num of pixels per frame
# ─── Rain ─────────────────────────────────────────────────────────────────────
RAIN_COLOR       = (130, 170, 220)
RAIN_DROP_COUNT  = 200
RAIN_SPEED_MIN   = 8
RAIN_SPEED_MAX   = 14
RAIN_LENGTH      = 12

# ─── Farm layout ───────────────────────────────────────────────────────────────
UI_PANEL_W        = 240
GROUND_HEIGHT_PCT = 0.10
SLOT_COUNT        = 10
SLOT_PADDING      = 6
SLOT_COLOR        = (150, 110, 80)
SLOT_BORDER_COLOR = (110, 80, 60)
GROUND_COLOR      = (115, 85, 65)

# ─── Plant simulation ─────────────────────────────────────────────────────────
WATER_GAIN_RAIN   = 0.15
WATER_LOSS        = 0.05
SUN_GAIN_CLEAR    = 0.15
SUN_LOSS          = 0.07
PLANT_MAX_STAT    = 100.0
OVERWATER_THRESHOLD = 92.0
OVERSUN_THRESHOLD   = 92.0
PLANT_BAD_SECONDS_TO_DIE = 6.0
PLANT_BAD_RECOVERY_RATE = 1.5
PLANT_GROWTH_RATE_GOOD = 1.0
PLANT_GROWTH_RATE_BAD = 0.4
PLANT_SPRITE_W = 64
PLANT_SPRITE_H = 96

# ─── In-game time ────────────────────────────────────────────────────────────
# We use an in-game "week" to schedule the Storm Titan. This is intentionally
# tunable so contributors can make the cadence faster/slower.
IN_GAME_DAY_SECONDS = 60.0
IN_GAME_DAYS_PER_WEEK = 7
IN_GAME_WEEK_SECONDS = IN_GAME_DAY_SECONDS * IN_GAME_DAYS_PER_WEEK

# ─── Storm Titan (boss) ──────────────────────────────────────────────────────
STORM_TITAN_WIDTH = 260
STORM_TITAN_HEIGHT = 130
STORM_TITAN_Y = 32

# 5 reflected blocks defeats the boss.
STORM_TITAN_MAX_HP = 5
# Spawn twice per in-game week.
STORM_TITAN_SPAWN_EVERY_SECONDS = IN_GAME_WEEK_SECONDS / 2

STORM_TITAN_STRIKE_COOLDOWN_SECONDS = 3.0
STORM_TITAN_STRIKE_WARNING_SECONDS = 1.0

# When the boss is defeated it lingers briefly, then leaves.
STORM_TITAN_RETREAT_SECONDS = 3.0

# Reward is delivered as an inventory item the player can plant.
STORM_TITAN_REWARD_ITEM_NAME = "Storm Seed"
STORM_TITAN_REWARD_ITEM_COUNT = 1

# Plant effect for an unblocked strike.
STORM_TITAN_LIGHTNING_KILLS_PLANT = True

# Visuals (fallback drawing if PNGs are missing)
STORM_TITAN_IMAGE_FILENAME = "storm_titan.png"

# ─── Cyclone Titan (boss) ───────────────────────────────────────────────────
CYCLONE_TITAN_WIDTH = 340
CYCLONE_TITAN_HEIGHT = 180
CYCLONE_TITAN_Y = 18

# Bigger boss with a bigger health bar.
CYCLONE_TITAN_MAX_HP = 12
CYCLONE_TITAN_SPAWN_EVERY_SECONDS = IN_GAME_WEEK_SECONDS

CYCLONE_TITAN_STRIKE_COOLDOWN_SECONDS = 2.4
CYCLONE_TITAN_STRIKE_WARNING_SECONDS = 0.9

CYCLONE_TITAN_RETREAT_SECONDS = 3.5

# Unblocked strikes one-shot plants and also hit nearby slots.
CYCLONE_TITAN_AOE_RADIUS_SLOTS = 1

# Visuals (fallback drawing if PNGs are missing)
CYCLONE_TITAN_IMAGE_FILENAME = "cyclone_titan.png"

# ─── Critters (squirrel/snake) ─────────────────────────────────────────────
# Spawn rolls are checked at a fixed interval while the game is unpaused.
CRITTER_SPAWN_CHECK_SECONDS = 1.0

SQUIRREL_SPAWN_CHANCE = 1 / 20
SQUIRREL_SPEED_PX_PER_SEC = 180.0
SQUIRREL_EAT_SECONDS = 3.0
SQUIRREL_IMAGE_FILENAME = "squirrel.png"

SNAKE_SPAWN_CHANCE = 1 / 50
SNAKE_SPEED_PX_PER_SEC = 240.0
SNAKE_EAT_SECONDS = 4.0
SNAKE_IMAGE_FILENAME = "snake.png"
