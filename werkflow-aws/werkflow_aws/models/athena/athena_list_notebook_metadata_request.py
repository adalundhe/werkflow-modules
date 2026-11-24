from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .athena_filter_definition import AthenaFilterDefinition


class AthenaListNotebookMetadataRequest(BaseModel):
    WorkGroup: StrictStr
    Filters: AthenaFilterDefinition | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
