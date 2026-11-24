from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_calculation_component import ConnectCalculationComponent


class ConnectMetricCalculation(BaseModel):
    CalculationComponents: list[ConnectCalculationComponent] | None = None
    Calculation: StrictStr | None = None
