# Testing Strategy – Rental Hunters (INST326 Project 4)

## Overview
Rental Hunters uses a layered testing strategy to ensure correctness,
reliability, and full system integration.

All tests are written using Python’s built-in `unittest` framework and
are organized into unit, integration, and system-level tests.

## Unit Testing
Unit tests verify individual components in isolation.

Examples include:
- Ensuring overall scores are numeric values
- Verifying score outputs fall within the expected range (0–10)

External services such as geocoding are mocked to ensure test stability
and independence from network availability.

## Integration Testing
Integration tests validate how core classes work together, including:
- RentalProperty
- ScoreCalculator
- PropertyManager

These tests confirm that data flows correctly between objects and that
business logic behaves as expected when components interact.

## System Testing
System tests verify complete end-to-end workflows, including:
- Creating rental properties
- Scoring and ranking rentals
- Saving results to CSV
- Loading saved state in a new session

These tests demonstrate that the system answers the project’s charter
question: **Which rental is the best option?**

## I/O and Data Validation Testing
Additional system tests verify data persistence and robustness:
- CSV files are successfully created and loaded
- Corrupted or invalid CSV data is rejected
- Invalid imported scores trigger appropriate errors

This ensures the system safely handles real-world data scenarios.

## Test Coverage Summary
- Unit tests validate core logic
- Integration tests verify class coordination
- System tests confirm full workflows
- I/O tests ensure persistence and data integrity

All tests pass successfully at submission time.
