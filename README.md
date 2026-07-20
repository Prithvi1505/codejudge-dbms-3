# codejudge-dbms-3

## Normalization Write-up
Unnormalized: Repeating course info in every enrollment row.
1NF: Atomic values.
2NF: Removed partial dependencies (course info in separate table).
3NF: Removed transitive dependencies (instructor details separated).

## Indexing Justification
- idx_students_department speeds up GROUP BY queries.
- Did not index marks_obtained (high write frequency, low selectivity).

## Concurrency Scenario
Two students try to enroll in last seat → Lost Update.
Serializable isolation level prevents it by locking rows.


# Part 2 — Cryptographic Protocols & Network Security

## Task 3: Security Principle Mapping
- **RSA**: Provides Confidentiality (encryption) and can support Non-repudiation (with digital signatures).
- **Diffie-Hellman**: Key exchange protocol only. It establishes a shared secret but does not encrypt data itself.

**Why DH is key exchange, not encryption**: It allows two parties to agree on a secret key over an insecure channel. The key can then be used with symmetric encryption (e.g., AES).

## Task 4: Threat Model Write-up

**a.** Place a hardware firewall at the network perimeter. Rule: Allow only ports 80/443 inbound.

**b.** Deploy both Host-based IDS (detects file changes on server) and Network-based IDS (detects network anomalies).

**c.** Use HTTPS. It prevents credential sniffing (man-in-the-middle on plain HTTP).

**d.** 2FA: Password (knowledge) + OTP from app (possession). 
- Students: Read marks + enroll.
- Instructors: Read/Write marks.
- Admins: Full access.

**e.** Active attack: Attacker performs session hijacking after capturing cookies on open Wi-Fi. This is active because the attacker injects/modifies traffic.
