from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_parameter import SageMakerAutoParameter
from .sage_maker_categorical_parameter_range import SageMakerCategoricalParameterRange
from .sage_maker_continuous_parameter_range import SageMakerContinuousParameterRange
from .sage_maker_integer_parameter_range import SageMakerIntegerParameterRange


class SageMakerParameterRanges(BaseModel):
    IntegerParameterRanges: list[SageMakerIntegerParameterRange] | None = None
    ContinuousParameterRanges: list[SageMakerContinuousParameterRange] | None = None
    CategoricalParameterRanges: list[SageMakerCategoricalParameterRange] | None = None
    AutoParameters: list[SageMakerAutoParameter] | None = None
