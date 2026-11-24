from __future__ import annotations
from pydantic import BaseModel
from .bedrock_grader_config import BedrockGraderConfig
from .bedrock_rft_hyper_parameters import BedrockRFTHyperParameters


class BedrockRFTConfig(BaseModel):
    graderConfig: BedrockGraderConfig | None = None
    hyperParameters: BedrockRFTHyperParameters | None = None
