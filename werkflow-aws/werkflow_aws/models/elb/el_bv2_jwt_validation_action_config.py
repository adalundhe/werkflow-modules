from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_jwt_validation_action_additional_claim import ELBv2JwtValidationActionAdditionalClaim


class ELBv2JwtValidationActionConfig(BaseModel):
    JwksEndpoint: StrictStr | None = None
    Issuer: StrictStr | None = None
    AdditionalClaims: list[ELBv2JwtValidationActionAdditionalClaim] | None = None
