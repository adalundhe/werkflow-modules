from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftClusterParameterStatus(BaseModel):
    ParameterName: StrictStr | None = None
    ParameterApplyStatus: StrictStr | None = None
    ParameterApplyErrorDescription: StrictStr | None = None
