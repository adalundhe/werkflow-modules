from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .firehose_database_column_list import FirehoseDatabaseColumnList
from .firehose_database_list import FirehoseDatabaseList
from .firehose_database_source_authentication_configuration import FirehoseDatabaseSourceAuthenticationConfiguration
from .firehose_database_source_vpc_configuration import FirehoseDatabaseSourceVPCConfiguration
from .firehose_database_table_list import FirehoseDatabaseTableList


class FirehoseDatabaseSourceConfiguration(BaseModel):
    Type: Literal['MySQL', 'PostgreSQL']
    Endpoint: StrictStr
    Port: StrictInt
    Databases: FirehoseDatabaseList
    Tables: FirehoseDatabaseTableList
    SnapshotWatermarkTable: StrictStr
    DatabaseSourceAuthenticationConfiguration: FirehoseDatabaseSourceAuthenticationConfiguration
    DatabaseSourceVPCConfiguration: FirehoseDatabaseSourceVPCConfiguration
    SSLMode: Literal['Disabled', 'Enabled'] | None = None
    Columns: FirehoseDatabaseColumnList | None = None
    SurrogateKeys: list[StrictStr] | None = None
