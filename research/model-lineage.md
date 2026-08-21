# Model lineage: keep, upgrade, benchmark, drop

The objective is not to declare old traffic engineering stupid. Good researchers have challenged fixed equivalence factors for decades. The practical problem is that convenient scalar factors survive because planners need tractable tools.

## 1. Fixed PCU/PCE tables — KEEP AS BASELINE, NOT TRUTH

Passenger Car Unit / Passenger Car Equivalent converts heterogeneous flows into passenger-car equivalents. It remains useful for communication and many design procedures.

**Known problem:** reviews find values highly context-, region-, road- and method-specific. Indo-HCM development itself recognizes dynamic PCU behaviour.

**Road Space Lab treatment:** preserve fixed PCU as Model 0. Every newer method must beat it out-of-sample to earn complexity.

Key sources:
- Sharma & Biswas (2021), *Estimation of Passenger Car Unit on urban roads: A literature review*, DOI 10.1016/j.ijtst.2020.07.002.
- Ameena & Dhurai (2023), *Different methods for estimation of dynamic passenger car units – A review*, DOI 10.7770/safer-V12N-art769.
- CSIR-CRRI, *Development of Indian Highway Capacity Manual (Indo-HCM)* executive summary.

## 2. Dynamic PCU / speed-area methods — KEEP + REPRODUCE

Indian and Asian researchers have long estimated PCU/MCU from speed, physical area, effective space, composition and geometry.

**Upgrade:** report a distribution/function by regime rather than silently replacing one fixed scalar with another fixed scalar.

Sources:
- Alex & Isaac (2015), dynamic PCU at Indian signalised intersections, DOI 10.7708/ijtte.2015.5(2).09.
- Cao, Sano & Minh (2007), dynamic motorcycle unit/effective space, DOI 10.11175/easts.7.2439.
- Cao & Sano (2012), Hanoi motorcycle equivalent units, DOI 10.1061/(ASCE)TE.1943-5436.0000382.

## 3. Space-time consumption — KEEP + TEST ASSUMPTIONS

Will, Cornet & Munshi (2020) explicitly note the absence of a standard method for complex urban road-space use and propose a space-time framework applied to Rajkot.

**Upgrade:** use observed trajectory distributions instead of assuming one mean dynamic space per mode whenever possible; keep person occupancy separate and visible.

Source: DOI 10.5198/jtlu.2020.1526.

## 4. Areal continuum model — BENCHMARK SERIOUSLY

Maiti & Chilukuri (2026) replace class-aggregated/PCU continuum variables with conserved vehicle-area variables (areal density and areal flow) and validate on Indian trajectories.

This directly challenges a simplistic version of our initial intuition: **physical area can be a powerful macroscopic state variable even when static footprint is not a proportional capacity law.**

Road Space Lab should reuse/benchmark the authors' MIT-licensed code rather than reimplement it first.

- Paper DOI: 10.1016/j.physa.2026.131465
- Code: https://github.com/tffnandan/areal_continuum_model

## 5. Fully 2-D lane-free models — KEEP AS ADVANCED BASELINES

- Kanagaraj & Treiber (2018), self-driven particle model for mixed/disordered flows, DOI 10.1016/j.physa.2018.05.086.
- Agrawal, Kanagaraj & Treiber (2023), two-dimensional LWR model for lane-free traffic, DOI 10.1016/j.physa.2023.128990.
- Treiber & Chaudhari (2023/24), Intelligent Agent Model, arXiv:2310.16816.

These models already encode a core Road Space Lab idea: mixed traffic is genuinely two-dimensional rather than a line of differently sized rectangles.

## 6. Surrogate safety — REUSE, THEN EXTEND

FHWA SSAM converts trajectories into TTC, PET, deceleration, speed differential and conflict classifications. Current FHWA material notes that SSAM is mainly focused on conventional automobiles even though trajectory inputs can contain other modes.

**Road Space Lab treatment:** reproduce compatible safety surrogates and test whether mixed-traffic/lateral interaction needs additional metrics.

Source: https://highways.dot.gov/turner-fairbank-highway-research-center/software/ssam

## 7. Vehicle flow → person flow — SEPARATE LAYER

A PCU says nothing by itself about actual occupants. Road Space Lab will never infer person capacity from vehicle class without an explicit occupancy variable/distribution.

`person throughput = vehicle throughput × observed mean occupancy`

Full-seat hypothetical comparisons are valid scenarios, but not measurements of real occupancy.

## 8. Ride-hailing/deadheading — SEPARATE PRODUCTIVITY LAYER

Agarwal, Mani & Telang (2023) use Uber/Ola strikes in Mumbai, New Delhi and Bengaluru as natural experiments and find travel times fell when ride-hailing was unavailable, with the largest reductions in the most congested areas/busiest periods; deadheading elimination is one suggested mechanism.

Source: *Manufacturing & Service Operations Management* 25(3), DOI 10.1287/msom.2022.1158.

**Upgrade:** measure empty VKT and occupied passenger-km rather than assuming every commercial vehicle is empty or every private trip is socially optimal.

## 9. What we explicitly DROP

As general capacity models, unless proven for a narrowly defined context:

- `total city road surface / one m²-per-vehicle number`;
- a universal PCU/MCU attached to a vehicle type regardless of facility/regime;
- imported standstill gaps/headways where observed local distributions exist;
- static bounding-box area presented as dynamic road consumption;
- person-throughput claims without occupancy assumptions/data;
- capacity claims without simultaneous safety reporting.

These may remain useful toy calculations — but must be labelled as such.
