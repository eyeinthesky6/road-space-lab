# Upstream reuse plan

Road Space Lab should be an integration/benchmark layer, not another traffic simulator written from scratch.

| Need | Upstream first choice | Decision |
|---|---|---|
| Macroscopic mixed/lane-free benchmark | `tffnandan/areal_continuum_model` | **Reuse/reproduce**. MIT-licensed code accompanies the 2026 paper. Keep attribution and compare against our results before modifying. |
| Microscopic/network simulation | Eclipse SUMO | **Use externally**, do not vendor. Calibrate sublane/lateral behaviour from empirical Indian trajectories before treating simulation output as evidence. |
| 2-D surrogate safety | `Yiru-Jiao/SSMsOnPlane` | **Reuse/wrap**. MIT; already implements vectorised longitudinal and genuinely 2-D SSMs including TTC/DRAC/MTTC/PSD/TAdv/ACT/TTC2D. Do not rewrite these first. |
| Established safety reference | FHWA SSAM 3.0 | **Benchmark/interface**. Use TTC/PET/deceleration/conflict definitions as an established baseline; obey FHWA software terms. |
| Lateral interaction / motion prediction | `nsaunier/motion-prediction` | **Study/reproduce**. MIT code + data from published surrogate-safety research; useful for neighbour-interaction methodology. |
| Dense urban motorcycle/taxi trajectories | pNEUMA / EPFL | **Use dataset + study tools** after exact version license is recorded. |
| Indian disordered trajectories | SPT Chennai | **Primary empirical dataset**. No computer-vision rebuild required for Phase 1. |
| Lane-disciplined controls | NGSIM, inD, highD | **Cross-dataset validation** subject to source terms. |
| Raw Indian road-scene perception | IDD, IITM-HeTra, SIDDI | **Deferred** until a raw-video ingestion module is justified. |
| Two-wheeler behaviour classifier | IIIT-H MOTOR | **Deferred but valuable** for weaving/squeezing/behaviour labels. |

## Rule for copying upstream code

1. Prefer dependency/wrapper/submodule over copy-paste.
2. Record upstream commit/version.
3. Preserve license and attribution.
4. Add an adapter test showing the upstream result is reproduced before extending it.
5. If a project is stale but scientifically important, reproduce the formula from the paper in a clean-room module with citation rather than silently absorbing code.

## What Road Space Lab itself should own

The original value is the glue and evaluation layer:

- canonical trajectory schema;
- common spatial/time-window definitions;
- model adapters;
- cross-model/cross-dataset benchmark harness;
- Road-Space-Time experiments;
- lateral disturbance tests;
- person-throughput/productivity layer;
- model lineage/assumption registry;
- license-aware resource catalog;
- human-readable reports/calculator.
