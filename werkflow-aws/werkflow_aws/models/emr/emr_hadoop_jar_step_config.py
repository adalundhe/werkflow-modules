from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_key_value import EMRKeyValue


class EMRHadoopJarStepConfig(BaseModel):
    Properties: list[EMRKeyValue] | None = None
    Jar: StrictStr | None = None
    MainClass: StrictStr | None = None
    Args: list[StrictStr] | None = None
