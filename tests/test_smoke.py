"""Smoke test: proves the DeepEval + pytest gate runs end to end.

Deterministic (no LLM call, no API key) so it runs anywhere, including CI.
Replaced by real LLM-as-judge tests in Phase 1.
"""

from deepeval import assert_test
from deepeval.metrics import PatternMatchMetric
from deepeval.test_case import LLMTestCase

USER_STORY = (
    "As a registered user, I want to reset my password via email "
    "so that I can regain access to my account.\n"
    "AC1: Reset link is sent only to registered emails.\n"
    "AC2: Reset link expires after 30 minutes."
)

GENERATED_TEST_CASE = (
    "Title: Reset link expires after 30 minutes\n"
    "Preconditions: User 'a@example.com' is registered\n"
    "Steps:\n"
    "1. Request password reset for a@example.com\n"
    "2. Wait 31 minutes\n"
    "3. Open the reset link\n"
    "Expected: Link is rejected with an 'expired' message"
)

# A generated test case must contain Title, Steps and Expected, in that order.
TEST_CASE_STRUCTURE = r"(?s).*Title:.+Steps:.+Expected:.+"


def test_generated_test_case_has_required_structure():
    test_case = LLMTestCase(input=USER_STORY, actual_output=GENERATED_TEST_CASE)
    assert_test(test_case, [PatternMatchMetric(pattern=TEST_CASE_STRUCTURE)])
