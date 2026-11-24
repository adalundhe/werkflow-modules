from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .rekognition_region_of_interest import RekognitionRegionOfInterest
from .rekognition_stream_processor_data_sharing_preference import RekognitionStreamProcessorDataSharingPreference
from .rekognition_stream_processor_settings_for_update import RekognitionStreamProcessorSettingsForUpdate


class RekognitionUpdateStreamProcessorRequest(BaseModel):
    Name: StrictStr
    SettingsForUpdate: RekognitionStreamProcessorSettingsForUpdate | None = None
    RegionsOfInterestForUpdate: list[RekognitionRegionOfInterest] | None = None
    DataSharingPreferenceForUpdate: RekognitionStreamProcessorDataSharingPreference | None = None
    ParametersToDelete: list[Literal['ConnectedHomeMinConfidence', 'RegionsOfInterest']] | None = None
