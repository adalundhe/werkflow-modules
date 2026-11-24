from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_parameter_range import SageMakerParameterRange


class SageMakerHyperParameterSpecification(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    Range: SageMakerParameterRange | None = None
    IsTunable: StrictBool | None = None
    IsRequired: StrictBool | None = None
    DefaultValue: StrictStr | None = None
