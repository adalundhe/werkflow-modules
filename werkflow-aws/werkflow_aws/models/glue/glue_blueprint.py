from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_last_active_definition import GlueLastActiveDefinition


class GlueBlueprint(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    ParameterSpec: StrictStr | None = None
    BlueprintLocation: StrictStr | None = None
    BlueprintServiceLocation: StrictStr | None = None
    Status: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LastActiveDefinition: GlueLastActiveDefinition | None = None
