from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMAssociationFilter(BaseModel):
    key: Literal['InstanceId', 'Name', 'AssociationId', 'AssociationStatusName', 'LastExecutedBefore', 'LastExecutedAfter', 'AssociationName', 'ResourceGroupName', 'CloudConnectorId']
    value: StrictStr
