# Problem matrix: what exists, what we test, what we may add

This file is the project's guard against accidentally reinventing a published method — or claiming novelty where the literature already solved the problem.

| Problem | Existing serious work | What it already establishes | Road Space Lab treatment | Possible new contribution |
|---|---|---|---|---|
| Fixed PCU/PCE | HCM/Indo-HCM; Sharma & Biswas review; Alex & Isaac; dynamic-PCU reviews | Equivalence varies with facility, traffic composition, speed, geometry and interactions | Keep fixed PCU as M0 baseline; estimate contextual alternatives on the same data | Open out-of-sample benchmark showing when a fixed scalar is acceptable and when it fails |
| Different vehicle sizes | Speed-area PCU methods; areal occupancy; Maiti & Chilukuri 2026 | Physical area matters and can be a conserved macroscopic variable; static footprint alone is not necessarily a capacity law | Reproduce areal model before inventing a replacement | Capacity-area elasticity by regime; compare static area, areal flow and dynamic territory |
| Non-lane-disciplined traffic | Kanagaraj/Treiber particle model; 2-D LWR; Intelligent Agent Model; SUMO sublane model | Mixed traffic is genuinely 2-D; lateral motion cannot always be represented as lane changes between 1-D streams | Measure 2-D motion directly from SPT/pNEUMA; calibrate simulator only after observation | Common 2-D benchmark across Indian and lane-disciplined datasets |
| Motorcycle filtering/seepage | Hanoi/Japan motorcycle-equivalent literature; pNEUMA PTW filtering; SUMO sublanes | Motorcycles can exploit lateral gaps and materially raise raw vehicle throughput in some regimes | Treat this as evidence, not an inconvenience; separate vehicle throughput from persons and safety | Joint vehicle-capacity + person-capacity + conflict comparison using the same trajectories |
| Lateral instability / 'wobble' | 2-D models; lane-change/conflict research; motion-prediction; SSMsOnPlane | Lateral movement and neighbour responses are measurable, but no universal 'chaos factor' exists | Start with excursion, lateral velocity/acceleration, tortuosity, TTC/PET changes and hard-braking response | A disturbance-propagation metric only if it adds out-of-sample information beyond established SSMs |
| Braking / safety | FHWA SSAM; TTC, PET, DRAC/MTTC/PSD; 2-D SSM implementations | Capacity cannot be evaluated as safety; conflicts can be estimated from trajectories without waiting for crashes | Reuse established SSMs first; avoid made-up braking-distance constants where trajectories exist | Mixed-traffic interaction profiles by class and density |
| Queue storage | Classical geometry + observed standstill gaps | A smaller vehicle increases stationary storage, but gap and lateral packing matter | Keep as a simple calculator separate from moving capacity | Empirical Indian standstill-gap/packing distributions by class |
| Signal capacity / discharge | HCM/Indo-HCM, saturation-flow research, Indian dynamic PCU studies | Intersections are bottlenecks; discharge headway and green ratio dominate many capacity questions | Measure discharge at virtual lines; compare against static-area predictions | Demonstrate where citywide asphalt-area accounting breaks under network bottlenecks |
| Person throughput | TCQSM and transit-capacity literature | Vehicle flow and passenger flow are separate accounting layers | Never infer passengers from PCU; use observed occupancy or transparent sensitivity bands | Unified comparison of vehicle, person and productive movement under identical road-space conditions |
| Ride-hailing / taxi deadheading | Indian strike natural experiment; ridesourcing VKT/deadheading research; network equilibrium models | Empty cruising/pickup miles add traffic demand; Indian strikes show measurable congestion effects but mechanisms are mixed | Model occupied/empty states separately and never assume a universal empty share | Road-Space-Time split into occupied and empty commercial movement if suitable data can be obtained |
| Public transport argument | TCQSM; Rajkot road-space/person-efficiency work | High occupancy can yield high person throughput even with physically large vehicles | Keep transit person-capacity claims distinct from claims about physical vehicle footprint | Sensitivity analysis using actual occupancy, dwell, frequency, reliability and corridor constraints |
| Network capacity | LWR/CTM/MFD/network simulation; SUMO/UXsim/CityFlow | Network throughput is constrained by topology, bottlenecks, signals, route choice and spillback, not total asphalt area alone | Use a small network model after corridor-level metrics are validated | Compare aggregate-road-area heuristic against topology-aware prediction error |
| Ideal automated packing | TrafficFluid / lane-free CAV research | Coordinated automated vehicles can intentionally exploit 2-D road width very differently from human mixed traffic | Use as an upper-bound counterfactual, not evidence for present human traffic | Human-observed vs ideal-control 'coordination dividend' |

## Novelty standard

A Road Space Lab metric is not novel merely because it has a new name. Before promotion it must:

1. identify the closest prior metric/model;
2. reproduce that baseline;
3. state the additional observable it captures;
4. improve a pre-declared held-out prediction/description task or provide a clearly different accounting quantity;
5. remain interpretable enough for planners and practitioners.

If an existing method wins, Road Space Lab should expose and recommend it.
