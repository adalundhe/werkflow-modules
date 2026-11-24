from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class MWAAModuleLoggingConfigurationInput(BaseModel):
    Enabled: StrictBool
    LogLevel: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']
