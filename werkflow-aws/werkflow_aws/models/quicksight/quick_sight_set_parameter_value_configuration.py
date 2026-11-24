from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_destination_parameter_value_configuration import QuickSightDestinationParameterValueConfiguration


class QuickSightSetParameterValueConfiguration(BaseModel):
    DestinationParameterName: StrictStr | None = None
    Value: QuickSightDestinationParameterValueConfiguration | None = None
