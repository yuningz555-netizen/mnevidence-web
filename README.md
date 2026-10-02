# MnEvidence: adsorption prediction and conditional screening

An English companion interface for literature-domain modeling of KMnO4-modified carbon sorbents. It uses frozen Bayesian XGBoost response backbones and the manuscript's mass-balance projection, support-distance calculation, and NSGA-III preference scores. The research ensemble's validation metrics are not per-input accuracy guarantees.

## Scientific scope

- Cd, Pb, Cu and Cr(VI): four audited screening scenarios, with uptake-forward, removal-forward and balanced preferences. Different preferences can select the same candidate.
- The remaining 15 represented metal labels: exploratory prediction only; no audited optimization scenario and no assurance of equal predictive reliability.
- Defaults reuse the archived candidate pool. Editing the fixed material or initial-concentration background reruns the same six-control, five-objective search: 210 reference directions, population 210, 100 generations, seed 20260808, and the 65th-percentile risk filter. No retraining occurs.
- Screening risk is a combination of support distance and response disagreement. It is not environmental safety, Mn-release or hazardous-waste risk.
- Outputs are conditional model estimates, not experimental validation, causal evidence, a digital twin, or a process controller.

## Release contents

`runtime.zip` contains readable backend/frontend source, the prebuilt frontend, two frozen models, sanitized context defaults, six-control development-support coordinates, the archived candidate pool, dependency notices, and regression tests. `release_manifest.json` records SHA-256 hashes. The model hashes are unchanged from the local paper companion.

The release excludes the manuscript, Supplementary Information, PDFs, the complete research database, source identifiers, internal adjudication notes, local logs, and personal launch paths. Only input fields required by the runtime and support calculation are retained. Experimental-series identifiers are replaced by their equivalent design-class tokens; all predictions are checked against the original runtime before release. The locked 260-row internal holdout is not used as support data.

This is a website-runtime release, not a deposit of every dataset underlying the manuscript. A permanent research archive and formal citation are separate tasks; no DOI or accession is asserted here.

## Run locally

Requires Python 3.10.18. On Linux x86_64, the pinned CPU-only XGBoost 3.0.5 package avoids installing unnecessary GPU libraries; other platforms use XGBoost 3.0.5.

```bash
python build.py
python -m pip install -r requirements.txt
python -m unittest discover -s tests
python production.py
```

Open `http://127.0.0.1:8781/`. `HOST` and `PORT` can override the default binding. Do not expose a local machine to the internet merely by changing these values.

The production server serializes screening requests and returns HTTP 429 with a retry notice when occupied. Prediction and profile requests remain available. User inputs are not deliberately stored by application code. Hosting-provider access/error logs and policies still apply; do not submit confidential experimental data.

## Free Render deployment

Create a Python **Web Service**, not a static site, from the public repository URL. Use the commands in `render.yaml`, Python 3.10.18, `/api/health`, and the **Free** instance. Do not add a payment method, paid disk, database, custom domain, or subscription. A platform-generated HTTPS address is sufficient.

Free instances sleep after inactivity, may take about a minute to wake, and have memory/CPU and monthly-usage limits. Edited-context optimization can be slower than the archived default scenarios. With no payment method, usage limits may suspend availability; they must not be addressed by upgrading without the owner's approval. A website is not a guaranteed permanent archival endpoint.

## Rights and attribution

Third-party dependencies retain their original licenses; see `THIRD_PARTY_NOTICES.md` and the notices inside the archive. No license is asserted for original literature PDFs or publisher content, which are not redistributed. No blanket open license is invented for the compiled research inputs or frozen models. Public availability of this release does not by itself grant unrestricted reuse rights; a formal code/model/data license requires the research owners' choice.

No published-article citation is assigned before the manuscript has a verified publication record. The model manifest, release hashes and software versions identify the present runtime.
