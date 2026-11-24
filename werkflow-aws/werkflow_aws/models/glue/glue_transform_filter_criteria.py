from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_schema_column import GlueSchemaColumn


class GlueTransformFilterCriteria(BaseModel):
    Name: StrictStr | None = None
    TransformType: Literal['FIND_MATCHES'] | None = None
    Status: Literal['NOT_READY', 'READY', 'DELETING'] | None = None
    GlueVersion: StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    LastModifiedBefore: datetime.datetime | StrictStr | None = None
    LastModifiedAfter: datetime.datetime | StrictStr | None = None
    Schema: list[GlueSchemaColumn] | None = None
