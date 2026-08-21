# Falsifiable hypotheses

Road Space Lab is not a campaign for a vehicle type. Each claim below includes a result that would weaken or kill it.

## H1 — Static footprint is not a proportional capacity law

**Claim:** Reducing projected vehicle area by X% does not generally increase moving-road capacity by X%.

**Measure:** observed throughput/queue discharge against physical length/width and dynamic headway/lateral envelope.

**Falsifier:** across facilities and traffic regimes, capacity scales approximately inversely with projected plan area after controlling for signal state and demand.

## H2 — A fixed PCU/PCE is too coarse for heterogeneous urban traffic

**Claim:** equivalence varies materially with facility, density, composition, speed and interactions.

**Measure:** infer context-specific equivalence from identical trajectory windows, then compare variance and predictive error with fixed tables.

**Falsifier:** one class-level PCU performs as well out-of-sample as dynamic/contextual alternatives within a pre-declared tolerance.

## H3 — Lateral and multi-neighbour behaviour matters

**Claim:** in disordered traffic, longitudinal car-following alone misses material capacity/safety effects.

**Measure:** lateral excursion, lateral velocity/acceleration, path tortuosity, neighbour response, TTC/PET and hard-braking chains.

**Falsifier:** adding lateral/neighbour features does not improve out-of-sample explanation/prediction of throughput, speed collapse or conflict metrics.

## H4 — Vehicle throughput and person throughput must remain separate

**Claim:** vehicle-equivalent capacity cannot by itself answer how many people a corridor moves.

**Measure:** vehicles/hour × empirically observed occupancy distributions; report occupancy sensitivity when measurement is unavailable.

**Falsifier:** not really falsifiable as an accounting identity; the empirical question is whether occupancy differences are large enough to change decisions.

## H5 — Deadheading can impose a material congestion/productivity penalty

**Claim:** empty commercial VKT consumes road capacity without occupied passenger movement.

**Measure:** empty-VKT share, total VKT, occupied passenger-km, Road-Space-Time and time-of-day/location.

**Falsifier:** after controlling for demand substitution, empty-running share is negligible or has no meaningful relationship with network performance.

**Important:** do not assume an India-wide empty-running percentage. Measure it or run sensitivity bands.

## H6 — Capacity and safety may trade off

**Claim:** lateral filtering/seepage can raise raw vehicle throughput while also increasing conflict exposure or disturbance.

**Measure:** throughput alongside TTC, PET, deceleration, speed differential and interaction events.

**Falsifier:** higher-throughput mixed configurations consistently show equal/better safety surrogates at comparable demand and geometry.

## H7 — Area conservation may outperform PCU macroscopically

**Claim:** Maiti & Chilukuri's areal variables are a serious alternative baseline for lane-free mixed traffic.

**Measure:** predictive fit and conservation consistency of fixed PCU, dynamic PCU and areal-flow models on the same datasets.

**Falsifier:** areal variables provide no improvement or are less stable/predictive than simpler equivalents.

## H8 — Aggregate city road surface is not a network-capacity calculation

**Claim:** summing all asphalt area and dividing by one per-vehicle dynamic-area number ignores topology, directions, signals, bottlenecks and unused spatial capacity.

**Measure:** compare area-ratio predictions with observed bottleneck flows and network simulation.

**Falsifier:** aggregate-area accounting predicts corridor/network throughput across cities as well as topology- and bottleneck-aware models.

## H9 — Dynamic Road-Space-Time may be useful

**Provisional metric:**

`RST_i = integral A_dynamic_i(t) dt` in m²·s.

Candidate `A_dynamic` definitions will be benchmarked: physical rectangle, observed influence envelope, Voronoi/territory measures and model-derived interaction zones.

**Falsifier:** RST is unstable, non-identifiable, redundant with simpler variables, or does not improve relevant predictions.

## H10 — Disturbance propagation is measurable, but not yet defined

We hypothesize that an evasive lateral/longitudinal action by one road user can trigger a measurable response cascade in neighbours. A future Disturbance Propagation Index (DPI) must be event-defined, causally cautious and tested against existing safety/conflict metrics.

**Do not hard-code a 'chaos factor'.** If DPI cannot be made reliable, drop it.
