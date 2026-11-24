from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .get_date_field_response import GetDateFieldResponse


class GetSchedulingResponse(BaseModel):
    dependencies: StrictStr | None = None
    endDate: GetDateFieldResponse | None = None
    estimation: StrictStr | None = None
    inferredDates: StrictStr | None = None
    startDate: GetDateFieldResponse | None = None
