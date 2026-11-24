from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_entity_info import IAMEntityInfo


class IAMEntityDetails(BaseModel):
    EntityInfo: IAMEntityInfo | None = None
    LastAuthenticated: datetime.datetime | StrictStr | None = None
