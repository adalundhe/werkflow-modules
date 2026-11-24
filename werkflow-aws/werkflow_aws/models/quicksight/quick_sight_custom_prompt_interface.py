from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomPromptInterface(BaseModel):
    ModelProfileId: StrictStr | None = None
    SubscriptionId: StrictStr | None = None
    QbsAwsAccountId: StrictStr | None = None
    ResponseLength: StrictStr | None = None
    OutputStyle: StrictStr | None = None
    Identity: StrictStr | None = None
    Tone: StrictStr | None = None
    CustomInstructions: StrictStr | None = None
    promptSummary: StrictStr | None = None
