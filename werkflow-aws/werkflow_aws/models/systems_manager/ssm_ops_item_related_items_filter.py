from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMOpsItemRelatedItemsFilter(BaseModel):
    Key: Literal['ResourceType', 'AssociationId', 'ResourceUri']
    Values: list[StrictStr]
    Operator: Literal['Equal']
