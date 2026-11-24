from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSFleetAdvisorSchemaObjectResponse(BaseModel):
    SchemaId: StrictStr | None = None
    ObjectType: StrictStr | None = None
    NumberOfObjects: StrictInt | None = None
    CodeLineCount: StrictInt | None = None
    CodeSize: StrictInt | None = None
