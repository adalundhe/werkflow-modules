from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRHadoopStepConfig(BaseModel):
    Jar: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    MainClass: StrictStr | None = None
    Args: list[StrictStr] | None = None
