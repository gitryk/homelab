# After Install

## PostgreSQL
```
podman exec -it postgres psql -U postgres
ALTER USER postgres WITH PASSWORD 'passwd';
CREATE USER gitea PASSWORD 'passwd2';
CREATE DATABASE gitea OWNER gitea;
```
