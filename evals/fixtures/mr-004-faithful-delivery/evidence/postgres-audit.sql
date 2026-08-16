-- PostgreSQL audit extract retained from the acceptance environment.
-- Source command: pg_dump --data-only --table=export_audit --column-inserts mission_ops

INSERT INTO public.export_audit (export_id, state, reason, recorded_at)
VALUES ('exp-42', 'stopped', 'permission denied', '2026-08-16 08:42:17+00');
