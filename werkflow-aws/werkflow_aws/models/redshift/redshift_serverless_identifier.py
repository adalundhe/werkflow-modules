from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftServerlessIdentifier(BaseModel):
    NamespaceIdentifier: StrictStr
    WorkgroupIdentifier: StrictStr
