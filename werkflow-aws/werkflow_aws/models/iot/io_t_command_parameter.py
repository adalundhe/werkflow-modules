from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_command_parameter_value import IoTCommandParameterValue
from .io_t_command_parameter_value_condition import IoTCommandParameterValueCondition


class IoTCommandParameter(BaseModel):
    name: StrictStr | None = None
    type: StrictStr | None = None
    value: IoTCommandParameterValue | None = None
    defaultValue: IoTCommandParameterValue | None = None
    valueConditions: list[IoTCommandParameterValueCondition] | None = None
    description: StrictStr | None = None
