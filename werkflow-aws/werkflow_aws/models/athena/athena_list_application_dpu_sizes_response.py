from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_application_dpu_sizes import AthenaApplicationDPUSizes


class AthenaListApplicationDPUSizesResponse(BaseModel):
    ApplicationDPUSizes: list[AthenaApplicationDPUSizes] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
