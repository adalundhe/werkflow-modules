from __future__ import annotations
from pydantic import BaseModel
from .personalize_categorical_hyper_parameter_range import PersonalizeCategoricalHyperParameterRange
from .personalize_continuous_hyper_parameter_range import PersonalizeContinuousHyperParameterRange
from .personalize_integer_hyper_parameter_range import PersonalizeIntegerHyperParameterRange


class PersonalizeHyperParameterRanges(BaseModel):
    integerHyperParameterRanges: list[PersonalizeIntegerHyperParameterRange] | None = None
    continuousHyperParameterRanges: list[PersonalizeContinuousHyperParameterRange] | None = None
    categoricalHyperParameterRanges: list[PersonalizeCategoricalHyperParameterRange] | None = None
