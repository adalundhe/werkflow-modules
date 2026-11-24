from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .scheduler_dead_letter_config import SchedulerDeadLetterConfig
from .scheduler_ecs_parameters import SchedulerEcsParameters
from .scheduler_event_bridge_parameters import SchedulerEventBridgeParameters
from .scheduler_event_bridge_put_events_v2_parameters import SchedulerEventBridgePutEventsV2Parameters
from .scheduler_event_bridge_put_raw_events_parameters import SchedulerEventBridgePutRawEventsParameters
from .scheduler_kinesis_parameters import SchedulerKinesisParameters
from .scheduler_retry_policy import SchedulerRetryPolicy
from .scheduler_sage_maker_pipeline_parameters import SchedulerSageMakerPipelineParameters
from .scheduler_sqs_parameters import SchedulerSqsParameters


class SchedulerTarget(BaseModel):
    Arn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    DeadLetterConfig: SchedulerDeadLetterConfig | None = None
    RetryPolicy: SchedulerRetryPolicy | None = None
    Input: StrictStr | None = None
    EcsParameters: SchedulerEcsParameters | None = None
    EventBridgeParameters: SchedulerEventBridgeParameters | None = None
    EventBridgePutEventsV2Parameters: SchedulerEventBridgePutEventsV2Parameters | None = None
    EventBridgePutRawEventsParameters: SchedulerEventBridgePutRawEventsParameters | None = None
    KinesisParameters: SchedulerKinesisParameters | None = None
    SageMakerPipelineParameters: SchedulerSageMakerPipelineParameters | None = None
    SqsParameters: SchedulerSqsParameters | None = None
