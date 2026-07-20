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


## Aging Trace (Priority Scheduling)

Low-priority process P5 starved because higher priority processes keep arriving.

After aging (priority += 1 every 5 time units):
Time | P1 Pri | P5 Pri
0    | 10     | 1
10   | 10     | 3
20   | 10     | 5   ← P5 now scheduled

## Deadlock Scenario

Processes: P1, P2, P3  
Resources: R1 (DB lock), R2 (File lock), R3 (Cache lock)

- P1 holds R1, requests R2
- P2 holds R2, requests R3
- P3 holds R3, requests R1

All 4 conditions satisfied. Removing P3→R1 breaks circular wait.

Prevention: Impose resource ordering (always request lower numbered resource first). Limitation: May reduce concurrency.
