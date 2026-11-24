from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .mq_shared_resource_error import MQSharedResourceError


class MQSharedResource(BaseModel):
    DnsNames: list[StrictStr] | None = None
    Error: MQSharedResourceError | None = None
    ResourceArn: StrictStr | None = None
    ResourceShareArns: list[StrictStr] | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
