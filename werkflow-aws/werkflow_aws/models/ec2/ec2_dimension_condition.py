from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2DimensionCondition(BaseModel):
    Dimension: Literal['resource-region', 'availability-zone-id', 'account-id', 'account-name', 'instance-family', 'instance-type', 'instance-platform', 'reservation-arn', 'reservation-id', 'reservation-type', 'reservation-create-timestamp', 'reservation-start-timestamp', 'reservation-end-timestamp', 'reservation-end-date-type', 'tenancy', 'reservation-state', 'reservation-instance-match-criteria', 'reservation-unused-financial-owner'] | None = None
    Comparison: Literal['equals', 'in'] | None = None
    Values: list[StrictStr] | None = None
