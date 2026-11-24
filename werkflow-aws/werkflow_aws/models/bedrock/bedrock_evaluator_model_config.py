from __future__ import annotations
from pydantic import BaseModel
from .bedrock_evaluator_model import BedrockEvaluatorModel


class BedrockEvaluatorModelConfig(BaseModel):
    bedrockEvaluatorModels: list[BedrockEvaluatorModel] | None = None
