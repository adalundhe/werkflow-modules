from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .bedrock_automated_reasoning_policy_report_source_document import BedrockAutomatedReasoningPolicyReportSourceDocument
from .bedrock_automated_reasoning_policy_rule_report import BedrockAutomatedReasoningPolicyRuleReport
from .bedrock_automated_reasoning_policy_variable_report import BedrockAutomatedReasoningPolicyVariableReport


class BedrockAutomatedReasoningPolicyFidelityReport(BaseModel):
    coverageScore: StrictFloat | StrictInt | None = None
    accuracyScore: StrictFloat | StrictInt | None = None
    ruleReports: dict[StrictStr, BedrockAutomatedReasoningPolicyRuleReport] | None = None
    variableReports: dict[StrictStr, BedrockAutomatedReasoningPolicyVariableReport] | None = None
    documentSources: list[BedrockAutomatedReasoningPolicyReportSourceDocument] | None = None
