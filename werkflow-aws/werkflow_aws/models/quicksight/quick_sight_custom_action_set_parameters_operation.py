from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_set_parameter_value_configuration import QuickSightSetParameterValueConfiguration


class QuickSightCustomActionSetParametersOperation(BaseModel):
    ParameterValueConfigurations: list[QuickSightSetParameterValueConfiguration] | None = None
