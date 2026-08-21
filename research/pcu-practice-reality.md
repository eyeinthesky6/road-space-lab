# PCU/PCE in practice: what the field actually knows

## Short answer

Traffic engineers are not simply unaware that Passenger Car Units / Passenger Car Equivalents are contextual. The more accurate criticism is **abstraction leakage**: a context-calibrated engineering convenience can become a universal-looking scalar when it moves from research into manuals, spreadsheets, procurement studies, public claims or cross-city comparisons.

Road Space Lab should therefore **not replace one magic scalar with another**. It should expose the assumptions, calibration regime and uncertainty of every conversion.

## 1. Why PCU/PCE exists

Mixed traffic contains vehicles with very different size and operating characteristics. Capacity/LOS/signal calculations often need one common accounting unit, so a reference passenger car is used as an equivalence unit.

This is operationally convenient. It is not a claim that a motorcycle literally occupies one fixed fraction of a car's physical or dynamic road space in every context.

## 2. India already recognizes dynamic PCU

The CSIR-CRRI executive summary for development of the Indian Highway Capacity Manual explicitly says PCU is affected by factors influencing vehicle behaviour and describes field-data estimation of dynamic PCU for Indian roads.

Source: CSIR-CRRI, *Development of Indian Highway Capacity Manual (Indo-HCM)* executive summary.
https://crridom.gov.in/sites/default/files/news/Development-of-Indian-Highway-Capacity-Manual-Executive-Summary-15-04-2014.pdf

So our thesis is **not** “India uses one naive universal PCU everywhere.” The better question is how much information is lost when dynamic behaviour is compressed into a scalar and where that scalar is then reused outside its calibration regime.

## 3. Published Indian PCU values vary dramatically

Alex & Isaac (2015) modelled signalised mixed traffic under different approach widths, traffic compositions, speeds and flow ratios. Their reported two-wheeler PCU varied from roughly 0.05 to 0.24 across one composition experiment; buses varied roughly 2.20 to 3.90. Under a flow-ratio experiment, even the car reference varied substantially.

That is direct evidence against treating a class equivalence as an intrinsic physical constant.

Source: DOI 10.7708/ijtte.2015.5(2).09

## 4. Reviews say the same thing

Sharma & Biswas (2020) reviewed urban-road PCU estimation and found estimates are region-specific, with inconsistency not only in PCU ranges but even in how PCU changes with governing variables.

Source: DOI 10.1016/j.ijtst.2020.07.002

A later review of dynamic PCU methods again emphasizes variation with traffic and roadway conditions and notes PCU's widespread use in capacity analysis, LOS, saturation-flow/signal work and traffic-flow modelling.

Source: DOI 10.7770/safer-V12N-art769

## 5. The research frontier is already moving beyond PCU

Maiti & Chilukuri (2026) propose a vehicle-area-conservation continuum model for heterogeneous lane-free traffic, introducing areal density and areal flow and validating against trajectory data from Chennai, Surat and Guwahati.

Source: DOI 10.1016/j.physa.2026.131465
Code: https://github.com/tffnandan/areal_continuum_model

SPT Chennai (Rajput et al., 2026) provides long 2-D trajectories with vehicle size plus longitudinal and lateral kinematics specifically for disordered traffic, enabling models that do not need to reduce lateral behaviour to a fixed scalar.

Source: DOI 10.1016/j.trc.2025.105431
Data: https://www.chennaitrafficdata.com/

## 6. Where the real methodological risk appears

Road Space Lab will flag these as separate errors:

1. **Transfer error** — applying a PCU calibrated on one facility/composition/speed regime to another without validation.
2. **Category error** — using vehicle-equivalent capacity to infer person throughput.
3. **Geometry error** — assuming physical footprint reduction maps proportionally to moving capacity.
4. **Network error** — treating all city asphalt as one fungible reservoir of road space.
5. **Safety omission** — maximizing raw flow while ignoring conflict/risk changes.
6. **Productivity omission** — counting empty taxi/fleet movement as equivalent to occupied passenger movement.

## 7. Road Space Lab's proposed upgrade

Every model or conversion should eventually ship with a **model card** containing:

- intended question;
- facility type;
- traffic regime;
- calibration city/dataset;
- vehicle classes;
- required inputs;
- output unit;
- uncertainty/range;
- known invalid-use cases;
- closest competing model;
- evidence/reproduction status.

The output should be a model choice plus assumptions, **not one new universal Road Space Unit**.

## 8. Policy/industry implication

A planner, NGO, logistics company or transport consultant should be able to ask:

> “For this 8 m urban approach with 55% two-wheelers, weak lane discipline, a 90-second signal cycle and these observed headways, which capacity model is defensible?”

Road Space Lab should answer with several comparable estimates and show why they differ. That is a more useful public tool than merely publishing another table of PCUs.
