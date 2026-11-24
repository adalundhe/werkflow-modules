from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2Matcher(BaseModel):
    HttpCode: StrictStr | None = None
    GrpcCode: StrictStr | None = None
