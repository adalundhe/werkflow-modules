from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_command_parameter_value_number_range import IoTCommandParameterValueNumberRange


class IoTCommandParameterValueComparisonOperand(BaseModel):
    number: StrictStr | None = None
    numbers: list[StrictStr] | None = None
    string: StrictStr | None = None
    strings: list[StrictStr] | None = None
    numberRange: IoTCommandParameterValueNumberRange | None = None
