from __future__ import annotations
from pydantic import BaseModel
from .macie_reveal_configuration import MacieRevealConfiguration
from .macie_update_retrieval_configuration import MacieUpdateRetrievalConfiguration


class MacieUpdateRevealConfigurationRequest(BaseModel):
    configuration: MacieRevealConfiguration
    retrievalConfiguration: MacieUpdateRetrievalConfiguration | None = None
