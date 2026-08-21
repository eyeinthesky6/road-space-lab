# Road Space Index

**Open road traffic research, datasets, models, standards and tools — curated for traffic engineering, mobility, logistics, fleet, road safety and transport research.**

Road Space Index is the public resource directory inside [Road Space Lab](../README.md). It is designed to help practitioners and researchers quickly find trustworthy resources for questions such as:

- Where can I find **open traffic datasets** or **vehicle trajectory datasets**?
- What data exists for **Indian mixed traffic**, motorcycles, auto-rickshaws and weak lane discipline?
- Which **traffic simulation tools** support lateral movement, sublanes or lane-free traffic?
- What research exists on **Passenger Car Units (PCU/PCE)** and dynamic PCU methods?
- How can I measure **road capacity, queue discharge, headway, person throughput or road-space consumption**?
- Which tools calculate **TTC, PET, DRAC and surrogate traffic-safety measures** from trajectories?
- What evidence exists on **taxi / ride-hailing deadheading, empty vehicle kilometres and congestion**?
- Which datasets and models are actually reusable for commercial or consulting work?

The goal is not to become another giant link dump. Every resource should say **what it is useful for, where it applies, who produced it, what the access/license constraints are, and how confident we are in its provenance**.

## Browse by problem

| Problem / search area | Start here | Why it matters |
|---|---|---|
| Indian mixed-traffic trajectories | SPT Chennai | 2-D trajectories with vehicle dimensions plus longitudinal and lateral kinematics |
| Indian road-scene / two-wheeler data | IDD, MOTOR, IITM-HeTra, SIDDI | Perception, manoeuvre and heterogeneous-road datasets from Indian institutions |
| Vehicle trajectory datasets | SPT, pNEUMA, NGSIM, inD, highD, rounD, INTERACTION, CitySim | Compare traffic regimes instead of validating on one city only |
| Passenger Car Unit / PCU / PCE | Indo-HCM, dynamic-PCU reviews, Indian signal studies | Establish the conventional baseline before replacing it |
| Road-space / areal traffic models | Rajkot road-space study, Areal Continuum Model | Alternatives to treating every vehicle as a fixed passenger-car scalar |
| Lane-free / 2-D traffic | 2-D LWR, self-driven particle model, TrafficFluid | Models that explicitly represent lateral movement rather than only lane changes |
| Traffic simulation software | Eclipse SUMO, UXsim, CityFlow, TrafficFluid-Sim, Tactics2D | Reuse mature simulators instead of creating another one unnecessarily |
| Traffic safety from trajectories | FHWA SSAM, SSMsOnPlane, motion-prediction code | TTC, PET, DRAC, MTTC, PSD and interaction/conflict analysis |
| Taxi / ride-hailing congestion | Indian strike natural experiment + deadheading literature | Separate useful occupied movement from empty cruising and repositioning |
| Transit / person throughput | TCQSM + road-space/person-efficiency research | Keep passenger capacity distinct from raw vehicle throughput |
| Network bottlenecks | SUMO, UXsim, CityFlow, LWR/network models | Road networks are constrained by topology, signals, spillback and route choice — not total asphalt area alone |

## High-value starting resources

The machine-readable catalog currently tracks papers, standards, datasets, software and research code across India, the US, Europe and Asia. A few especially useful starting points:

### India and heterogeneous traffic

- **SPT Chennai** — primary Road Space Lab trajectory benchmark for disordered mixed traffic.
- **Indo-HCM / Indian Highway Capacity Manual** — official Indian capacity and PCU baseline.
- **Areal Continuum Model for Mixed Traffic** — 2026 alternative macroscopic formulation using vehicle area; accompanied by MIT-licensed research code.
- **IDD (Indian Driving Dataset)** — Indian road-scene perception dataset.
- **MOTOR** — Indian motorized two-wheeler rider/manoeuvre dataset.
- **IITM-HeTra** — heterogeneous Indian vehicle imagery surfaced through Kaggle; provenance/license checked separately before reuse.

