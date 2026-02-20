# Game Design Document

- Project Name: `Savanna_Pulse`
- Version: `0.4.0`
- Role: `Designer_Agent`
- Status: `DRAFT`

## 1) Identity: Vision & Core Pillars

### Experience Vision
`Savanna_Pulse` is a god-sim about steering the Masai Mara migration cycle through rainfall geometry and ecological pressure management. The player fantasy is to act as an unseen natural force that shapes routes, abundance, and survival outcomes across a living ecosystem.

### Core Pillars
1. **Spatial Rain Strategy**: Tetromino rain placement creates opportunity and risk on a readable grid.
2. **Migration Flow Orchestration**: Herds are guided via terrain incentives and safe corridors, not direct unit micromanagement.
3. **Predator-Prey Coexistence**: Lions and crocodiles must be fed enough to stabilize the system without collapsing herbivore populations.
4. **System Readability**: Trails, overlays, and pulse summaries clearly communicate cause and effect every turn.

### Non-Negotiable Design Principles
- Each action must have a visible tradeoff (short-term gain vs long-term ecosystem pressure).
- Randomness creates adaptation, not helplessness.
- Failure is systemic and legible (never arbitrary).
- Player clarity is mandatory: the game must always explain what changed and why.

## 2) Loop Architecture: Micro/Macro Logic

### Micro Loop (Card Selection -> Shape Placement -> Animal Movement -> Resource Recovery)
```text
[Card Selection]
  -> Draw 3 randomized rain cards (tetromino shapes)
  -> Choose 1 card based on route and ecosystem priorities

[Shape Placement]
  -> Rotate/flip shape and place on legal grid cells
  -> Apply moisture and grass-growth triggers to covered tiles

[Animal Movement]
  -> Herbivores re-evaluate safe paths toward active seasonal destination
  -> Predators re-position along density corridors and water chokepoints
  -> Grazing/hunting outcomes update populations and threat pressure

[Resource Recovery]
  -> Grass regrowth and moisture evaporation/retention resolve by biome/season
  -> Hunger and fertility counters update
  -> Next card set is prepared
```

### Macro Loop (Seasonal migration across 4 biomes -> Roguelike upgrades/God powers)
```text
[Run Start]
  -> Select starting god powers (2 active + 1 passive)

[Seasonal Arc]
  -> Wet -> Early Dry -> Dry Peak -> Storm Return

[4-Biome Migration]
  -> River Crossings -> Open Grassland -> Acacia Belt -> Marsh Delta
  -> Complete each biome's migration objective + ecological stability check

[Between-Biome Upgrade Draft]
  -> Pick 1 of 3 roguelike upgrades:
     - Rain deck mutation
     - Herd adaptation
     - Predator management utility

[Run End]
  -> Win: complete all 4 biomes with ecological balance intact
  -> Lose: any collapse condition reached (herbivore extinction, predator starvation collapse, or biome desertification)
```

## 3) Interaction Schema: Input/Feedback Mechanics

### Input Model
- **Pointer/Cursor**: inspect tiles, route risk, and fertility state.
- **Card Choice**: select one rain tetromino from three options each turn.
- **Placement Controls**: rotate/flip/confirm geometric placement.
- **Guidance Tools**: place soft route beacons to bias herd movement decisions.
- **God Powers**: trigger limited interventions (cooldowns + seasonal charges).

### Feedback Channels
- **Visual Feedback**:
  - Placement legality highlight (valid/invalid cells).
  - Grass vitality heatmap and moisture layer.
  - Herd migration trails with volume-weighted thickness.
  - Predator threat overlay and ambush vectors.
- **Audio Feedback**:
  - Warning cues for overhunting, drought stress, and predator starvation.
  - Biome ambience intensity tied to ecosystem health.
- **UI/System Feedback**:
  - Core meters: Herbivore Population / Predator Stability / Biome Fertility.
  - Turn-end delta report explaining gains/losses and causes.
  - Event ticker with actionable alerts.

### Interaction Constraints, Edge Conditions, Fail States
- Rain placement invalid on blocked landmarks or out-of-bounds cells.
- If no legal placement exists, one seasonal redraw is allowed; further deadlock forces penalized auto-place.
- Beacons cannot route through impassable tiles.
- God powers cannot ignore hard collapse thresholds once triggered.
- Fail states:
  1. Herbivore population falls below extinction threshold.
  2. Predator starvation instability persists beyond collapse limit.
  3. Biome fertility remains under desertification threshold for defined consecutive turns.

## 4) Functional Modules

