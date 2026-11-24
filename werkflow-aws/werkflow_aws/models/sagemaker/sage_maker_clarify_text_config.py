from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_clarify_text_granularity import SageMakerClarifyTextGranularity
from .sage_maker_clarify_text_language import SageMakerClarifyTextLanguage


class SageMakerClarifyTextConfig(BaseModel):
    Language: SageMakerClarifyTextLanguage | None = None
    Granularity: SageMakerClarifyTextGranularity | None = None
