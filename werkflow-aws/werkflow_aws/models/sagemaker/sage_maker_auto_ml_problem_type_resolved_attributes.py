from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_tabular_resolved_attributes import SageMakerTabularResolvedAttributes
from .sage_maker_text_generation_resolved_attributes import SageMakerTextGenerationResolvedAttributes


class SageMakerAutoMLProblemTypeResolvedAttributes(BaseModel):
    TabularResolvedAttributes: SageMakerTabularResolvedAttributes | None = None
    TextGenerationResolvedAttributes: SageMakerTextGenerationResolvedAttributes | None = None
