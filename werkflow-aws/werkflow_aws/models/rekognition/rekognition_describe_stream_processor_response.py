from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .rekognition_region_of_interest import RekognitionRegionOfInterest
from .rekognition_stream_processor_data_sharing_preference import RekognitionStreamProcessorDataSharingPreference
from .rekognition_stream_processor_input import RekognitionStreamProcessorInput
from .rekognition_stream_processor_notification_channel import RekognitionStreamProcessorNotificationChannel
from .rekognition_stream_processor_output import RekognitionStreamProcessorOutput
from .rekognition_stream_processor_settings import RekognitionStreamProcessorSettings


class RekognitionDescribeStreamProcessorResponse(BaseModel):
    Name: StrictStr | None = None
    StreamProcessorArn: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    Input: RekognitionStreamProcessorInput | None = None
    Output: RekognitionStreamProcessorOutput | None = None
    RoleArn: StrictStr | None = None
    Settings: RekognitionStreamProcessorSettings | None = None
    NotificationChannel: RekognitionStreamProcessorNotificationChannel | None = None
    KmsKeyId: StrictStr | None = None
    RegionsOfInterest: list[RekognitionRegionOfInterest] | None = None
    DataSharingPreference: RekognitionStreamProcessorDataSharingPreference | None = None
    ResponseMetadata: dict[str, Any] | None = None
