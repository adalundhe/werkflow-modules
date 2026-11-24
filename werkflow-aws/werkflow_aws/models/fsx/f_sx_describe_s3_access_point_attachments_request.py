from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_s3_access_point_attachments_filter import FSxS3AccessPointAttachmentsFilter


class FSxDescribeS3AccessPointAttachmentsRequest(BaseModel):
    Names: list[StrictStr] | None = None
    Filters: list[FSxS3AccessPointAttachmentsFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
