from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_snapmirror_relationship_filter import FSxSnapmirrorRelationshipFilter


class FSxDescribeSnapmirrorRelationshipsRequest(BaseModel):
    SnapmirrorRelationshipIds: list[StrictStr] | None = None
    Filters: list[FSxSnapmirrorRelationshipFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
