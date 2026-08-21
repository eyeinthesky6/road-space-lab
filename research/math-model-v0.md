# Road Space Lab mathematical model v0.2

**Purpose:** replace the vague claim “smaller vehicle = proportionally more road capacity” with explicit competing models that can be falsified using real trajectories.

This document deliberately separates **parking/queue storage**, **moving vehicle throughput**, **person throughput**, **safety**, and **productive mobility**. They are not interchangeable.

## 1. The proposition we are testing

A common implicit hypothesis is:

> If projected vehicle footprint falls by `r%`, usable moving-road capacity rises by approximately `r%`.

Call this the **Proportional Footprint Hypothesis (PFH)**.

Road Space Lab does **not** assume PFH is false. We test it against progressively richer models.

---

## 2. Static footprint

For vehicle length `L` and width `W`:

`A_body = L W`

This is relevant to parking and physical exclusion, but it does not itself specify moving capacity because it contains no speed, headway, lateral interaction, signal state or network topology.

## 3. Stopped queue storage

For a regular single-file queue of usable length `S`, vehicle length `L` and standstill gap `g_s`:

`N_stop = floor((S + g_s) / (L + g_s))`

This follows from:

`N L + (N-1) g_s <= S`

For regular side-by-side packing across width `B`, effective width `W_e` and lateral clearance `c`:

`P_stop = floor((B + c) / (W_e + c))`

A regular-grid upper/baseline estimate is then `N_stop * P_stop`.

**Important:** Indian signal queues can stagger, filter and interleave. The regular grid is therefore only a transparent baseline; observed 2-D queue density is preferable.

## 4. Moving longitudinal capacity: two boundary models

### 4.1 Time-headway-dominated stream

If observed front-to-front time headway is `h` seconds:

`q_h = 3600 / h`

Vehicle length does not appear. Therefore, **if empirical time headway remains unchanged after making the vehicle shorter, length reduction produces zero capacity gain.**

This is one boundary, not a universal behavioral law.

### 4.2 Constant-distance-gap stream

If speed `v` and net distance gap `g` are held fixed:

`q_g = 3600 v / (L + g)`

Now length matters, but less than proportionally whenever `g > 0`.

The local elasticity of capacity to a proportional *reduction* in length is:

`epsilon_L = L / (L + g)`

Hence:

`0 < epsilon_L < 1` for `g > 0`.

This is a useful mathematical result. Example: `L=4 m`, `g=12 m` gives `epsilon_L=0.25`. A small 10% length reduction therefore produces only about a 2.5% capacity increase near that operating point.

For a finite change from `L_0` to `L_1`:

`capacity_gain = (L_0 + g)/(L_1 + g) - 1`

At 30 km/h, `L_0=4.0 m`, `L_1=3.6 m`, `g=12 m`:

`capacity_gain = 2.56%`

The speed cancels from the percentage because it is held constant.

### What this proves — and what it does not

It proves that **even a very simple moving-space model does not imply proportionality between body length and capacity** once non-body spacing exists.

It does *not* prove that real drivers keep constant gaps. SPT/other trajectories determine which boundary is closer to observed behavior by vehicle class, speed and density.

## 5. Width is threshold-driven

For a carriageway width `B`, effective lateral allocation `W_e`, and lateral clearance `c`:

`P = floor((B + c)/(W_e + c))`

Raw cross-section capacity in a simplified independent-stream approximation is:

`Q = P * q * gamma`

where `gamma` is the usable signal/green fraction when applicable.

The floor operation matters: **a modest reduction in width can produce zero throughput gain until another parallel stream actually fits.** At the threshold, capacity can jump abruptly.

Therefore width-to-capacity response is not generally proportional either.

For lane-disciplined cars, `W_e` may effectively be the lane allocation rather than body width. For motorcycles in disordered traffic, `W_e` must be measured from actual lateral territory/interaction rather than assumed to equal body width.

## 6. Why motorcycles remain an empirical question

Motorcycles can exploit lateral gaps and create more parallel streams; Indian and international literature already shows PCU/equivalence is context-sensitive. Road Space Lab therefore does **not** hard-code either of these claims:

- “one bike is 0.25 cars”; or
- “bikes save only 5–10% capacity.”

The measurable decomposition is:

`Q_vehicle ~= P_effective * 3600/h_effective * gamma`

where both `P_effective` and `h_effective` come from observed trajectories for the traffic regime.

Then person throughput is calculated separately:

`Q_person = sum_k(Q_k * occupancy_k)`

and commercial productive throughput can additionally distinguish occupied from empty movement.

## 7. Reverse-engineering a dynamic-area claim

Suppose someone claims one moving vehicle consumes `A_d` square metres and implicitly allocates lateral width `W_a`.

Then longitudinal front-to-front slot is:

`s = A_d / W_a`

At speed `v`:

`h = s/v`

and therefore:

`q = 3600/h = 3600 v W_a / A_d`

So the **same `A_d` produces a different flow at every speed**. Area alone cannot specify moving capacity.

Example for `A_d=88 m²` and `W_a=3.5 m`:

- longitudinal slot = `25.14 m`;
- at 30 km/h, `h=3.02 s`, `q≈1,193 veh/h/stream`;
- at 50 km/h, `h=1.81 s`, `q≈1,989 veh/h/stream`.

This does not tell us which flow is “correct”. It reveals the hidden speed/headway assumption in the 88 m² number.

## 8. Dynamic road space from observations

For moving vehicle `i`, a simple observed slot candidate is:

