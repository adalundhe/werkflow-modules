from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .firehose_database_column_list import FirehoseDatabaseColumnList
from .firehose_database_list import FirehoseDatabaseList
from .firehose_database_snapshot_info import FirehoseDatabaseSnapshotInfo
from .firehose_database_source_authentication_configuration import FirehoseDatabaseSourceAuthenticationConfiguration
from .firehose_database_source_vpc_configuration import FirehoseDatabaseSourceVPCConfiguration
from .firehose_database_table_list import FirehoseDatabaseTableList


class FirehoseDatabaseSourceDescription(BaseModel):
    Type: StrictStr | None = None
    Endpoint: StrictStr | None = None
    Port: StrictInt | None = None
    SSLMode: StrictStr | None = None
    Databases: FirehoseDatabaseList | None = None
    Tables: FirehoseDatabaseTableList | None = None
    Columns: FirehoseDatabaseColumnList | None = None
    SurrogateKeys: list[StrictStr] | None = None
    SnapshotWatermarkTable: StrictStr | None = None
    SnapshotInfo: list[FirehoseDatabaseSnapshotInfo] | None = None
    DatabaseSourceAuthenticationConfiguration: FirehoseDatabaseSourceAuthenticationConfiguration | None = None
    DatabaseSourceVPCConfiguration: FirehoseDatabaseSourceVPCConfiguration | None = None
