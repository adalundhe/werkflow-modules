from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_resource_uri import GlueResourceUri


class GlueUserDefinedFunction(BaseModel):
    FunctionName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    ClassName: StrictStr | None = None
    OwnerName: StrictStr | None = None
    FunctionType: StrictStr | None = None
    OwnerType: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ResourceUris: list[GlueResourceUri] | None = None
    ArtifactLocation: StrictStr | None = None
    GovernanceMode: StrictStr | None = None
    CatalogId: StrictStr | None = None
