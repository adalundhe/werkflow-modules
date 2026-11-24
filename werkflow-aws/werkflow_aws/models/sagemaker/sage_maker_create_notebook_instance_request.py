from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_instance_metadata_service_configuration_model import SageMakerInstanceMetadataServiceConfigurationModel
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateNotebookInstanceRequest(BaseModel):
    NotebookInstanceName: StrictStr
    InstanceType: StrictStr
    RoleArn: StrictStr
    SubnetId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    IpAddressType: Literal['ipv4', 'dualstack'] | None = None
    KmsKeyId: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    LifecycleConfigName: StrictStr | None = None
    DirectInternetAccess: Literal['Enabled', 'Disabled'] | None = None
    VolumeSizeInGB: StrictInt | None = None
    AcceleratorTypes: list[Literal['ml.eia1.medium', 'ml.eia1.large', 'ml.eia1.xlarge', 'ml.eia2.medium', 'ml.eia2.large', 'ml.eia2.xlarge']] | None = None
    DefaultCodeRepository: StrictStr | None = None
    AdditionalCodeRepositories: list[StrictStr] | None = None
    RootAccess: Literal['Enabled', 'Disabled'] | None = None
    PlatformIdentifier: StrictStr | None = None
    InstanceMetadataServiceConfiguration: SageMakerInstanceMetadataServiceConfigurationModel | None = None
