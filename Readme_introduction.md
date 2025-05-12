This is a corrected version and applied fixes for arrowhead docker version 
****** Issues Encountered and Fixes *****(still need some fixes to run it)
1.	MySQL Initialization Error:
○ MySQL container exited due to an error:
○ ERROR 1067 (42000): Invalid default value for 'updated_at'
○ This happened during the execution of create_arrowhead_tables.sql.
○ The issue was resolved by manually modifying the SQL to explicitly define the default timestamp or adjusting MySQL startup settings if needed.
2.	Service Registry Connection Failure:
○ Arrowhead core logs showed:
○ Could not get any response from: https://127.0.0.1:8443/serviceregistry/echo
○ This was caused by using 127.0.0.1 (localhost) within containerized services, which does not work across Docker containers.
3.	Fixes Applied:
○ Replaced hardcoded IPs (like 127.0.0.1) with Docker service names (e.g., arrowhead-core, arrowhead-core-mysql).
○ Updated docker-compose.yml:
• Changed container names to use hyphens (e.g., arrowhead-core instead of arrowhead_core) to comply with URI syntax.
• Updated environment variable MYSQL_HOST=arrowhead-core-mysql.
○ Updated all .properties files:
• system.address=arrowhead-core
• sr_address=arrowhead-core
• spring.datasource.url uses arrowhead-core-mysql
○ Ensured that domain.name is set to arrowhead-core in each core service to avoid placeholder IP errors.
○ Added system users (gateway, orchestrator, etc.) to init-users.sql and placed it in the ./sql directory.
○ MySQL logs and docker exec were used to confirm that users were correctly created.
○ Used docker-compose down -v and docker-compose up --build to reset and initialize the environment properly.
4.	TLS Certificate Hostname Mismatch:
○ Services threw errors like:
"The certificate does not contain the specified IP address or DNS name as a Subject Alternative Name."
○ Fixes:
• Ensured the sr_address and system.address values match the Common Name (CN) or SAN in the service registry's certificate.
• Used disable.hostname.verifier=true in testing environments only to bypass strict hostname verification.