`A_slot,i(t) = v_i(t) h_i(t) W_eff,i(t)`

`W_eff` is **not automatically body width**. Candidate definitions to benchmark are:

1. marked-lane allocation;
2. nearest-neighbour / lateral-clearance envelope;
3. clipped Voronoi territory;
4. model-derived interaction/influence zone.

Road-Space-Time remains experimental:

`RST_i = integral A_dynamic,i(t) dt`

We will drop it if it is unstable or adds no information beyond established area/flow variables.

## 9. Lateral instability and disturbance

Do not invent an “Indian chaos factor”. Measure:

- lateral excursion;
- lateral velocity and acceleration;
- path tortuosity;
- minimum lateral/longitudinal neighbour gaps;
- hard braking / evasive response after a subject manoeuvre;
- TTC, PET, DRAC/related surrogate-safety measures.

A future disturbance-propagation metric is allowed only if it adds out-of-sample information beyond established safety measures and is robust to common-cause braking (e.g. everyone reacting to the same signal).

## 10. Productive mobility and deadheading

Vehicle throughput is not useful-mobility throughput.

For a class with mean occupancy `o` and productive/occupied share `u`:

`Q_productive_person = Q_vehicle * o * u`

For private occupied travel, `u` is normally 1 because the driver is a beneficiary of the trip. For taxis/fleet vehicles, empty cruising/repositioning should be represented explicitly when data exist.

If empty-VKT share is `e`:

`vehicle_km / occupied_vehicle_km = 1/(1-e)`

This identity is not itself a congestion model; it quantifies the extra vehicle movement associated with empty operation.

## 11. Safety is not folded into one magic capacity number

Initially report a Pareto surface rather than inventing policy weights:

`(vehicle throughput, person throughput, productive movement, TTC/PET/conflicts, speed/reliability)`

A configuration that maximizes raw vehicles/hour is not automatically “better”.

## 12. Network capacity

`total city road area / m² per vehicle` is not a network-flow equation.

Network performance depends on bottlenecks, directionality, intersections, signal timing, spillback, route choice and demand. After corridor metrics are validated, Road Space Lab will use a topology-aware simulator (SUMO/UXsim baseline) for network tests.

## 13. Model ladder for the first real test

Use identical SPT Chennai windows:

- **M0:** published/fixed PCU baseline;
- **M1:** dynamic PCU / speed-area / area-occupancy methods;
- **M2:** Maiti & Chilukuri areal density/areal flow model;
- **M3:** observed 2-D headway + lateral territory descriptors;
- **M4:** optional RST candidate;
- **Overlay:** TTC/PET/deceleration + occupancy/productivity kept separate.

Pre-declare evaluation metrics and hold out windows. We do not tune M3/M4 until they “win”.

## 14. Immediate falsification tests in code

`tests/test_capacity.py` currently checks:

1. 88 m² cannot identify unique flow without speed;
2. positive moving gap mathematically makes length-capacity elasticity `<1` in the constant-gap model;
3. 4.0 m → 3.6 m with a 12 m moving gap yields only ~2.56% flow gain;
4. if measured time headway is fixed, shortening the vehicle gives 0% flow gain;
5. width reduction can give zero parallel-stream gain until a packing threshold is crossed;
6. stopped queue storage is much more sensitive to vehicle length/gap than the moving examples;
7. empty commercial movement is kept separate from productive person movement.

These are **unit tests of assumptions and mathematics**, not empirical proof of H1. The empirical proof/attack is the SPT benchmark.

## Research anchors

- CSIR-CRRI, *Development of Indian Highway Capacity Manual (Indo-HCM)* executive summary: recognizes dynamic PCU and says PCU changes with factors influencing vehicle behaviour. https://crridom.gov.in/sites/default/files/news/Development-of-Indian-Highway-Capacity-Manual-Executive-Summary-15-04-2014.pdf
- Alex & Isaac (2015), *Dynamic PCU Values at Signalised Intersections in India for Mixed Traffic*, DOI 10.7708/ijtte.2015.5(2).09 — reports large condition-dependent PCU ranges.
- Sharma & Biswas (2020), *Estimation of Passenger Car Unit on Urban Roads: A Literature Review*, DOI 10.1016/j.ijtst.2020.07.002 — finds regional/methodological inconsistency in PCU estimates.
- Maiti & Chilukuri (2026), *An areal continuum model for mixed traffic*, DOI 10.1016/j.physa.2026.131465 — vehicle-area-conservation alternative validated on Chennai, Surat and Guwahati trajectories.
- Rajput et al. (2026), *SPT: Obtaining long trajectory data of disordered traffic using a swarm of unmanned aerial vehicles*, DOI 10.1016/j.trc.2025.105431 — primary 2-D Indian trajectory benchmark.
- FHWA, *Surrogate Safety Assessment Model (SSAM)* — TTC/PET trajectory-safety baseline. https://highways.dot.gov/turner-fairbank-highway-research-center/software/ssam
- Eclipse SUMO Sublane Model — explicit lateral resolution, parallel two-wheelers, lateral gaps and encroachment. https://sumo.dlr.de/docs/Simulation/SublaneModel.html
- *Measuring road space consumption by transport modes* (Rajkot), DOI 10.5198/jtlu.2020.1526 — existing space-time/person-efficiency work.
- *The Impact of Ride-Hailing Services on Congestion: Evidence from Indian Cities*, DOI 10.1287/msom.2022.1158 — Indian strike natural experiments for ride-hailing congestion.
