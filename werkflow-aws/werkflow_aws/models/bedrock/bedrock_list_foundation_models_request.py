from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockListFoundationModelsRequest(BaseModel):
    byProvider: StrictStr | None = None
    byCustomizationType: Literal['FINE_TUNING', 'CONTINUED_PRE_TRAINING', 'DISTILLATION'] | None = None
    byOutputModality: Literal['TEXT', 'IMAGE', 'EMBEDDING'] | None = None
    byInferenceType: Literal['ON_DEMAND', 'PROVISIONED'] | None = None
    projectIdentifier: StrictStr | None = None
