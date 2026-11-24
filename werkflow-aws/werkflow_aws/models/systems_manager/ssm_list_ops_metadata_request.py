from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_metadata_filter import SSMOpsMetadataFilter


class SSMListOpsMetadataRequest(BaseModel):
    Filters: list[SSMOpsMetadataFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
