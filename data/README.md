# Data policy and source shortlist

## Do not upload giant datasets here

Trajectory/video datasets can be gigabytes and often have non-commercial or attribution restrictions. Keep raw data in `data/raw/` locally (gitignored) and commit only:

- source URL;
- version/date accessed;
- license/terms snapshot or reference;
- checksum;
- conversion script;
- derived small samples only when redistribution is explicitly permitted.

## Priority 1 — SPT Chennai

Official site: https://www.chennaitrafficdata.com/

Paper: *SPT: A multi-drone-based trajectory dataset for disordered traffic*, Transportation Research Part C (2026), DOI 10.1016/j.trc.2025.105431.

Why first: vehicle class + dimensions + longitudinal position/speed/acceleration + lateral position/velocity/acceleration. It directly supports the dynamic-space hypothesis without re-running computer vision.

**Action:** verify current download terms before adding any files.

## Priority 2 — pNEUMA, Athens

Official: https://open-traffic.epfl.ch/

More than half a million urban trajectories across 100+ intersections; vehicle types include car, taxi, bus, medium/heavy vehicle and motorcycle. Kinematic fields include speed and longitudinal/lateral acceleration.

**License warning:** EPFL pages have historically shown differing Creative Commons wording. Treat as `VERIFY BEFORE COMMERCIAL USE` until the exact dataset/version terms are recorded.

## Priority 3 — NGSIM, US FHWA

Use the authoritative USDOT/FHWA distribution where possible rather than a Kaggle mirror. Useful as a lane-disciplined control dataset.

## Priority 4 — inD / highD, Germany

Excellent drone trajectories for intersection/highway behaviour. Their standard research access is not equivalent to unrestricted commercial redistribution. Do not mirror into this repo.

## Indian perception/behaviour datasets

### MOTOR — IIIT Hyderabad / ICRA 2026
25+ hours of dense Indian two-wheeler riding with multi-view video and telemetry/behaviour signals. Valuable for manoeuvre/weaving classification rather than direct road-capacity measurement.

### IDD / I2WDD — IIIT Hyderabad INSAAN
Large Indian road-scene and two-wheeler datasets useful if/when we add raw-video trajectory extraction.

### IITM-HeTra — IIT Madras / RBC-DSAI (Kaggle)
Useful heterogeneous-traffic detection material with two-wheelers, cars, autos and heavy vehicles. Verify dataset/card license and upstream provenance before using any labels commercially.

## Kaggle policy

Kaggle is a discovery surface, **not provenance**. For every candidate:

1. find the original institution/source;
2. verify uploader rights;
3. record exact license;
4. prefer authoritative upstream distribution;
5. never treat `publicly downloadable` as `commercially reusable`.

See `resources/catalog.csv` for the growing inventory.
