from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_credit_specification_request import EC2CreditSpecificationRequest
from .ec2_elastic_gpu_specification import EC2ElasticGpuSpecification
from .ec2_instance_requirements_request import EC2InstanceRequirementsRequest
from .ec2_launch_template_block_device_mapping_request import EC2LaunchTemplateBlockDeviceMappingRequest
from .ec2_launch_template_capacity_reservation_specification_request import EC2LaunchTemplateCapacityReservationSpecificationRequest
from .ec2_launch_template_cpu_options_request import EC2LaunchTemplateCpuOptionsRequest
from .ec2_launch_template_elastic_inference_accelerator import EC2LaunchTemplateElasticInferenceAccelerator
from .ec2_launch_template_enclave_options_request import EC2LaunchTemplateEnclaveOptionsRequest
from .ec2_launch_template_hibernation_options_request import EC2LaunchTemplateHibernationOptionsRequest
from .ec2_launch_template_iam_instance_profile_specification_request import EC2LaunchTemplateIamInstanceProfileSpecificationRequest
from .ec2_launch_template_instance_maintenance_options_request import EC2LaunchTemplateInstanceMaintenanceOptionsRequest
from .ec2_launch_template_instance_market_options_request import EC2LaunchTemplateInstanceMarketOptionsRequest
from .ec2_launch_template_instance_metadata_options_request import EC2LaunchTemplateInstanceMetadataOptionsRequest
from .ec2_launch_template_instance_network_interface_specification_request import EC2LaunchTemplateInstanceNetworkInterfaceSpecificationRequest
from .ec2_launch_template_instance_secondary_interface_specification_request import EC2LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest
from .ec2_launch_template_license_configuration_request import EC2LaunchTemplateLicenseConfigurationRequest
from .ec2_launch_template_network_performance_options_request import EC2LaunchTemplateNetworkPerformanceOptionsRequest
from .ec2_launch_template_placement_request import EC2LaunchTemplatePlacementRequest
from .ec2_launch_template_private_dns_name_options_request import EC2LaunchTemplatePrivateDnsNameOptionsRequest
from .ec2_launch_template_tag_specification_request import EC2LaunchTemplateTagSpecificationRequest
from .ec2_launch_templates_monitoring_request import EC2LaunchTemplatesMonitoringRequest
from .ec2_operator_request import EC2OperatorRequest


class EC2RequestLaunchTemplateData(BaseModel):
    KernelId: StrictStr | None = None
    EbsOptimized: StrictBool | None = None
    IamInstanceProfile: EC2LaunchTemplateIamInstanceProfileSpecificationRequest | None = None
    BlockDeviceMappings: list[EC2LaunchTemplateBlockDeviceMappingRequest] | None = None
    NetworkInterfaces: list[EC2LaunchTemplateInstanceNetworkInterfaceSpecificationRequest] | None = None
    ImageId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    KeyName: StrictStr | None = None
    Monitoring: EC2LaunchTemplatesMonitoringRequest | None = None
    Placement: EC2LaunchTemplatePlacementRequest | None = None
    RamDiskId: StrictStr | None = None
    DisableApiTermination: StrictBool | None = None
    InstanceInitiatedShutdownBehavior: Literal['stop', 'terminate'] | None = None
    UserData: StrictStr | None = None
    TagSpecifications: list[EC2LaunchTemplateTagSpecificationRequest] | None = None
    ElasticGpuSpecifications: list[EC2ElasticGpuSpecification] | None = None
    ElasticInferenceAccelerators: list[EC2LaunchTemplateElasticInferenceAccelerator] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    InstanceMarketOptions: EC2LaunchTemplateInstanceMarketOptionsRequest | None = None
    CreditSpecification: EC2CreditSpecificationRequest | None = None
    CpuOptions: EC2LaunchTemplateCpuOptionsRequest | None = None
    CapacityReservationSpecification: EC2LaunchTemplateCapacityReservationSpecificationRequest | None = None
    LicenseSpecifications: list[EC2LaunchTemplateLicenseConfigurationRequest] | None = None
    HibernationOptions: EC2LaunchTemplateHibernationOptionsRequest | None = None
    MetadataOptions: EC2LaunchTemplateInstanceMetadataOptionsRequest | None = None
    EnclaveOptions: EC2LaunchTemplateEnclaveOptionsRequest | None = None
    InstanceRequirements: EC2InstanceRequirementsRequest | None = None
    PrivateDnsNameOptions: EC2LaunchTemplatePrivateDnsNameOptionsRequest | None = None
    MaintenanceOptions: EC2LaunchTemplateInstanceMaintenanceOptionsRequest | None = None
    DisableApiStop: StrictBool | None = None
    Operator: EC2OperatorRequest | None = None
    NetworkPerformanceOptions: EC2LaunchTemplateNetworkPerformanceOptionsRequest | None = None
    SecondaryInterfaces: list[EC2LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest] | None = None
