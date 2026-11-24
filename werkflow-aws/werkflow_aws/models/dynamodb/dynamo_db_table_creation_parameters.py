from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_definition_model import DynamoDBAttributeDefinitionModel
from .dynamo_db_global_secondary_index_model import DynamoDBGlobalSecondaryIndexModel
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_on_demand_throughput_model import DynamoDBOnDemandThroughputModel
from .dynamo_db_provisioned_throughput_model import DynamoDBProvisionedThroughputModel
from .dynamo_dbsse_specification_model import DynamoDBSSESpecificationModel
from .dynamo_db_vector_index_model import DynamoDBVectorIndexModel


class DynamoDBTableCreationParameters(BaseModel):
    TableName: StrictStr | None = None
    AttributeDefinitions: list[DynamoDBAttributeDefinitionModel] | None = None
    KeySchema: list[DynamoDBKeySchemaElementModel] | None = None
    BillingMode: StrictStr | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputModel | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughputModel | None = None
    SSESpecification: DynamoDBSSESpecificationModel | None = None
    GlobalSecondaryIndexes: list[DynamoDBGlobalSecondaryIndexModel] | None = None
    VectorIndexes: list[DynamoDBVectorIndexModel] | None = None
