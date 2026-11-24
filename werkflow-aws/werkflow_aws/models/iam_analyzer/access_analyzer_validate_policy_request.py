from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerValidatePolicyRequest(BaseModel):
    policyDocument: StrictStr
    policyType: Literal['IDENTITY_POLICY', 'RESOURCE_POLICY', 'SERVICE_CONTROL_POLICY', 'RESOURCE_CONTROL_POLICY']
    locale: Literal['DE', 'EN', 'ES', 'FR', 'IT', 'JA', 'KO', 'PT_BR', 'ZH_CN', 'ZH_TW'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    validatePolicyResourceType: Literal['AWS::S3::Bucket', 'AWS::S3::AccessPoint', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3ObjectLambda::AccessPoint', 'AWS::IAM::AssumeRolePolicyDocument', 'AWS::DynamoDB::Table'] | None = None
