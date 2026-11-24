from __future__ import annotations
from pydantic import BaseModel
from .kinesis_internal_failure_exception import KinesisInternalFailureException
from .kinesis_kms_access_denied_exception import KinesisKMSAccessDeniedException
from .kinesis_kms_disabled_exception import KinesisKMSDisabledException
from .kinesis_kms_invalid_state_exception import KinesisKMSInvalidStateException
from .kinesis_kms_not_found_exception import KinesisKMSNotFoundException
from .kinesis_kms_opt_in_required import KinesisKMSOptInRequired
from .kinesis_kms_throttling_exception import KinesisKMSThrottlingException
from .kinesis_resource_in_use_exception import KinesisResourceInUseException
from .kinesis_resource_not_found_exception import KinesisResourceNotFoundException
from .kinesis_subscribe_to_shard_event import KinesisSubscribeToShardEvent


class KinesisSubscribeToShardEventStream(BaseModel):
    SubscribeToShardEvent: KinesisSubscribeToShardEvent | None = None
    ResourceNotFoundException: KinesisResourceNotFoundException | None = None
    ResourceInUseException: KinesisResourceInUseException | None = None
    KMSDisabledException: KinesisKMSDisabledException | None = None
    KMSInvalidStateException: KinesisKMSInvalidStateException | None = None
    KMSAccessDeniedException: KinesisKMSAccessDeniedException | None = None
    KMSNotFoundException: KinesisKMSNotFoundException | None = None
    KMSOptInRequired: KinesisKMSOptInRequired | None = None
    KMSThrottlingException: KinesisKMSThrottlingException | None = None
    InternalFailureException: KinesisInternalFailureException | None = None
