from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyCapacityReservationRequest(BaseModel):
    CapacityReservationId: StrictStr
    InstanceCount: StrictInt | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    EndDateType: Literal['unlimited', 'limited'] | None = None
    Accept: StrictBool | None = None
    DryRun: StrictBool | None = None
    AdditionalInfo: StrictStr | None = None
    InstanceMatchCriteria: Literal['open', 'targeted'] | None = None
    AcceptModificationTerms: StrictBool | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    QuoteId: StrictStr | None = None
