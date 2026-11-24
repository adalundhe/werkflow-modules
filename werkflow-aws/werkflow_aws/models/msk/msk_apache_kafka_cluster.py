from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKApacheKafkaCluster(BaseModel):
    ApacheKafkaClusterId: StrictStr | None = None
    BootstrapBrokerString: StrictStr | None = None
