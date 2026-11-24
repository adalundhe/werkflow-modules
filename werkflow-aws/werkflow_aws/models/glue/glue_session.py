from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_connections_list import GlueConnectionsList
from .glue_session_command import GlueSessionCommand


class GlueSession(BaseModel):
    Id: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    Description: StrictStr | None = None
    Role: StrictStr | None = None
    Command: GlueSessionCommand | None = None
    DefaultArguments: dict[StrictStr, StrictStr] | None = None
    Connections: GlueConnectionsList | None = None
    Progress: StrictFloat | StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    GlueVersion: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    WorkerType: StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    ExecutionTime: StrictFloat | StrictInt | None = None
    DPUSeconds: StrictFloat | StrictInt | None = None
    IdleTimeout: StrictInt | None = None
    ProfileName: StrictStr | None = None
    SessionType: StrictStr | None = None
