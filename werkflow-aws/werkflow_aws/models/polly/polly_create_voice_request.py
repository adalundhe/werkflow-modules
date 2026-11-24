from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .polly_customer_managed_encryption import PollyCustomerManagedEncryption
from .polly_voice_creation_data import PollyVoiceCreationData


class PollyCreateVoiceRequest(BaseModel):
    Name: StrictStr
    LanguageCode: Literal['de-DE', 'en-US', 'es-US', 'fr-FR', 'hi-IN', 'it-IT', 'pt-BR']
    TermsAccepted: StrictBool
    VoiceCreationData: PollyVoiceCreationData
    CustomerManagedEncryption: PollyCustomerManagedEncryption | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
