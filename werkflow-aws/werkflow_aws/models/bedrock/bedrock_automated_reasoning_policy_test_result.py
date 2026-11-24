from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_check_finding import BedrockAutomatedReasoningCheckFinding
from .bedrock_automated_reasoning_policy_test_case import BedrockAutomatedReasoningPolicyTestCase


class BedrockAutomatedReasoningPolicyTestResult(BaseModel):
    testCase: BedrockAutomatedReasoningPolicyTestCase | None = None
    policyArn: StrictStr | None = None
    testRunStatus: StrictStr | None = None
    testFindings: list[BedrockAutomatedReasoningCheckFinding] | None = None
    testRunResult: StrictStr | None = None
    aggregatedTestFindingsResult: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
