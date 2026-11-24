from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_connections_list import GlueConnectionsList
from .glue_session_command import GlueSessionCommand


class GlueCreateSessionRequest(BaseModel):
    Id: StrictStr
    Role: StrictStr
    Command: GlueSessionCommand
    Description: StrictStr | None = None
    Timeout: StrictInt | None = None
    IdleTimeout: StrictInt | None = None
    DefaultArguments: dict[StrictStr, StrictStr] | None = None
    Connections: GlueConnectionsList | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    NumberOfWorkers: StrictInt | None = None
    WorkerType: Literal['Standard', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'G.025X', 'Z.2X', 'G.12X', 'G.16X', 'R.1X', 'R.2X', 'R.4X', 'R.8X'] | None = None
    SecurityConfiguration: StrictStr | None = None
    GlueVersion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    RequestOrigin: StrictStr | None = None
    SessionType: Literal['LIVY', 'SPARK_CONNECT'] | None = None
