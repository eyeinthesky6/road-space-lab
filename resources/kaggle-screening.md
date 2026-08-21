# Kaggle screening — useful discovery, not automatic evidence

Kaggle is useful for finding Indian perception datasets quickly, but it mixes original institutional datasets, derivative copies, commercial samples and synthetic/unclear tables. Road Space Lab will not treat a Kaggle license badge as sufficient provenance when the uploader did not create the underlying data.

## Useful now / later

### IITM-HeTra — **keep**

- Kaggle: `deepak242424/iitmhetra`
- Origin: heterogeneous traffic captured from road monitoring cameras in Chennai; associated with IIT Madras / RBC-DSAI work.
- 2,400 sampled frames were labelled; 1,417 remained after quality screening.
- Useful classes include two-wheelers, LMVs, autos and heavy vehicles.
- Use: Indian vehicle detection if we later add raw-video ingestion.
- Not needed for Phase 1 because SPT already supplies trajectories.

### IDD derivative detections — **discover only; prefer official IDD**

Kaggle contains YOLO-formatted derivatives of IIIT Hyderabad's Indian Driving Dataset. These can save preprocessing time, but Road Space Lab should use the official IDD source and terms as provenance and verify whether a derivative's redistribution/license is compatible with upstream rights.

### Indian Traffic Sign / VQA datasets — **peripheral**

Several Kaggle datasets have clear CC0/Apache/CC-BY-SA labels and may be useful if Road Space Lab later expands into signs, road semantics or VLM road audits. They do not answer the current dynamic road-capacity hypotheses.

## Do not use as core evidence without provenance

### Generic 'Indian traffic violation' tables

High usability/download counts do not establish that individual rows came from an authoritative enforcement system. Prefer MoRTH/Parivahan or state-police sources and reproduce extraction.

### 'Ride safety' / congestion tables with unknown license or generated-looking fields

Do not use to make causal claims about Mumbai/Delhi taxis, crime, traffic or safety unless source methodology is independently established.

### Commercial image samples

DataCluster and similar vendors expose useful samples for vehicle/autorickshaw detection, but the full data are commercial and their Kaggle pages may mix sample-license wording with broader commercial terms. Catalog as a vendor option, not open research data.

## Screening checklist

For every Kaggle candidate record:

1. **Who created the underlying observations?**
2. **Is there an institutional/paper/original URL?**
3. **Does the uploader have redistribution rights?**
4. **Does the stated license apply to raw data, annotations, code, or only the Kaggle metadata?**
5. **Can we use it commercially if Road Space Lab later supports consulting/client work?**
6. **Can another researcher reproduce the download today?**
7. **Does it contain trajectories/measurements, or only images suitable for perception training?**

The default is **link, don't mirror**.
