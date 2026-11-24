from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_delivery_stream_encryption_configuration_input import FirehoseDeliveryStreamEncryptionConfigurationInput


class FirehoseStartDeliveryStreamEncryptionRequest(BaseModel):
    DeliveryStreamName: StrictStr
    DeliveryStreamEncryptionConfigurationInput: FirehoseDeliveryStreamEncryptionConfigurationInput | None = None
