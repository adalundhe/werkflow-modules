from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_model_variant_config import SageMakerModelVariantConfig


class SageMakerStopInferenceExperimentRequest(BaseModel):
    Name: StrictStr
    ModelVariantActions: dict[StrictStr, Literal['Retain', 'Remove', 'Promote']]
    DesiredModelVariants: list[SageMakerModelVariantConfig] | None = None
    DesiredState: Literal['Completed', 'Cancelled'] | None = None
    Reason: StrictStr | None = None
