from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_connection_group_association_filter import CloudFrontConnectionGroupAssociationFilter


class CloudFrontListConnectionGroupsRequest(BaseModel):
    AssociationFilter: CloudFrontConnectionGroupAssociationFilter | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
