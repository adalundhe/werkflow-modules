from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel


class RDSModifyDBShardGroupResponse(BaseModel):
    DBShardGroupResourceId: StrictStr | None = None
    DBShardGroupIdentifier: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    MaxACU: StrictFloat | StrictInt | None = None
    MinACU: StrictFloat | StrictInt | None = None
    ComputeRedundancy: StrictInt | None = None
    Status: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Endpoint: StrictStr | None = None
    DBShardGroupArn: StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
