from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_resource_uri import GlueResourceUri


class GlueUserDefinedFunctionInput(BaseModel):
    FunctionName: StrictStr | None = None
    ClassName: StrictStr | None = None
    OwnerName: StrictStr | None = None
    FunctionType: Literal['REGULAR_FUNCTION', 'AGGREGATE_FUNCTION', 'STORED_PROCEDURE'] | None = None
    OwnerType: Literal['USER', 'ROLE', 'GROUP'] | None = None
    ResourceUris: list[GlueResourceUri] | None = None
    ArtifactLocation: StrictStr | None = None
    GovernanceMode: Literal['IAM_ONLY', 'LAKE_FORMATION'] | None = None
