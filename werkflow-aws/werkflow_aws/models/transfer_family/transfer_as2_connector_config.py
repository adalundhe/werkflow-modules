from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_as2_async_mdn_connector_config import TransferAs2AsyncMdnConnectorConfig


class TransferAs2ConnectorConfig(BaseModel):
    LocalProfileId: StrictStr | None = None
    PartnerProfileId: StrictStr | None = None
    MessageSubject: StrictStr | None = None
    Compression: StrictStr | None = None
    EncryptionAlgorithm: StrictStr | None = None
    SigningAlgorithm: StrictStr | None = None
    MdnSigningAlgorithm: StrictStr | None = None
    MdnResponse: StrictStr | None = None
    BasicAuthSecretId: StrictStr | None = None
    PreserveContentType: StrictStr | None = None
    AsyncMdnConfig: TransferAs2AsyncMdnConnectorConfig | None = None
