from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyProduct(BaseModel):
    Name: StrictStr | None = None
    Feature: StrictStr | None = None
