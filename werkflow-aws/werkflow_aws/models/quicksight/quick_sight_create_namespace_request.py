from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightCreateNamespaceRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    IdentityStore: Literal['QUICKSIGHT']
    Tags: list[QuickSightTag] | None = None
