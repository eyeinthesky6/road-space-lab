# Phase 1 empirical benchmark runbook

This is the execution order for the first real Road Space Lab result.

## Objective

Test the **Proportional Footprint Hypothesis (PFH)** and competing PCU/area/2-D representations on the same Indian trajectory windows without tuning the preferred model to win.

## A. Freeze the questions before seeing results

Primary questions:

1. Does a reduction in body length/area produce a proportional increase in observed bottleneck throughput?
2. How much do observed time headways vary by vehicle class, speed, density and local composition?
3. Does effective lateral parallelism scale with physical width, or with a larger/smaller dynamic envelope?
4. Do fixed PCU values predict observed mixed-flow states as well as contextual/dynamic PCU?
5. Does the areal-flow model outperform PCU on macroscopic flow-density prediction?
6. Do lateral descriptors improve held-out prediction after headway/area variables are already included?
7. Do configurations with higher raw vehicle throughput also exhibit worse/better surrogate-safety metrics?

Secondary questions:

- How sensitive are person-throughput conclusions to observed/plausible occupancy?
- How much does productive mobility change under taxi/fleet empty-running sensitivity bands?

## B. Dataset acquisition

Primary: SPT Chennai, official source `https://www.chennaitrafficdata.com/`.

Before analysis record:

- download date/version;
- official access/redistribution terms;
- source URL;
- file names/sizes;
- SHA-256 checksums;
- coordinate conventions and sampling interval.

Do not commit restricted/large raw data to GitHub.

## C. Ingestion gate

Use `src/roadspacelab/spt.py` to normalize:

- vehicle id/class;
- timestamp;
- x/y;
- length/width;
- longitudinal speed/acceleration;
- lateral velocity/acceleration.

Reject the run if required fields are missing or units cannot be verified.

## D. Window definition

Define spatial windows/virtual lines **before** model fitting.

For each window save:

- x range and carriageway width;
- observation duration;
- direction;
- signal influence / midblock flag;
- class mix;
- mean/quantile speed;
- observed crossing count;
- observed front-to-front headway distribution;
- observed density/area occupancy.

Split windows into calibration and held-out sets by time/block rather than randomly mixing adjacent frames.

## E. Model ladder

### M0 — fixed PCU

Use published/manual values with exact source and facility scope. No silent substitutions.

### M1 — dynamic PCU

Implement at least one published speed-area / area-occupancy formulation and report class/context variation.

### M2 — areal model

Reproduce Maiti & Chilukuri's published areal-density/areal-flow calculations and, where practical, their MIT-licensed code/results.

### M3a — observed headway + physical width

`Q_hat = P * 3600/h * gamma`, with `P` based only on physical/declared allocation.

### M3b — observed headway + dynamic lateral envelope

Replace physical width with an empirically derived local effective width/territory.

### M4 — experimental Road-Space-Time

Only after M0–M3 are reproduced. Drop it if redundant.

## F. Core metrics

Report separately:

- vehicle throughput;
- queue discharge where applicable;
- speed/flow/density state;
- PCU/equivalence by context;
- body area;
- dynamic slot/territory area;
- lateral excursion/velocity/acceleration/tortuosity;
- TTC/PET/DRAC or other established surrogate-safety measures;
- person throughput sensitivity;
- productive movement sensitivity for commercial empty-running scenarios.

## G. PFH test statistic

For comparable regimes estimate:

`E_A = (% change in observed capacity) / (% reduction in body area)`

and separately:

`E_L = (% change in observed capacity) / (% reduction in body length)`

Do not pool unlike regimes merely to obtain one headline number.

Interpretation:

- `E≈1`: proportionality is a useful approximation in that regime;
- `0<E<<1`: size reduction yields a much smaller capacity response;
- `E≈0`: little/no capacity response;
- `E>1`: operational/lateral effects amplify the geometric change;
- `E<0`: smaller-body regimes are associated with lower capacity after controls.

## H. Validation

For every model report:

- held-out MAE/RMSE or appropriate likelihood/error;
- residuals by density/class mix;
- sensitivity to spatial window size;
- bootstrap confidence intervals;
- calibration parameters required;
- failure cases.

A simpler model wins if richer models do not improve held-out performance meaningfully.

## I. First publishable outputs

1. **Does a smaller vehicle create proportional road capacity? — an Indian trajectory benchmark**
2. **How variable is PCU in real mixed traffic?**
3. **Physical width vs dynamic lateral territory for cars, autos and two-wheelers**
4. **Vehicle throughput vs person throughput: why the same road can have different 'capacity' answers**
5. **Ride-hailing/empty-running scenario calculator** (separate from the SPT causal analysis)

## J. Stop conditions

Stop and revise the project if:

- SPT geometry/terms prevent reproducible use;
- Road-Space-Time is not identifiable from trajectories;
- a published method already dominates our proposed metric with lower complexity;
- results depend entirely on one arbitrary gap/envelope threshold.

A negative result is still a Road Space Lab result.
