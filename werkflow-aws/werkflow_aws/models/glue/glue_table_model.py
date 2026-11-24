from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_column import GlueColumn
from .glue_federated_table import GlueFederatedTable
from .glue_iceberg_table_metadata import GlueIcebergTableMetadata
from .glue_rls_properties import GlueRLSProperties
from .glue_storage_descriptor import GlueStorageDescriptor
from .glue_table_identifier import GlueTableIdentifier
from .glue_table_status import GlueTableStatus
from .glue_view_definition import GlueViewDefinition


class GlueTableModel(BaseModel):
    Name: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    Description: StrictStr | None = None
    Owner: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    LastAccessTime: datetime.datetime | StrictStr | None = None
    LastAnalyzedTime: datetime.datetime | StrictStr | None = None
    Retention: StrictInt | None = None
    StorageDescriptor: GlueStorageDescriptor | None = None
    PartitionKeys: list[GlueColumn] | None = None
    ViewOriginalText: StrictStr | None = None
    ViewExpandedText: StrictStr | None = None
    TableType: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
    CreatedBy: StrictStr | None = None
    IsRegisteredWithLakeFormation: StrictBool | None = None
    TargetTable: GlueTableIdentifier | None = None
    CatalogId: StrictStr | None = None
    VersionId: StrictStr | None = None
    FederatedTable: GlueFederatedTable | None = None
    ViewDefinition: GlueViewDefinition | None = None
    IsMultiDialectView: StrictBool | None = None
    IsMaterializedView: StrictBool | None = None
    IcebergTableMetadata: GlueIcebergTableMetadata | None = None
    Status: GlueTableStatus | None = None
    RLSProperties: GlueRLSProperties | None = None
