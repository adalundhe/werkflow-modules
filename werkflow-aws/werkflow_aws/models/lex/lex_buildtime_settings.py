from __future__ import annotations
from pydantic import BaseModel
from .lex_descriptive_bot_builder_specification import LexDescriptiveBotBuilderSpecification
from .lex_sample_utterance_generation_specification import LexSampleUtteranceGenerationSpecification


class LexBuildtimeSettings(BaseModel):
    descriptiveBotBuilder: LexDescriptiveBotBuilderSpecification | None = None
    sampleUtteranceGeneration: LexSampleUtteranceGenerationSpecification | None = None
