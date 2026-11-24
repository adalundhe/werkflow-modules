from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class Route53TestDNSAnswerResponse(BaseModel):
    Nameserver: StrictStr | None = None
    RecordName: StrictStr | None = None
    RecordType: StrictStr | None = None
    RecordData: list[StrictStr] | None = None
    ResponseCode: StrictStr | None = None
    Protocol: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
