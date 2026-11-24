from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_index_capacity_configuration import QBusinessIndexCapacityConfiguration
from .q_business_tag import QBusinessTag


class QBusinessCreateIndexRequest(BaseModel):
    applicationId: StrictStr
    displayName: StrictStr
    description: StrictStr | None = None
    type: Literal['ENTERPRISE', 'STARTER'] | None = None
    tags: list[QBusinessTag] | None = None
    capacityConfiguration: QBusinessIndexCapacityConfiguration | None = None
    clientToken: StrictStr | None = None
