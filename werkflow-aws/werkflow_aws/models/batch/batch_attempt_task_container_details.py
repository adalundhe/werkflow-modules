from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_network_interface import BatchNetworkInterface


class BatchAttemptTaskContainerDetails(BaseModel):
    exitCode: StrictInt | None = None
    name: StrictStr | None = None
    reason: StrictStr | None = None
    logStreamName: StrictStr | None = None
    networkInterfaces: list[BatchNetworkInterface] | None = None
