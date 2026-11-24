from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class VerifiedPermissionsGetSchemaResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    policyStoreId: StrictStr | None = None
    schema_: StrictStr | None = Field(default=None, alias='schema')
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    namespaces: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
