from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSDescribeClustersRequest(BaseModel):
    clusters: list[StrictStr] | None = None
    include: list[Literal['ATTACHMENTS', 'CONFIGURATIONS', 'SETTINGS', 'STATISTICS', 'TAGS']] | None = None
