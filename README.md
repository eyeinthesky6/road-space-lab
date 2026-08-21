# Road Space Lab

**Measure roads as dynamic systems, not parking lots.**

Road Space Lab is an open research-and-software project for testing how much *usable moving-road capacity* different vehicles actually consume under real traffic conditions — especially heterogeneous, weak-lane-discipline traffic such as Indian cities.

The project does **not** begin with a conclusion that cars, motorcycles, buses, autos or taxis are inherently better. It begins with a measurement problem:

> Static vehicle footprint, fixed Passenger Car Units (PCU/PCE), vehicle throughput, person throughput, safety and useful mobility are different quantities. When may they be converted into one another, and when does doing so become misleading?

## What we are building

1. **Reference base** — papers, standards, datasets, open-source software and known limitations.
2. **Transparent calculator** — simple queue, headway, signal, braking, occupancy and deadheading calculations with every assumption exposed.
3. **Trajectory analytics** — longitudinal + lateral motion, effective dynamic space, weaving, braking, conflicts and interaction propagation.
4. **Model benchmark** — compare fixed PCU, dynamic PCU, speed-area methods, areal-flow models and fully 2-D traffic models against the same observed trajectories.
5. **Road-Space-Time experiments** — test whether a dynamic territory integrated through time is a useful complement to PCU and static-area measures.
6. **Person/productivity layer** — keep vehicle flow separate from actual occupancy, passenger-km and empty/deadheading vehicle-km.
7. **Road resource inventory** — a curated, license-aware directory of datasets, models, simulators, safety tools and research code.

## Why this exists

Traffic engineering already knows that PCU/PCE values are contextual. Reviews report large variation by traffic composition, road geometry, facility type, speed and driving culture. India’s own Indo-HCM work uses dynamic methods in several contexts. More recent research goes further: lane-free 2-D models and an areal continuum model attempt to avoid forcing heterogeneous traffic into a single fixed passenger-car equivalent.

The gap is less “nobody studied this” and more **the useful pieces are scattered**. Road Space Lab stitches them into one reproducible benchmark and asks the same questions across datasets and models.

## Core hypotheses — all falsifiable

See [`research/hypotheses.md`](research/hypotheses.md) for full definitions and failure criteria.

- **H1 — Footprint is insufficient:** static plan area alone is not a sufficient predictor of moving-road capacity.
- **H2 — Fixed PCU is contextual:** one vehicle-class scalar cannot reliably represent all facilities, densities and traffic compositions.
- **H3 — Traffic is 2-D:** lateral motion and multi-neighbour interaction materially affect effective road use in disordered traffic.
- **H4 — Vehicle flow ≠ person flow:** occupancy must be measured separately.
- **H5 — Empty running matters:** deadheading can consume capacity without producing occupied passenger movement.
- **H6 — Capacity and safety can diverge:** a configuration that raises vehicle throughput may worsen conflict risk.
- **H7 — Area may still be powerful:** modern area-conservation models are a serious benchmark, not something to dismiss.
- **H8 — Networks are bottlenecked:** citywide asphalt area divided by a per-vehicle area is not a network-capacity model.

## First benchmark

**SPT Chennai → same trajectories → competing models.**

We will calculate, from one empirical dataset:

1. fixed PCU/PCE burden;
2. dynamic PCU / speed-area burden;
3. areal density + areal flow;
4. trajectory-derived dynamic Road-Space-Time;
5. lateral instability and neighbour-response measures;
6. TTC/PET/deceleration safety measures;
7. vehicle throughput and person-throughput sensitivity separately.

Then we test which measures best explain observed queue discharge, speed collapse, density-flow relationships and conflict behaviour.

## Data strategy

We **do not commit large or restricted datasets into this repository**. `data/README.md` records authoritative download locations, licenses and usage notes. Primary candidates include:

- **SPT Chennai** — disordered mixed-traffic trajectories with longitudinal and lateral kinematics.
- **pNEUMA (Athens)** — >0.5M urban trajectories including motorcycles and taxis.
- **NGSIM (US FHWA)** — classic lane-disciplined trajectory control dataset.
- **inD / highD (Germany)** — drone-based intersection/highway trajectories; licensing must be respected.
- **MOTOR / IDD (IIIT Hyderabad)** — Indian two-wheeler manoeuvres and Indian road-scene data.
- **IITM-HeTra / other Kaggle mirrors** — useful supplementary perception datasets, subject to source/license verification.

## Reuse before reinvention

Candidate upstream tools/research code are catalogued under [`resources/`](resources/):

- **Eclipse SUMO** — microscopic/intermodal simulation and sublane modelling.
- **Areal Continuum Model** — open MIT-licensed research implementation accompanying Maiti & Chilukuri (2026).
- **FHWA SSAM** — trajectory-based surrogate safety measures (TTC, PET, deceleration, speed differential, etc.).
- **Traffic Intelligence / trajectory toolkits** — reuse where licensing and maintenance status fit.
- **pNEUMA tooling** — useful examples for urban trajectory processing/visualisation.

Road Space Lab should wrap or benchmark good upstream work rather than fork 200,000 lines of somebody else’s simulator.

## Minimal calculator

The initial Python module is deliberately dependency-free and transparent:

```python
from roadspacelab.metrics import (
    queue_storage,
    signal_capacity,
    deadheading_multiplier,
    person_throughput,
)

print(queue_storage(100, vehicle_length_m=4.0, standstill_gap_m=0.8))
print(signal_capacity(headway_s=1.9, green_s=45, cycle_s=90))
print(deadheading_multiplier(0.40))
```

These formulas are baselines, **not our final traffic model**. The point is to expose assumptions and replace them with observations where data exist.

## Repository map

```text
road-space-lab/
├── docs/                  methodology and metric definitions
├── research/              hypotheses, literature map, model lineage
├── resources/             datasets/repos/tools inventory
├── data/                  download manifests + licensing notes (no giant blobs)
├── src/roadspacelab/      transparent calculation/trajectory code
├── examples/              runnable scenarios
└── tests/                 sanity tests
```

## Scientific rule

Every proposed metric must answer four questions:

1. **What does it measure?**
2. **What observation/calculation produces it?**
3. **What assumptions does it require?**
4. **What result would show that it is useless or inferior to an existing model?**

No metric gets promoted because it supports our preferred story.

## Start here

- [`research/research-landscape.md`](research/research-landscape.md) — what has already been done.
- [`research/model-lineage.md`](research/model-lineage.md) — what we retain, upgrade or reject and why.
- [`resources/catalog.csv`](resources/catalog.csv) — machine-readable resource inventory.
- [`docs/methodology.md`](docs/methodology.md) — proposed empirical comparison protocol.

## License

Road Space Lab code and original project documentation are MIT licensed unless a file says otherwise. **Upstream papers, datasets and software keep their own licenses.** Listing a resource here does not relicense it.
