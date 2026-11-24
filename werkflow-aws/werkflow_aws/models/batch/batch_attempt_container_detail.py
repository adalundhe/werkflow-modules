from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_network_interface import BatchNetworkInterface


class BatchAttemptContainerDetail(BaseModel):
    containerInstanceArn: StrictStr | None = None
    taskArn: StrictStr | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
    logStreamName: StrictStr | None = None
    networkInterfaces: list[BatchNetworkInterface] | None = None
