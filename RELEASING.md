# Release checklist

Initial GitHub source publication was authorized by the maintainer on 2026-09-04. Tagged releases, official marketplace submission and production service tests are separate approvals. Intended repository: `everyinfra/everynumber-plugin`. Initial package version: `0.1.0`.

1. Review the exact file list, source provenance, license and public-facing claims.
2. Run `python3 scripts/validate.py`; validate the Codex plugin with the current official validator and the skill with the official quick validator. Validate the Claude manifest with the installed host when available.
3. Test a local installation in each host that will be advertised. A manifest parse is not runtime compatibility evidence. Verify discovery without paid operations; obtain approval before a paid service test.
4. Obtain approval for the exact public repository creation, initial commit and push. Apply only the approved description, topics and homepage in `repository-metadata.json`.
5. After publication, verify public README rendering, local document links, topics, description and actual clone/install flow. Remove the local-only publication notes only after those facts change.
6. Tag and publish a release only with approval. Validate the exact archive contents, exclude `.git`, credentials, local outputs and build artifacts, and record its checksum.
7. Request marketplace submission separately. Do not call an available GitHub repository an approved marketplace listing.

Each repository owns its skill and version independently. A change to the original all-in-one bundle does not automatically update this repository. Keep contract changes, tests and public documentation aligned. No runtime fetch of another repository is used.
