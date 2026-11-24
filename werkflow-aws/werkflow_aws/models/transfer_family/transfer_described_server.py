from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .transfer_endpoint_details import TransferEndpointDetails
from .transfer_identity_provider_details import TransferIdentityProviderDetails
from .transfer_protocol_details import TransferProtocolDetails
from .transfer_s3_storage_options import TransferS3StorageOptions
from .transfer_tag import TransferTag
from .transfer_workflow_details import TransferWorkflowDetails


class TransferDescribedServer(BaseModel):
    Arn: StrictStr | None = None
    Certificate: StrictStr | None = None
    ProtocolDetails: TransferProtocolDetails | None = None
    Domain: StrictStr | None = None
    EndpointDetails: TransferEndpointDetails | None = None
    EndpointType: StrictStr | None = None
    HostKeyFingerprint: StrictStr | None = None
    IdentityProviderDetails: TransferIdentityProviderDetails | None = None
    IdentityProviderType: StrictStr | None = None
    LoggingRole: StrictStr | None = None
    PostAuthenticationLoginBanner: StrictStr | None = None
    PreAuthenticationLoginBanner: StrictStr | None = None
    Protocols: list[StrictStr] | None = None
    SecurityPolicyName: StrictStr | None = None
    ServerId: StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    UserCount: StrictInt | None = None
    WorkflowDetails: TransferWorkflowDetails | None = None
    StructuredLogDestinations: list[StrictStr] | None = None
    S3StorageOptions: TransferS3StorageOptions | None = None
    As2ServiceManagedEgressIpAddresses: list[StrictStr] | None = None
    IpAddressType: StrictStr | None = None
