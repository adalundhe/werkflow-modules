from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_app_sync_parameters import EventBridgeAppSyncParameters
from .event_bridge_batch_parameters import EventBridgeBatchParameters
from .event_bridge_dead_letter_config import EventBridgeDeadLetterConfig
from .event_bridge_ecs_parameters import EventBridgeEcsParameters
from .event_bridge_http_parameters import EventBridgeHttpParameters
from .event_bridge_input_transformer import EventBridgeInputTransformer
from .event_bridge_kinesis_parameters import EventBridgeKinesisParameters
from .event_bridge_redshift_data_parameters import EventBridgeRedshiftDataParameters
from .event_bridge_retry_policy import EventBridgeRetryPolicy
from .event_bridge_run_command_parameters import EventBridgeRunCommandParameters
from .event_bridge_sage_maker_pipeline_parameters import EventBridgeSageMakerPipelineParameters
from .event_bridge_sqs_parameters import EventBridgeSqsParameters


class EventBridgeTarget(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Input: StrictStr | None = None
    InputPath: StrictStr | None = None
    InputTransformer: EventBridgeInputTransformer | None = None
    KinesisParameters: EventBridgeKinesisParameters | None = None
    RunCommandParameters: EventBridgeRunCommandParameters | None = None
    EcsParameters: EventBridgeEcsParameters | None = None
    BatchParameters: EventBridgeBatchParameters | None = None
    SqsParameters: EventBridgeSqsParameters | None = None
    HttpParameters: EventBridgeHttpParameters | None = None
    RedshiftDataParameters: EventBridgeRedshiftDataParameters | None = None
    SageMakerPipelineParameters: EventBridgeSageMakerPipelineParameters | None = None
    DeadLetterConfig: EventBridgeDeadLetterConfig | None = None
    RetryPolicy: EventBridgeRetryPolicy | None = None
    AppSyncParameters: EventBridgeAppSyncParameters | None = None
