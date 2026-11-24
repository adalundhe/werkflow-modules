from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_bedrock_model_specification import LexBedrockModelSpecification


class LexSampleUtteranceGenerationSpecification(BaseModel):
    enabled: StrictBool | None = None
    bedrockModelSpecification: LexBedrockModelSpecification | None = None
