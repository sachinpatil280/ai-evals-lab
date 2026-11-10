"""Gates on the golden dataset: every record is valid, and the set is diverse enough to calibrate a judge."""

import json
from collections import Counter
from pathlib import Path

import pytest

from evals.schema import Difficulty, GoldenRecord

DATASETS = Path(__file__).parent.parent / "datasets"
GOLDEN = DATASETS / "golden.jsonl"

# Phase 1 week-1 targets. Raise as the dataset grows toward 50-100.
MIN_RECORDS = 15
MIN_DOMAINS = 4
MIN_HARD = 5  # ambiguous + edge


def load_golden() -> list[GoldenRecord]:
    lines = [line for line in GOLDEN.read_text().splitlines() if line.strip()]
    return [GoldenRecord.model_validate_json(line) for line in lines]


def test_example_record_matches_schema():
    GoldenRecord.model_validate(json.loads((DATASETS / "example_record.json").read_text()))


def test_every_line_is_a_valid_record():
    for n, line in enumerate(GOLDEN.read_text().splitlines(), start=1):
        if line.strip():
            try:
                GoldenRecord.model_validate_json(line)
            except ValueError as e:
                pytest.fail(f"golden.jsonl line {n}: {e}")


def test_ids_are_unique():
    duplicates = [i for i, c in Counter(r.id for r in load_golden()).items() if c > 1]
    assert not duplicates, f"duplicate ids: {duplicates}"


def test_minimum_record_count():
    count = len(load_golden())
    assert count >= MIN_RECORDS, f"{count}/{MIN_RECORDS} records"


def test_domain_coverage():
    domains = {r.domain for r in load_golden()}
    assert len(domains) >= MIN_DOMAINS, f"{len(domains)}/{MIN_DOMAINS} domains: {sorted(domains)}"


def test_hard_case_coverage():
    hard = sum(r.difficulty != Difficulty.EASY for r in load_golden())
    assert hard >= MIN_HARD, f"{hard}/{MIN_HARD} ambiguous or edge records"
