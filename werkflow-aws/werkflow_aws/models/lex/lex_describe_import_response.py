from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_import_resource_specification import LexImportResourceSpecification


class LexDescribeImportResponse(BaseModel):
    importId: StrictStr | None = None
    resourceSpecification: LexImportResourceSpecification | None = None
    importedResourceId: StrictStr | None = None
    importedResourceName: StrictStr | None = None
    mergeStrategy: StrictStr | None = None
    importStatus: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
