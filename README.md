# MnEvidence: adsorption prediction and conditional screening

An English companion interface for literature-domain modeling of KMnO4-modified carbon sorbents. It uses frozen Bayesian XGBoost response backbones and the manuscript's mass-balance projection, support-distance calculation, and NSGA-III preference scores. The research ensemble's validation metrics are not per-input accuracy guarantees.

Live application: https://15569.pythonanywhere.com/

The 3 October 2026 release uses the revised 1,296-row research dataset and new frozen response backbones. Its 10-fold out-of-fold research ensemble results are R² = 0.911 (uptake) and 0.890 (removal); these figures are not accuracy guarantees for individual website inputs. The local release was checked against its source runtime on 119 prediction cases, 12 strategy representatives, 20 conditional profiles, and an edited-context NSGA-III run. Cross-platform cloud verification is reported separately after deployment. Runtime comparisons allow only small floating-point differences.

## Scientific scope

- Cd, Pb, Cu and Cr(VI): four audited screening scenarios, with uptake-forward, removal-forward and balanced preferences. Different preferences can select the same candidate.
- The remaining 15 represented metal labels: exploratory prediction only; no audited optimization scenario and no assurance of equal predictive reliability.
- Defaults reuse the archived candidate pool. Editing the fixed material or initial-concentration background reruns the same six-control, five-objective search: 210 reference directions, population 210, 100 generations, seed 20260808, and the 65th-percentile risk filter. No retraining occurs.
- Screening risk is a combination of support distance and response disagreement. It is not environmental safety, Mn-release or hazardous-waste risk.
- Outputs are conditional model estimates, not experimental validation, causal evidence, a digital twin, or a process controller.

## Release contents

`runtime.zip` contains readable backend/frontend source, the prebuilt frontend, two frozen models, sanitized context defaults, six-control development-support coordinates, the archived candidate pool, dependency notices, and regression tests. `release_manifest.json` records SHA-256 hashes. The model hashes match the current local paper companion, not the superseded 2 October release.

The release excludes the manuscript, Supplementary Information, PDFs, the complete research database, source identifiers, internal adjudication notes, local logs, and personal launch paths. Only input fields required by the runtime and support calculation are retained. Experimental-series identifiers are replaced by their equivalent design-class tokens; all predictions are checked against the original runtime before release. The locked 259-row internal holdout is not used as support data.

This is a website-runtime release, not a deposit of every dataset underlying the manuscript. A permanent research archive and formal citation are separate tasks; no DOI or accession is asserted here.

## Run locally

Requires Python 3.10 (cloud-tested on 3.10.12). On Linux x86_64, the pinned CPU-only XGBoost 3.0.5 package avoids installing unnecessary GPU libraries; other platforms use XGBoost 3.0.5.

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

Some new Render accounts can require card verification even when the Free instance is selected. Stop rather than adding a card when no-payment-method hosting is required. This account's initial deployment encountered that requirement; no Render service or payment method was created.

## PythonAnywhere free deployment

The Beginner account provides one web application on a platform-generated domain, one worker and 512 MB storage. Use a Python 3.10 virtual environment, install the pinned requirements with pip's cache disabled, extract the archive with `python build.py`, and run the tests. Configure a **manual WSGI application** using `pythonanywhere_wsgi.py` rather than running a persistent console server. The frozen models, input transforms and search rules remain the same.

The application does not need outbound network access at runtime. Dependency installation uses official PyPI packages. Free-account resource limits and periodic renewal/confirmation requirements still apply; do not upgrade, add payment details or assume permanent availability. Only claim a working public website after actual cloud prediction tests pass.

The dashboard's storage percentage is server filesystem usage, not browser local storage. At the pre-update check, the virtual environment used about 427 MB and the site directory about 55 MB. The browser stores only the selected light/dark theme. API responses and HTML entry pages use `Cache-Control: no-store`; built static assets have versioned filenames. Clearing the browser theme cannot free server storage.

The current Beginner plan is $0/month with no payment method. Its 100 CPU-seconds/day allowance applies to consoles and tasks, not web applications ([official explanation](https://www.pythonanywhere.com/tarpit/)). The web application has one worker and low bandwidth, so it is suitable for a low-traffic research companion, not an unlimited service. Log in at least monthly and click **Run until 1 month from today** on the Web page; the initial expiry is 2 November 2026. Policies and availability can change. In the measured deployment, a prediction took about 0.37 seconds including network round trip and an uncached edited-context search took about 11.7 seconds; these are observations, not response-time guarantees.

## Rights and attribution

Third-party dependencies retain their original licenses; see `THIRD_PARTY_NOTICES.md` and the notices inside the archive. No license is asserted for original literature PDFs or publisher content, which are not redistributed. No blanket open license is invented for the compiled research inputs or frozen models. Public availability of this release does not by itself grant unrestricted reuse rights; a formal code/model/data license requires the research owners' choice.

No published-article citation is assigned before the manuscript has a verified publication record. The model manifest, release hashes and software versions identify the present runtime.
