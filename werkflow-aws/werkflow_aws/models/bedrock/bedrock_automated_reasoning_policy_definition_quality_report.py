from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .bedrock_automated_reasoning_policy_definition_type_value_pair import BedrockAutomatedReasoningPolicyDefinitionTypeValuePair
from .bedrock_automated_reasoning_policy_disjoint_rule_set import BedrockAutomatedReasoningPolicyDisjointRuleSet


class BedrockAutomatedReasoningPolicyDefinitionQualityReport(BaseModel):
    typeCount: StrictInt | None = None
    variableCount: StrictInt | None = None
    ruleCount: StrictInt | None = None
    unusedTypes: list[StrictStr] | None = None
    unusedTypeValues: list[BedrockAutomatedReasoningPolicyDefinitionTypeValuePair] | None = None
    unusedVariables: list[StrictStr] | None = None
    conflictingRules: list[StrictStr] | None = None
    disjointRuleSets: list[BedrockAutomatedReasoningPolicyDisjointRuleSet] | None = None
