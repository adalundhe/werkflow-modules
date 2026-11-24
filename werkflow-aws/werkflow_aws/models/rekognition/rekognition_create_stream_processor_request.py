from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rekognition_region_of_interest import RekognitionRegionOfInterest
from .rekognition_stream_processor_data_sharing_preference import RekognitionStreamProcessorDataSharingPreference
from .rekognition_stream_processor_input import RekognitionStreamProcessorInput
from .rekognition_stream_processor_notification_channel import RekognitionStreamProcessorNotificationChannel
from .rekognition_stream_processor_output import RekognitionStreamProcessorOutput
from .rekognition_stream_processor_settings import RekognitionStreamProcessorSettings


class RekognitionCreateStreamProcessorRequest(BaseModel):
    Input: RekognitionStreamProcessorInput
    Output: RekognitionStreamProcessorOutput
    Name: StrictStr
    Settings: RekognitionStreamProcessorSettings
    RoleArn: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
    NotificationChannel: RekognitionStreamProcessorNotificationChannel | None = None
    KmsKeyId: StrictStr | None = None
    RegionsOfInterest: list[RekognitionRegionOfInterest] | None = None
    DataSharingPreference: RekognitionStreamProcessorDataSharingPreference | None = None
