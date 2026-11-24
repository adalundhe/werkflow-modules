from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_ops_entity_item import SSMOpsEntityItem


class SSMOpsEntity(BaseModel):
    Id: StrictStr | None = None
    Data: dict[StrictStr, SSMOpsEntityItem] | None = None
