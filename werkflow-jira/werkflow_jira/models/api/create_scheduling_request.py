from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .create_date_field_request import CreateDateFieldRequest


class CreateSchedulingRequest(BaseModel):
    dependencies: StrictStr | None = None
    endDate: CreateDateFieldRequest | None = None
    estimation: StrictStr | None = None
    inferredDates: StrictStr | None = None
    startDate: CreateDateFieldRequest | None = None
