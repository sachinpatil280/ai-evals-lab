"""Gates on the golden dataset: every record is valid, and the set is diverse enough to calibrate a judge."""

import json
from collections import Counter
from pathlib import Path

import pytest

from evals.schema import Difficulty, GoldenRecord

DATASETS = Path(__file__).parent.parent / "datasets"
GOLDEN = DATASETS / "golden"  # one us-NNN.json file per record

# Phase 1 week-1 targets. Raise as the dataset grows toward 50-100.
MIN_RECORDS = 15
MIN_DOMAINS = 4
MIN_HARD = 5  # ambiguous + edge


def golden_files() -> list[Path]:
    return sorted(GOLDEN.glob("*.json"))


def load_golden() -> list[GoldenRecord]:
    return [GoldenRecord.model_validate_json(f.read_text()) for f in golden_files()]


def test_example_record_matches_schema():
    GoldenRecord.model_validate(json.loads((DATASETS / "example_record.json").read_text()))


def test_every_file_is_a_valid_record():
    for f in golden_files():
        try:
            record = GoldenRecord.model_validate_json(f.read_text())
        except ValueError as e:
            pytest.fail(f"{f.name}: {e}")
        assert record.id == f.stem, f"{f.name}: id is '{record.id}', must match file name"


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
