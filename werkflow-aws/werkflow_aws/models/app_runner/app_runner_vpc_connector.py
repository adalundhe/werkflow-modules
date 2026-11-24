from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AppRunnerVpcConnector(BaseModel):
    VpcConnectorName: StrictStr | None = None
    VpcConnectorArn: StrictStr | None = None
    VpcConnectorRevision: StrictInt | None = None
    Subnets: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    DeletedAt: datetime.datetime | StrictStr | None = None
