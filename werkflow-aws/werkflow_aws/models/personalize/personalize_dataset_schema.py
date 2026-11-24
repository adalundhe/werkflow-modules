from __future__ import annotations
import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class PersonalizeDatasetSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: StrictStr | None = None
    schemaArn: StrictStr | None = None
    schema_: StrictStr | None = Field(default=None, alias='schema')
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    domain: StrictStr | None = None
