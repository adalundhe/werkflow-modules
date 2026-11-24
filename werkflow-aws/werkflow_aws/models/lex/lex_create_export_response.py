from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_export_resource_specification import LexExportResourceSpecification


class LexCreateExportResponse(BaseModel):
    exportId: StrictStr | None = None
    resourceSpecification: LexExportResourceSpecification | None = None
    fileFormat: StrictStr | None = None
    exportStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
