from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_command_parameter_value_comparison_operand import IoTCommandParameterValueComparisonOperand


class IoTCommandParameterValueCondition(BaseModel):
    comparisonOperator: StrictStr | None = None
    operand: IoTCommandParameterValueComparisonOperand | None = None
