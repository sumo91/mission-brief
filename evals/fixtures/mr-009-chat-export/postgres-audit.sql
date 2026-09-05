-- Synthetic retained PostgreSQL acceptance extract for the complete fixture population.
-- Query: SELECT order_id, state, recorded_at FROM export_audit ORDER BY order_id;
COPY export_audit (order_id, state, recorded_at) FROM stdin;
A	completed	2026-09-05 00:01:00+00
B	completed	2026-09-05 00:03:00+00
C	terminal_failure	2026-09-05 00:04:00+00
\.
