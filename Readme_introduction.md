# ⚙️ Arrowhead Core Docker Demo (Fixed Version)

This repository contains a **corrected and improved version** of the Eclipse Arrowhead Core setup using Docker Compose. The goal is to deploy a working instance of Arrowhead Core systems for **demo/testing purposes** in a simplified environment.

> ⚠️ This setup currently runs in **non-secure mode**. Secure mode with TLS and certificate validation is disabled until fully configured.

---

## ✅ What's Working

* All services build and run correctly in Docker using a shared `docker-compose.yml`.
* MySQL initializes correctly with Arrowhead-specific tables and test users.
* `.properties` files are fully updated to avoid networking and hostname issues.
* The system is suitable for testing **Service Registry**, **Orchestrator**, **Authorization**, and **EventHandler** flows.

---

## 🛠️ Fixes Applied

### 🔧 1. MySQL Initialization Error

**Problem:**

```bash
ERROR 1067 (42000): Invalid default value for 'updated_at'
```

**Cause:** Incorrect timestamp defaults in SQL scripts.

**Fix:**

* Adjusted the SQL schema or used compatible MySQL 8.0 settings.
* Ran `initSQL.sh` using **WSL** instead of Git Bash to avoid SSL and shell execution issues.

---

### 🔧 2. Docker Network Communication Issue

**Problem:**

```bash
Could not get any response from: https://127.0.0.1:8443/serviceregistry/echo
```

**Cause:** `127.0.0.1` (localhost) doesn't work between Docker containers.

**Fixes:**

* Replaced `127.0.0.1` in `.properties` and `docker-compose.yml` with service names:

  * `arrowhead-core` for internal service calls
  * `arrowhead-core-mysql` for DB host
* Ensured consistency across:

  * `domain.name`, `system.address`, `sr_address`

---

### 🔧 3. Container Naming and Configs

**Fixes:**

* Renamed containers from `snake_case` to `kebab-case` (`arrowhead_core` → `arrowhead-core`) for URI compatibility.
* Updated `MYSQL_HOST`, `spring.datasource.url`, etc.
* Confirmed MySQL connectivity via:

```bash
docker logs arrowhead-core-mysql
```

---

### 🔧 4. Added Demo Users

**Fixes:**

* Created `01-create-users.sql` for initializing essential system users (Orchestrator, Gateway, etc.).
* Placed the script in `./sql/` for auto-execution.
* Verified using:

```bash
docker exec -it arrowhead-core-mysql bash
mysql -u root -p
```

---

### ⚠️ 5. TLS & Hostname Verification Errors (Deferred)

**Issue:**

```bash
The certificate does not contain the specified IP address or DNS name...
```

**Temporary Handling:**

* Skipped secure services:

  * Gateway
  * Gatekeeper
  * Certificate Authority
* Disabled secure mode in `.properties` files:

```properties
# server.ssl.enabled=true
# server.ssl.client-auth=need
```

* Used certificates generated under `certificate_generation/`, but **not yet enabled**.

---

### 🔧 6. Startup Synchronization

**Fixes:**

* Replaced use of `wait-for-it.sh` with Docker-native `depends_on: condition: service_healthy` and added MySQL `healthcheck` block.
* Removed external dependency on `wait-for-it.sh` script.

---

## 🧪 What Still Needs Fixing

* Proper TLS configuration and `.p12` certificate linking.
* Secure mode activation with hostname validation.
* Launching `gateway`, `gatekeeper`, and `certificate-authority` modules.
* Organizing `certificates/` folder more cleanly (currently certificates copied manually).

---

## 📁 Structure Overview

```
├── docker-compose.yml
├── sql/
│   └── 01-create-users.sql
├── certificates/
│   └── *.p12 (from certificate_generation/)
├── properties/
│   ├── authorization.properties
│   ├── orchestrator.properties
│   ├── serviceregistry.properties
│   └── ...
```

---

## 👩‍💻 Maintained by

**Arash** – for academic demo & experimentation use 🚀

---

Let me know if you want this exported to a `.md` file ready to commit, or want to add badges/extra sections like contact or licensing.
