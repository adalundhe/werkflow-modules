from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDataSourceAttachmentResponse(BaseModel):
    attachmentId: StrictStr | None = None
    id: StrictStr | None = None
    arn: StrictStr | None = None
    dataSourceArn: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
