from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_categorical_parameter import SageMakerCategoricalParameter


class SageMakerEnvironmentParameterRanges(BaseModel):
    CategoricalParameterRanges: list[SageMakerCategoricalParameter] | None = None
