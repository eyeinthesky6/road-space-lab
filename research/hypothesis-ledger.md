# Hypothesis evidence ledger

This is a living scorecard. “Supported” means supported by current evidence/model logic, **not proven universally**.

| Hypothesis | Current status | What already supports/challenges it | What would change our mind next |
|---|---|---|---|
| H1 Static footprint is not a proportional moving-capacity law | **Theoretical support; empirical benchmark pending** | `q=3600/h` has no body length when observed headway is fixed; `q=3600v/(L+g)` gives length elasticity `L/(L+g)<1` for positive gap; width packing is thresholded | SPT/cross-dataset evidence showing capacity scales near-inversely with body area after controls |
| H2 Fixed PCU/PCE is too coarse | **Strongly supported as a universal claim** | Indo-HCM recognizes dynamic PCU; Indian signal study reports large context-dependent ranges; 2020 review finds regional and trend inconsistency | A single fixed class PCU matching contextual methods out-of-sample within predeclared tolerance |
| H3 Lateral and multi-neighbour behaviour matters | **Strong support that 2-D representation matters; capacity penalty sign is open** | SPT exists specifically for disordered/non-lane traffic; 2-D/lane-free models and SUMO sublanes model lateral interaction | Lateral/neighbour features fail to improve any held-out flow/safety task |
| H4 Vehicle throughput != person throughput | **Accounting identity** | Occupancy is a separate variable by definition | Decision impact may be small if occupancies are similar, but the quantities remain distinct |
| H5 Deadheading can impose material penalty | **Ride-hailing congestion effect supported; mechanism share unresolved** | Indian Ola/Uber strike natural experiments find lower congestion when service is disrupted; deadheading is one plausible mechanism | Direct Indian occupied/empty state data showing negligible empty movement or negligible network effect |
| H6 Capacity and safety may trade off | **Open** | Filtering can increase raw vehicle throughput; trajectory safety literature gives TTC/PET/conflict tools | Same regimes showing throughput gains with consistently equal/better safety surrogates |
| H7 Areal conservation may outperform PCU macroscopically | **Serious competing model** | 2026 model validated with Chennai/Surat/Guwahati trajectories and released code | Reproduction shows no predictive/conservation advantage over simpler baselines |
| H8 Aggregate road-surface division is not network capacity | **Strong theoretical support** | Network/corridor capacity depends on bottlenecks, signals, direction, spillback and topology | Aggregate-area heuristic matches topology-aware predictions across held-out cities/corridors |
| H9 Road-Space-Time adds useful information | **Experimental / no novelty claim yet** | Related space-time and territory concepts already exist | Drop/rename if redundant, unstable or inferior to existing areal/Voronoi measures |
| H10 Disturbance propagation can be measured robustly | **Open / highest risk** | Lateral acceleration, evasive motion and conflict trajectories are measurable | Drop if common-cause events and causal ambiguity make the index unreliable |

## One important change from the original argument

Road Space Lab will **not** try to prove that motorcycles can only improve capacity by 5–10%. Small vehicles can create additional lateral streams and may materially raise raw vehicle throughput. The experiment instead asks how much of that geometric advantage survives real headway, lateral interaction, safety and occupancy/productivity accounting.

That makes the project harder to accuse of reverse-engineering a preferred conclusion.
