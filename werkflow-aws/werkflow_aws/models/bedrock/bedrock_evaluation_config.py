from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_evaluation_config import BedrockAutomatedEvaluationConfig
from .bedrock_human_evaluation_config import BedrockHumanEvaluationConfig


class BedrockEvaluationConfig(BaseModel):
    automated: BedrockAutomatedEvaluationConfig | None = None
    human: BedrockHumanEvaluationConfig | None = None
