# Security and privacy

Review the changed attack surface and every trust boundary it crosses.

## Examine

- Authentication, session handling, identity binding, token lifecycle, and account-state assumptions.
- Authorization, resource ownership, tenant isolation, role checks, and indirect object references.
- Validation, normalization, canonicalization, encoding, and unsafe ambiguity at system boundaries.
- SQL, command, template, path, header, URL, log, and other injection paths.
- XSS, CSRF, CORS, SSRF, path traversal, unsafe redirects, deserialization, uploads, and file handling where applicable.
- Secret, credential, cookie, webhook-signature, and token storage or exposure.
- Privacy: unnecessary collection, overbroad responses, logs containing sensitive data, retention, and cross-user disclosure.
- Rate limits, replay protection, abuse resistance, brute force, enumeration, and denial-of-service amplification.
- Dependency or configuration changes that weaken defaults or expand privileges.
- Webhook and background-job authenticity, idempotency, and least privilege.

## Evidence standard

For a finding, identify the attacker or untrusted input, reachable path, missing or ineffective control, and concrete impact. Do not emit generic security advice without a path in the reviewed change. Treat safety controls and factual vulnerabilities as non-overridable even when a project rubric uses `replace`.
