from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EKSInsightsFilter(BaseModel):
    categories: list[Literal['UPGRADE_READINESS', 'MISCONFIGURATION', 'ROLLBACK_READINESS']] | None = None
    kubernetesVersions: list[StrictStr] | None = None
    statuses: list[Literal['PASSING', 'WARNING', 'ERROR', 'UNKNOWN']] | None = None
