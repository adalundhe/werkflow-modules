from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeConnectionResourceParameters(BaseModel):
    ResourceConfigurationArn: StrictStr | None = None
    ResourceAssociationArn: StrictStr | None = None
