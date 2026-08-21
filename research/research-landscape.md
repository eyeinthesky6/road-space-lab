# Research landscape — what already exists and what is still missing

## Bottom line

Road Space Lab is **not** entering an empty field. There is substantial work on dynamic PCUs, motorcycle equivalents, two-dimensional mixed traffic, space-time use, areal flow, trajectory safety and ride-hailing congestion.

The opportunity is integration: one open, reproducible comparison layer that feeds the **same observed trajectories** through competing road-space/capacity/safety/productivity definitions and records where each works or fails.

## India

### Indo-HCM / CSIR-CRRI
India developed its own Highway Capacity Manual specifically because heterogeneous Indian conditions could not be handled cleanly by simply importing foreign procedures. The Indo-HCM development summary explicitly recognizes that PCU changes with factors affecting vehicle behaviour and uses field-derived dynamic methods in parts of the manual.

Source: https://crridom.gov.in/en/indian-highway-capacity-manual

### PCU reviews
Sharma & Biswas (2021) review urban-road PCU methods and find outcomes region-specific and inconsistent, including the trend of PCU versus governing factors. Ameena & Dhurai (2023) similarly review dynamic PCU methods for heterogeneous Indian traffic and list capacity, LOS, saturation flow and signal design among applications.

### Fully 2-D Indian mixed traffic
Venkatesan Kanagaraj and Martin Treiber model mixed traffic as disordered self-driven particles, explicitly motivated by varied dimensions/speeds and weak lane discipline. Later work extends this to 2-D macroscopic LWR and a general Intelligent Agent Model.

### Areal continuum (2026)
Maiti & Chilukuri introduce area-conserved macroscopic variables and validate on trajectory data from three Indian cities. This is probably the strongest modern alternative to PCU that Road Space Lab should benchmark first.

### SPT Chennai (2026)
The SPT dataset provides high-resolution disordered-traffic trajectories, including vehicle type and 2-D kinematics, extracted from coordinated drone recording on a Chennai arterial. It is the best initial empirical base for our lateral/dynamic tests.

### Rajkot road-space-time
Will, Cornet & Munshi (2020) propose a space-time approach to dynamic/on-road and parked space in Rajkot, motivated by the absence of a standard spatial-efficiency method for complex urban settings.

## Japan / motorcycle-dominated Asian traffic
Researchers associated with Nagaoka University of Technology developed dynamic Motorcycle Units using **effective space**, speed and surrounding motorcycles rather than only projected rectangles. Hanoi studies measured motorcycle speed, headway, deceleration and mixed-flow capacity.

Useful sources:
- Cao, Sano & Minh (2007), DOI 10.11175/easts.7.2439.
- Minh, Sano & Matsumoto (2005), DOI 10.11175/easts.6.1496.
- Cao & Sano (2012), DOI 10.1061/(ASCE)TE.1943-5436.0000382.

This literature is an important challenge to any claim that motorcycles consume the same road space as cars. It suggests motorcycles can materially increase *vehicle* throughput under some regimes — while still leaving person throughput, safety and context open.

## Europe

### pNEUMA / EPFL
Athens drone data contains more than half a million trajectories across 100+ intersections, including cars, taxis, buses and motorcycles. Follow-up work shows that the road's effective/active lane use can differ from painted lanes because of bottlenecks, stopping and powered-two-wheeler filtering.

Source: https://open-traffic.epfl.ch/

### Germany trajectory datasets
highD and inD provide high-quality drone trajectories for highways/intersections and are valuable orderly/lane-disciplined controls. Their licenses are not equivalent to unrestricted commercial data; verify before use.

### Dresden / Treiber group
The 2-D LWR, self-driven particle and Intelligent Agent Model work provides a mature theoretical comparison set for lane-free traffic.

## United States / Canada

### HCM/PCE is also not universal
PCE is not uniquely an India problem. Research on heavy vehicles during queue discharge found site-specific PCEs substantially different from the then-HCM values, illustrating that even lane-disciplined traffic can make fixed equivalence values context-sensitive.

### FHWA SSAM
SSAM turns trajectories into surrogate safety measures including TTC, PET, deceleration, speed differential and conflict type. This is exactly the kind of 'capacity plus safety' baseline Road Space Lab needs.

Source: https://highways.dot.gov/turner-fairbank-highway-research-center/software/ssam

### NGSIM
Classic FHWA trajectory data provides a lane-disciplined comparison/control against Indian disordered traffic.

## Ride-hailing and empty running

Agarwal, Mani & Telang (2023) use ride-hailing strikes in Mumbai, New Delhi and Bengaluru as exogenous shocks. Ride-hailing absence reduced travel times in all three cities, with the largest effects in the most congested areas/busy periods. The paper discusses mechanisms including elimination of deadheading, substitution to public transport and route effects.

This supports a **testable deadheading/productivity hypothesis**, not the claim that every taxi is the primary cause of congestion everywhere.

DOI: 10.1287/msom.2022.1158

## What appears genuinely under-integrated

We have not found one mature open project that combines all of the following:

1. fixed + dynamic PCU baselines;
2. area-conservation baselines;
3. fully 2-D trajectory behaviour;
4. road-space-time/influence territory;
5. lateral disturbance/interaction propagation;
6. TTC/PET/deceleration safety;
7. actual occupancy/person throughput;
8. empty/deadheading productivity;
9. cross-dataset benchmarking from India to lane-disciplined controls;
10. a license-aware public inventory of reusable road research/data/code.

That integration layer is Road Space Lab's best wedge.

## Research posture

- Do not call existing engineers 'dumb' in the project. Their own literature has documented limitations for decades.
- Do call out when a convenient engineering approximation is presented publicly as a universal physical law.
- Prefer measurements and out-of-sample error over rhetoric.
- Preserve inconvenient results. If motorcycles beat cars by 3× on raw vehicle throughput in a valid regime, publish it. Then separately evaluate person throughput, safety and useful movement.
