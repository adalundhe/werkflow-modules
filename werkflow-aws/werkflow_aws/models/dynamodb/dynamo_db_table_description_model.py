from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_archival_summary_model import DynamoDBArchivalSummaryModel
from .dynamo_db_attribute_definition_model import DynamoDBAttributeDefinitionModel
from .dynamo_db_billing_mode_summary_model import DynamoDBBillingModeSummaryModel
from .dynamo_db_global_secondary_index_description_model import DynamoDBGlobalSecondaryIndexDescriptionModel
from .dynamo_db_global_table_witness_description_model import DynamoDBGlobalTableWitnessDescriptionModel
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_local_secondary_index_description_model import DynamoDBLocalSecondaryIndexDescriptionModel
from .dynamo_db_on_demand_throughput_model import DynamoDBOnDemandThroughputModel
from .dynamo_db_provisioned_throughput_description_model import DynamoDBProvisionedThroughputDescriptionModel
from .dynamo_db_replica_description_model import DynamoDBReplicaDescriptionModel
from .dynamo_db_restore_summary_model import DynamoDBRestoreSummaryModel
from .dynamo_dbsse_description_model import DynamoDBSSEDescriptionModel
from .dynamo_db_stream_specification_model import DynamoDBStreamSpecificationModel
from .dynamo_db_table_class_summary_model import DynamoDBTableClassSummaryModel
from .dynamo_db_table_warm_throughput_description_model import DynamoDBTableWarmThroughputDescriptionModel
from .dynamo_db_vector_index_description_model import DynamoDBVectorIndexDescriptionModel


class DynamoDBTableDescriptionModel(BaseModel):
    AttributeDefinitions: list[DynamoDBAttributeDefinitionModel] | None = None
    TableName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElementModel] | None = None
    TableStatus: StrictStr | None = None
    CreationDateTime: datetime.datetime | StrictStr | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputDescriptionModel | None = None
    TableSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    TableArn: StrictStr | None = None
    TableId: StrictStr | None = None
    BillingModeSummary: DynamoDBBillingModeSummaryModel | None = None
    LocalSecondaryIndexes: list[DynamoDBLocalSecondaryIndexDescriptionModel] | None = None
    GlobalSecondaryIndexes: list[DynamoDBGlobalSecondaryIndexDescriptionModel] | None = None
    StreamSpecification: DynamoDBStreamSpecificationModel | None = None
    LatestStreamLabel: StrictStr | None = None
    LatestStreamArn: StrictStr | None = None
    GlobalTableVersion: StrictStr | None = None
    Replicas: list[DynamoDBReplicaDescriptionModel] | None = None
    GlobalTableWitnesses: list[DynamoDBGlobalTableWitnessDescriptionModel] | None = None
    GlobalTableSettingsReplicationMode: StrictStr | None = None
    RestoreSummary: DynamoDBRestoreSummaryModel | None = None
    SSEDescription: DynamoDBSSEDescriptionModel | None = None
    ArchivalSummary: DynamoDBArchivalSummaryModel | None = None
    TableClassSummary: DynamoDBTableClassSummaryModel | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    DisassociationProtectionEnabled: StrictBool | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughputModel | None = None
    WarmThroughput: DynamoDBTableWarmThroughputDescriptionModel | None = None
    MultiRegionConsistency: StrictStr | None = None
    VectorIndexes: list[DynamoDBVectorIndexDescriptionModel] | None = None
