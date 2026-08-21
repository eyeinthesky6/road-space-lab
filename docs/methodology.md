# Empirical methodology v0.1

## Question

Given the same road segment and observed traffic trajectories, which representation best explains/predicts usable capacity and safety: fixed vehicle equivalents, dynamic equivalents, vehicle area, or a richer two-dimensional dynamic-space representation?

## 1. Canonical trajectory schema

Minimum fields when available:

- `dataset`, `site_id`, `vehicle_id`, `timestamp_s`
- `vehicle_class`
- `x_m`, `y_m`
- `length_m`, `width_m`
- `speed_mps`
- `accel_long_mps2`
- `velocity_lat_mps`, `accel_lat_mps2`
- road/region identifiers, signal phase and direction if available

Optional but important:

- observed occupancy / passenger count
- taxi/commercial state (occupied, empty, unavailable, unknown)
- lane/virtual-lane assignment
- vehicle heading

Never infer unavailable occupancy/deadheading fields as facts. Use explicit scenario ranges.

## 2. Observed, minimally modelled descriptors

For each vehicle/window:

- physical footprint `L × W`;
- time headway at virtual lines;
- lateral excursion `P95(y)-P05(y)` after coordinate normalisation;
- path tortuosity;
- lateral speed/acceleration distributions;
- longitudinal acceleration/deceleration distributions;
- queue discharge rate;
- density/flow/speed by region/time window;
- TTC, PET and conflict/deceleration measures where definable.

## 3. Model ladder

### M0 — Fixed PCU/PCE
Use published/manual values appropriate to facility where possible. Purpose: practical legacy baseline.

### M1 — Dynamic PCU
Estimate contextual PCU/equivalents from observed speed, area, headway/clearance and composition methods in literature. Report confidence/distribution, not only a scalar.

### M2 — Static/areal variables
Compute vehicle plan area, areal density and areal flow. Reproduce Maiti & Chilukuri before extending it.

### M3 — 2-D dynamic space
Candidate dynamic-area definitions:

1. physical rectangle only;
2. data-derived longitudinal/lateral interaction envelope;
3. territory/Voronoi-like local allocation;
4. interaction zone from a validated 2-D model.

For a vehicle `i`, experimental Road-Space-Time is:

`RST_i = integral A_dynamic_i(t) dt`

No candidate definition becomes canonical until it improves an explicit benchmark.

### M4 — Safety/productivity overlay
Report capacity together with TTC/PET/deceleration/conflict indicators. Separately compute person throughput when occupancy is known, and passenger/productive movement when commercial state is known.

## 4. First experiment: SPT Chennai

1. Obtain dataset under its stated terms; record checksum/version/license.
2. Normalize coordinates and vehicle classes without smoothing away lateral movement.
3. Choose repeatable spatial windows/virtual lines.
4. Calculate observed class distributions and kinematics.
5. Reproduce fixed/dynamic PCU baselines.
6. Reproduce areal variables/model.
7. Add lateral descriptors and candidate RST.
8. Compare prediction/explanation of queue discharge, flow-density state and speed collapse.
9. Add surrogate safety metrics.
10. Bootstrap by time window/vehicle sample; report uncertainty.

## 5. Cross-dataset test

Run the same pipeline on:

- SPT Chennai — disordered Indian traffic;
- pNEUMA Athens — dense European urban traffic with motorcycles/taxis;
- NGSIM — lane-disciplined US control;
- inD/highD where licensing allows.

A metric that only works on one camera/site is not a general road model.

## 6. 'Smaller vehicles increase capacity' experiment

Do not compare photographs. Compare four distinct quantities:

1. **queue storage** (standstill);
2. **vehicle throughput** at a bottleneck;
3. **person throughput** using occupancy observations/sensitivity;
4. **safety-adjusted/productive movement**.

Estimate capacity elasticity to physical area:

`E = (% change in capacity) / (% reduction in projected area)`

If `E≈1` robustly, footprint is close to proportional. If `E<<1`, shrinking footprint produces much smaller capacity gains. If `E>1`, operational effects amplify the geometry. There is no need to predetermine the sign.

## 7. Motorcycle 'wobble'/disturbance hypothesis

Avoid a made-up chaos multiplier. Operationalize progressively:

- lateral excursion;
- lateral speed/acceleration;
- path tortuosity;
- close-neighbour response within a defined time/distance window;
- hard-braking/evasive events;
- TTC/PET changes before/after a subject manoeuvre.

A Disturbance Propagation Index is **provisional** until event detection and causal attribution are validated. Correlation is not automatically propagation.

## 8. Taxi/deadheading hypothesis

Definitions:

- empty-VKT share `e = empty_VKT / total_VKT`;
- total-km per occupied-km identity `1/(1-e)`;
- occupied passenger-km;
- road-space-time split by occupied/empty state where state data exist.

Use strike/natural-experiment literature for causal context, but do not infer empty state from vehicle appearance in ordinary trajectory datasets.

## 9. Evaluation

For each model/metric report:

- fit and held-out prediction error;
- stability across traffic density/composition/site;
- calibration burden;
- interpretability;
- data requirements;
- conservation/physical consistency where relevant;
- runtime;
- safety/productivity blind spots.

Prefer the simplest method that survives the benchmark.
