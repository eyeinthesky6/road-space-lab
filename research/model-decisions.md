# Model decisions: retain, upgrade, benchmark or drop

Road Space Lab exists partly to make modelling decisions auditable.

| Method/assumption | Decision | Why |
|---|---|---|
| Fixed PCU/PCE table | **Retain as baseline, not truth** | Widely used and useful for comparison, but literature and Indo-HCM itself recognize context sensitivity |
| Dynamic PCU | **Retain and reproduce** | Directly addresses traffic composition/speed/geometry variation; still compresses behaviour to a scalar |
| Static body footprint `L*W` | **Retain for parking/physical occupancy** | Real physical quantity, but incomplete moving-capacity model |
| Universal “m² per moving vehicle” | **Drop as standalone capacity claim** | Requires hidden speed/headway/lateral-allocation assumptions |
| Vehicle-area conservation / areal flow | **Priority benchmark** | Strong 2026 alternative with published code and Indian empirical validation |
| Full stopping distance treated as permanent road slot | **Drop as primary capacity model** | Follower/leader braking partly cancels; observed headway is preferable for flow; braking remains relevant to safety/conflict analysis |
| Pure one-dimensional car-following for disordered traffic | **Insufficient alone** | SPT and 2-D research explicitly capture lateral movement and non-lane behaviour |
| Made-up motorcycle/Indian “chaos factor” | **Reject** | Replace with observed lateral motion, neighbour gaps, evasive responses and safety metrics |
| Universal motorcycle=0.25 PCU | **Reject as universal constant** | Published Indian dynamic PCU values vary strongly with traffic/geometric conditions |
| “Motorcycles save only 5–10%” | **Do not assume** | Lateral parallelism can create large raw vehicle-throughput gains; must be measured |
| Person throughput inferred from PCU | **Reject** | Occupancy is separate and must be observed or sensitivity-tested |
| Taxi appearance implies empty/occupied state | **Reject** | Ordinary trajectory video cannot reliably identify commercial state; use operational data/natural experiments or explicit scenarios |
| City road-area / per-vehicle-area = city capacity | **Reject as network model** | Ignores topology, signals, direction, bottlenecks and spillback |
| Safety collapsed into one weighted capacity score | **Defer** | First show throughput and safety metrics side by side; weights are policy choices |
| Raw YouTube/street images as first quantitative dataset | **Deprioritize** | Existing SPT/pNEUMA/NGSIM trajectories already remove CV extraction error for the first benchmark |
| SUMO/UXsim/TrafficFluid | **Reuse** | Mature open simulators cover different network/2-D counterfactuals; do not build another simulator |
