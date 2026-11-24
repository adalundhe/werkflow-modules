from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_sage_maker_notebook_instance_metadata_service_configuration_details import SecurityHubAwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails


class SecurityHubAwsSageMakerNotebookInstanceDetails(BaseModel):
    AcceleratorTypes: list[StrictStr] | None = None
    AdditionalCodeRepositories: list[StrictStr] | None = None
    DefaultCodeRepository: StrictStr | None = None
    DirectInternetAccess: StrictStr | None = None
    FailureReason: StrictStr | None = None
    InstanceMetadataServiceConfiguration: SecurityHubAwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails | None = None
    InstanceType: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    NotebookInstanceArn: StrictStr | None = None
    NotebookInstanceLifecycleConfigName: StrictStr | None = None
    NotebookInstanceName: StrictStr | None = None
    NotebookInstanceStatus: StrictStr | None = None
    PlatformIdentifier: StrictStr | None = None
    RoleArn: StrictStr | None = None
    RootAccess: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    SubnetId: StrictStr | None = None
    Url: StrictStr | None = None
    VolumeSizeInGB: StrictInt | None = None
