from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_allowed_methods import CloudFrontAllowedMethods
from .cloud_front_forwarded_values import CloudFrontForwardedValues
from .cloud_front_function_associations import CloudFrontFunctionAssociations
from .cloud_front_grpc_config import CloudFrontGrpcConfig
from .cloud_front_lambda_function_associations import CloudFrontLambdaFunctionAssociations
from .cloud_front_trusted_key_groups import CloudFrontTrustedKeyGroups
from .cloud_front_trusted_signers import CloudFrontTrustedSigners


class CloudFrontDefaultCacheBehavior(BaseModel):
    TargetOriginId: StrictStr | None = None
    TrustedSigners: CloudFrontTrustedSigners | None = None
    TrustedKeyGroups: CloudFrontTrustedKeyGroups | None = None
    ViewerProtocolPolicy: StrictStr | None = None
    AllowedMethods: CloudFrontAllowedMethods | None = None
    SmoothStreaming: StrictBool | None = None
    Compress: StrictBool | None = None
    LambdaFunctionAssociations: CloudFrontLambdaFunctionAssociations | None = None
    FunctionAssociations: CloudFrontFunctionAssociations | None = None
    FieldLevelEncryptionId: StrictStr | None = None
    RealtimeLogConfigArn: StrictStr | None = None
    CachePolicyId: StrictStr | None = None
    OriginRequestPolicyId: StrictStr | None = None
    ResponseHeadersPolicyId: StrictStr | None = None
    GrpcConfig: CloudFrontGrpcConfig | None = None
    ForwardedValues: CloudFrontForwardedValues | None = None
    MinTTL: StrictInt | None = None
    DefaultTTL: StrictInt | None = None
    MaxTTL: StrictInt | None = None
