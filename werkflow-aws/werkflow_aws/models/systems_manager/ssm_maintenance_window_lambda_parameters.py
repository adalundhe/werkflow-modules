from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class SSMMaintenanceWindowLambdaParameters(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    ClientContext: StrictStr | None = None
    Qualifier: StrictStr | None = None
    Payload: StrictBytes | Any | None = None
