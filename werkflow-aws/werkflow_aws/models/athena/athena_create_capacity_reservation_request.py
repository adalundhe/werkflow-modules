from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .athena_tag_model import AthenaTagModel


class AthenaCreateCapacityReservationRequest(BaseModel):
    TargetDpus: StrictInt
    Name: StrictStr
    Tags: list[AthenaTagModel] | None = None