| Module Name | Category | Responsibility Summary |
|---|---|---|
| Grid System | Core Gameplay | Owns grid topology, biome tile tagging, occupancy, and legal tetromino placement rules. |
| Tetromino Engine | Core Gameplay | Generates randomized rain shapes, handles rotation/flip rules, and applies placement effects. |
| Animal AI | AI | Computes herbivore safe-path movement and predator hunting pressure based on evolving map state. |
| Resource Manager | Simulation/Economy | Resolves grass regrowth, water state, hunger/fertility counters, and collapse threshold checks each turn. |
| Season & Biome Director | Progression | Advances seasonal phases and biome objectives while scaling environmental pressure. |
| God Power System | Core Gameplay | Manages active/passive divine abilities, cooldowns, charges, and effect execution. |
| Telemetry & UX Layer | UI/UX | Presents trails, heatmaps, warnings, and turn-resolution summaries for player readability. |
| Run Progression Manager | Progression | Handles between-biome upgrade drafts, win/loss state, and meta-unlock persistence. |

## 5) State Machine: Entity Transition Logic

### Primary Entities
1. Herbivore Herd
2. Predator Group (Lions/Crocodiles)
3. Ecology Tile Cell
4. Run State Controller

### 5.1 Herbivore Herd
- **States**: `Idle`, `Migrating`, `Grazing`, `Fleeing`, `Exhausted`, `Dead`
- **Transition Triggers/Guards**:
  - `Idle -> Migrating`: waypoint active and safe path score above minimum.
  - `Migrating -> Grazing`: reaches viable forage tile.
  - `Migrating -> Fleeing`: predator threat exceeds alert threshold.
  - `Fleeing -> Exhausted`: stamina depleted.
  - `Exhausted -> Grazing`: safety + recovery time satisfied.
  - `Any non-Dead -> Dead`: lethal hunt/starvation/disaster.
- **Invalid Transitions & Handling**:
  - `Dead -> any`: reject and log integrity event.
  - `Exhausted -> Migrating` without recovery: block and re-evaluate next tick.

### 5.2 Predator Group
- **States**: `Patrolling`, `Stalking`, `Feeding`, `Starving`, `Collapsed`
- **Transition Triggers/Guards**:
  - `Patrolling -> Stalking`: herd density enters hunt radius.
  - `Stalking -> Feeding`: successful hunt event.
  - `Feeding -> Patrolling`: satiation timer completes.
  - `Patrolling/Stalking -> Starving`: hunger counter crosses threshold.
  - `Starving -> Patrolling`: successful feed.
  - `Starving -> Collapsed`: starvation persists N turns.
- **Invalid Transitions & Handling**:
  - `Collapsed -> any`: reject; contributes to run-loss evaluation.

### 5.3 Ecology Tile Cell
- **States**: `Barren`, `Recovering`, `Fertile`, `Overgrown`, `Flooded`, `Desertified`
- **Transition Triggers/Guards**:
  - `Barren -> Recovering`: rain effect applied.
  - `Recovering -> Fertile`: regrowth timer completes.
  - `Fertile -> Overgrown`: sustained moisture + low grazing pressure.
  - `Fertile/Overgrown -> Barren`: high grazing + moisture deficit.
  - `Any non-Desertified -> Flooded`: storm surge/flood event.
  - `Flooded -> Recovering`: water recession completes.
  - `Barren -> Desertified`: depletion threshold sustained for N turns.
- **Invalid Transitions & Handling**:
  - `Desertified -> Fertile` direct jump blocked; must pass staged restoration.

### 5.4 Run State Controller
- **States**: `Planning`, `Resolution`, `UpgradeDraft`, `BiomeComplete`, `RunWon`, `RunLost`
- **Transition Triggers/Guards**:
  - `Planning -> Resolution`: player confirms card placement/actions.
  - `Resolution -> Planning`: turn resolved, biome objective not yet complete.
  - `Resolution -> UpgradeDraft`: biome objective and stability check complete.
  - `UpgradeDraft -> BiomeComplete`: upgrade confirmed.
  - `BiomeComplete -> Planning`: next biome initialized.
  - `Any active state -> RunWon`: all 4 biome goals complete with balance intact.
  - `Any active state -> RunLost`: collapse condition reached.
- **Invalid Transitions & Handling**:
  - `RunWon/RunLost -> any` blocked except new run initialization.

### QA Acceptance Intent (Design-Level)
- Micro-loop always resolves in fixed order: card -> placement -> movement -> recovery.
- Player can identify collapse causes via telemetry and event feed.
- Win requires co-survival of herbivores and predators plus viable fertility.
- All four biomes are traversed unless early collapse ends the run.
