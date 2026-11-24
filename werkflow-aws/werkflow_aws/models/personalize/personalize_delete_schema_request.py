from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteSchemaRequest(BaseModel):
    schemaArn: StrictStr
