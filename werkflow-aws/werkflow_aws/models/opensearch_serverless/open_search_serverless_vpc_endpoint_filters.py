from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class OpenSearchServerlessVpcEndpointFilters(BaseModel):
    status: Literal['PENDING', 'DELETING', 'ACTIVE', 'FAILED'] | None = None
