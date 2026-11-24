from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_credit_specification import EC2CreditSpecification
from .ec2_elastic_gpu_specification_response import EC2ElasticGpuSpecificationResponse
from .ec2_instance_requirements import EC2InstanceRequirements
from .ec2_launch_template_block_device_mapping import EC2LaunchTemplateBlockDeviceMapping
from .ec2_launch_template_capacity_reservation_specification_response import EC2LaunchTemplateCapacityReservationSpecificationResponse
from .ec2_launch_template_cpu_options import EC2LaunchTemplateCpuOptions
from .ec2_launch_template_elastic_inference_accelerator_response import EC2LaunchTemplateElasticInferenceAcceleratorResponse
from .ec2_launch_template_enclave_options import EC2LaunchTemplateEnclaveOptions
from .ec2_launch_template_hibernation_options import EC2LaunchTemplateHibernationOptions
from .ec2_launch_template_iam_instance_profile_specification import EC2LaunchTemplateIamInstanceProfileSpecification
from .ec2_launch_template_instance_maintenance_options import EC2LaunchTemplateInstanceMaintenanceOptions
from .ec2_launch_template_instance_market_options import EC2LaunchTemplateInstanceMarketOptions
from .ec2_launch_template_instance_metadata_options import EC2LaunchTemplateInstanceMetadataOptions
from .ec2_launch_template_instance_network_interface_specification import EC2LaunchTemplateInstanceNetworkInterfaceSpecification
from .ec2_launch_template_instance_secondary_interface_specification import EC2LaunchTemplateInstanceSecondaryInterfaceSpecification
from .ec2_launch_template_license_configuration import EC2LaunchTemplateLicenseConfiguration
from .ec2_launch_template_network_performance_options import EC2LaunchTemplateNetworkPerformanceOptions
from .ec2_launch_template_placement import EC2LaunchTemplatePlacement
from .ec2_launch_template_private_dns_name_options import EC2LaunchTemplatePrivateDnsNameOptions
from .ec2_launch_template_tag_specification import EC2LaunchTemplateTagSpecification
from .ec2_launch_templates_monitoring import EC2LaunchTemplatesMonitoring
from .ec2_operator_response import EC2OperatorResponse


class EC2ResponseLaunchTemplateData(BaseModel):
    KernelId: StrictStr | None = None
    EbsOptimized: StrictBool | None = None
    IamInstanceProfile: EC2LaunchTemplateIamInstanceProfileSpecification | None = None
    BlockDeviceMappings: list[EC2LaunchTemplateBlockDeviceMapping] | None = None
    NetworkInterfaces: list[EC2LaunchTemplateInstanceNetworkInterfaceSpecification] | None = None
    ImageId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    KeyName: StrictStr | None = None
    Monitoring: EC2LaunchTemplatesMonitoring | None = None
    Placement: EC2LaunchTemplatePlacement | None = None
    RamDiskId: StrictStr | None = None
    DisableApiTermination: StrictBool | None = None
    InstanceInitiatedShutdownBehavior: StrictStr | None = None
    UserData: StrictStr | None = None
    TagSpecifications: list[EC2LaunchTemplateTagSpecification] | None = None
    ElasticGpuSpecifications: list[EC2ElasticGpuSpecificationResponse] | None = None
    ElasticInferenceAccelerators: list[EC2LaunchTemplateElasticInferenceAcceleratorResponse] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    InstanceMarketOptions: EC2LaunchTemplateInstanceMarketOptions | None = None
    CreditSpecification: EC2CreditSpecification | None = None
    CpuOptions: EC2LaunchTemplateCpuOptions | None = None
    CapacityReservationSpecification: EC2LaunchTemplateCapacityReservationSpecificationResponse | None = None
    LicenseSpecifications: list[EC2LaunchTemplateLicenseConfiguration] | None = None
    HibernationOptions: EC2LaunchTemplateHibernationOptions | None = None
    MetadataOptions: EC2LaunchTemplateInstanceMetadataOptions | None = None
    EnclaveOptions: EC2LaunchTemplateEnclaveOptions | None = None
    InstanceRequirements: EC2InstanceRequirements | None = None
    PrivateDnsNameOptions: EC2LaunchTemplatePrivateDnsNameOptions | None = None
    MaintenanceOptions: EC2LaunchTemplateInstanceMaintenanceOptions | None = None
    DisableApiStop: StrictBool | None = None
    Operator: EC2OperatorResponse | None = None
    NetworkPerformanceOptions: EC2LaunchTemplateNetworkPerformanceOptions | None = None
    SecondaryInterfaces: list[EC2LaunchTemplateInstanceSecondaryInterfaceSpecification] | None = None
