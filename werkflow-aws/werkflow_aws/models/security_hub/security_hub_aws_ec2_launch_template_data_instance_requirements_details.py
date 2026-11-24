from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_ec2_launch_template_data_instance_requirements_accelerator_count_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_network_interface_count_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails
from .security_hub_aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details import SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails


class SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsDetails(BaseModel):
    AcceleratorCount: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails | None = None
    AcceleratorManufacturers: list[StrictStr] | None = None
    AcceleratorNames: list[StrictStr] | None = None
    AcceleratorTotalMemoryMiB: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails | None = None
    AcceleratorTypes: list[StrictStr] | None = None
    BareMetal: StrictStr | None = None
    BaselineEbsBandwidthMbps: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails | None = None
    BurstablePerformance: StrictStr | None = None
    CpuManufacturers: list[StrictStr] | None = None
    ExcludedInstanceTypes: list[StrictStr] | None = None
    InstanceGenerations: list[StrictStr] | None = None
    LocalStorage: StrictStr | None = None
    LocalStorageTypes: list[StrictStr] | None = None
    MemoryGiBPerVCpu: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails | None = None
    MemoryMiB: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails | None = None
    NetworkInterfaceCount: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails | None = None
    OnDemandMaxPricePercentageOverLowestPrice: StrictInt | None = None
    RequireHibernateSupport: StrictBool | None = None
    SpotMaxPricePercentageOverLowestPrice: StrictInt | None = None
    TotalLocalStorageGB: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails | None = None
    VCpuCount: SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails | None = None
