from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_import_resource_specification import LexImportResourceSpecification


class LexStartImportResponse(BaseModel):
    importId: StrictStr | None = None
    resourceSpecification: LexImportResourceSpecification | None = None
    mergeStrategy: StrictStr | None = None
    importStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
