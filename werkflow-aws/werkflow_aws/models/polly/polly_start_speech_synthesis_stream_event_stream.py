from __future__ import annotations
from pydantic import BaseModel
from .polly_audio_event import PollyAudioEvent
from .polly_service_failure_exception import PollyServiceFailureException
from .polly_service_quota_exceeded_exception import PollyServiceQuotaExceededException
from .polly_stream_closed_event import PollyStreamClosedEvent
from .polly_throttling_exception import PollyThrottlingException
from .polly_validation_exception import PollyValidationException


class PollyStartSpeechSynthesisStreamEventStream(BaseModel):
    AudioEvent: PollyAudioEvent | None = None
    StreamClosedEvent: PollyStreamClosedEvent | None = None
    ValidationException: PollyValidationException | None = None
    ServiceQuotaExceededException: PollyServiceQuotaExceededException | None = None
    ServiceFailureException: PollyServiceFailureException | None = None
    ThrottlingException: PollyThrottlingException | None = None
