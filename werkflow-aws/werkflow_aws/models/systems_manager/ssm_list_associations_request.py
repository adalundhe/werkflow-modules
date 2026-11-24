from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_association_filter import SSMAssociationFilter


class SSMListAssociationsRequest(BaseModel):
    AssociationFilterList: list[SSMAssociationFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
