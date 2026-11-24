from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dms_database_short_info_response import DMSDatabaseShortInfoResponse
from .dms_schema_short_info_response import DMSSchemaShortInfoResponse
from .dms_server_short_info_response import DMSServerShortInfoResponse


class DMSSchemaResponse(BaseModel):
    CodeLineCount: StrictInt | None = None
    CodeSize: StrictInt | None = None
    Complexity: StrictStr | None = None
    Server: DMSServerShortInfoResponse | None = None
    DatabaseInstance: DMSDatabaseShortInfoResponse | None = None
    SchemaId: StrictStr | None = None
    SchemaName: StrictStr | None = None
    OriginalSchema: DMSSchemaShortInfoResponse | None = None
    Similarity: StrictFloat | StrictInt | None = None
