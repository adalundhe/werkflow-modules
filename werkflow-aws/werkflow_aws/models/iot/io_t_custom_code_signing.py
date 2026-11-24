from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_code_signing_certificate_chain import IoTCodeSigningCertificateChain
from .io_t_code_signing_signature import IoTCodeSigningSignature


class IoTCustomCodeSigning(BaseModel):
    signature: IoTCodeSigningSignature | None = None
    certificateChain: IoTCodeSigningCertificateChain | None = None
    hashAlgorithm: StrictStr | None = None
    signatureAlgorithm: StrictStr | None = None
