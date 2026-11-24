from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_column import GlueColumn
from .glue_federated_table import GlueFederatedTable
from .glue_storage_descriptor import GlueStorageDescriptor
from .glue_table_identifier import GlueTableIdentifier
from .glue_view_definition_input import GlueViewDefinitionInput


class GlueTableInput(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    Owner: StrictStr | None = None
    LastAccessTime: datetime.datetime | StrictStr | None = None
    LastAnalyzedTime: datetime.datetime | StrictStr | None = None
    Retention: StrictInt | None = None
    StorageDescriptor: GlueStorageDescriptor | None = None
    PartitionKeys: list[GlueColumn] | None = None
    ViewOriginalText: StrictStr | None = None
    ViewExpandedText: StrictStr | None = None
    TableType: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    TargetTable: GlueTableIdentifier | None = None
    FederatedTable: GlueFederatedTable | None = None
    ViewDefinition: GlueViewDefinitionInput | None = None
