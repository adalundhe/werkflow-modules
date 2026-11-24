from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .msk_catalog import MSKCatalog
from .msk_dead_letter_queue_s3 import MSKDeadLetterQueueS3
from .msk_destination_table import MSKDestinationTable
from .msk_schema_evolution import MSKSchemaEvolution
from .msk_table_creation import MSKTableCreation


class MSKIcebergDestinationConfiguration(BaseModel):
    AppendOnly: StrictBool | None = None
    Catalog: MSKCatalog | None = None
    DataFreshnessInSeconds: StrictInt | None = None
    DeadLetterQueueS3: MSKDeadLetterQueueS3 | None = None
    DestinationTableList: list[MSKDestinationTable] | None = None
    SchemaEvolution: MSKSchemaEvolution | None = None
    ServiceExecutionRoleArn: StrictStr | None = None
    TableCreation: MSKTableCreation | None = None
    CompressionType: StrictStr | None = None
