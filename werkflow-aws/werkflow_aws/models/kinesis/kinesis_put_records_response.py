from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_put_records_result_entry import KinesisPutRecordsResultEntry


class KinesisPutRecordsResponse(BaseModel):
    FailedRecordCount: StrictInt | None = None
    Records: list[KinesisPutRecordsResultEntry] | None = None
    EncryptionType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
