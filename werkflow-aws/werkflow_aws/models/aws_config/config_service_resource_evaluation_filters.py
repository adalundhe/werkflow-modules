from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .config_service_time_window import ConfigServiceTimeWindow


class ConfigServiceResourceEvaluationFilters(BaseModel):
    EvaluationMode: Literal['DETECTIVE', 'PROACTIVE'] | None = None
    TimeWindow: ConfigServiceTimeWindow | None = None
    EvaluationContextIdentifier: StrictStr | None = None