### International comparison datasets

- **pNEUMA** — dense urban trajectories including motorcycles and taxis.
- **NGSIM** — classic FHWA lane-disciplined trajectory dataset.
- **inD / highD / rounD** — drone-derived European intersection/highway/roundabout trajectories.
- **INTERACTION** — multi-agent interaction trajectories across several countries.
- **CitySim** — trajectory and safety-critical interaction dataset.

### Open traffic software and research code

- **Eclipse SUMO** — mature microscopic/intermodal simulator with a sublane model useful for motorcycles and lateral interaction.
- **TrafficFluid-Sim** — automated lane-free 2-D traffic counterfactual built on SUMO.
- **UXsim** — compact MIT-licensed Python network traffic simulator.
- **CityFlow** — city-scale traffic simulation and traffic-signal research platform.
- **SSMsOnPlane** — MIT-licensed 2-D surrogate-safety metrics from trajectory data.
- **Areal Continuum Model implementation** — MIT-licensed code accompanying the published mixed-traffic model.

## What makes this index different

Existing public lists are often excellent but narrow: for example, some focus only on trajectory datasets, autonomous-driving perception, traffic forecasting or one simulator ecosystem. Road Space Index intentionally connects **traffic-flow theory + real trajectories + safety + person throughput + commercial vehicle productivity + simulation + licensing**.

That means a logistics operator, mobility startup, planner, transport consultant or researcher should be able to start from a real question — *"Do motorcycles increase useful road capacity?"*, *"How much road demand is empty taxi movement creating?"*, *"Which dataset contains lateral acceleration?"* — and find the relevant evidence and tools without already knowing the academic vocabulary.

## Inclusion rule

Each entry should record:

- authoritative source/provenance;
- institution/authors and geography;
- what problem it solves;
- road/traffic regime;
- whether it contains code, data, a model, a standard or only a paper;
- license/access and commercial-use status;
- how Road Space Lab plans to use it;
- whether it has been reproduced/validated here.

## Status vocabulary

- `priority` — directly useful to the first benchmark;
- `baseline` — established method/standard we must compare against;
- `benchmark` — an external method to reproduce;
- `review` — promising, but license/provenance/technical fit still needs inspection;
- `reference` — important context, not necessarily reusable code/data.

## License rule

A GitHub repository, Kaggle page or downloadable PDF is **not automatically reusable**. Preserve upstream licenses and cite original authors. When the source is ambiguous, catalog it as `VERIFY`; do not vendor it.

## Files

- [`catalog.csv`](catalog.csv) — machine-readable Road Space Index.
- [`kaggle-screening.md`](kaggle-screening.md) — how we evaluate Kaggle and mirrored datasets.
- [`reuse-plan.md`](reuse-plan.md) — what we plan to wrap, reproduce or benchmark rather than rebuild.
- [`../research/problem-matrix.md`](../research/problem-matrix.md) — maps each problem to existing serious research and remaining gaps.

## Search terms covered naturally by this project

Road traffic datasets, traffic engineering datasets, Indian traffic dataset, mixed traffic modelling, heterogeneous traffic, vehicle trajectory data, motorcycle traffic, two-wheeler traffic, auto-rickshaw traffic, Passenger Car Unit, PCU, PCE, dynamic PCU, road capacity, saturation flow, queue discharge, traffic simulation, SUMO, lane-free traffic, 2-D traffic modelling, road-space consumption, person throughput, transport capacity, taxi deadheading, ride-hailing congestion, traffic conflicts, TTC, PET, surrogate safety measures, traffic camera analytics, logistics traffic data and road safety research.

## Contribute

Found a strong dataset, paper, standard or open-source traffic tool that is missing? Open an issue with the canonical source, institution/authors, license/access terms and the problem it helps solve. High-quality corrections are as valuable as new links.
