from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_orderable_db_instance_option import DocumentDBOrderableDBInstanceOption


class DocumentDBDescribeOrderableDBInstanceOptionsResponse(BaseModel):
    OrderableDBInstanceOptions: list[DocumentDBOrderableDBInstanceOption] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
