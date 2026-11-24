from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESTopicFilter(BaseModel):
    TopicName: StrictStr | None = None
    UseDefaultIfPreferenceUnavailable: StrictBool | None = None
