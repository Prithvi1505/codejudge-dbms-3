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
