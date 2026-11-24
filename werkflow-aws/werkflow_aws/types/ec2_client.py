from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class EC2Client(ABC):

    @abstractmethod
    def describe_volumes(
        self,
        *,
        VolumeIds: list[str] | None = None,
        IncludeManagedResources: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_volume(
        self,
        *,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
        Encrypted: bool | None = None,
        Iops: int | None = None,
        KmsKeyId: str | None = None,
        OutpostArn: str | None = None,
        Size: int | None = None,
        SnapshotId: str | None = None,
        VolumeType: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        MultiAttachEnabled: bool | None = None,
        Throughput: int | None = None,
        ClientToken: str | None = None,
        VolumeInitializationRate: int | None = None,
        Operator: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_volume(
        self,
        *,
        VolumeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_volume(
        self,
        *,
        Device: str,
        InstanceId: str,
        VolumeId: str,
        EbsCardIndex: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_volume(
        self,
        *,
        VolumeId: str,
        Device: str | None = None,
        Force: bool | None = None,
        InstanceId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instances(
        self,
        *,
        InstanceIds: list[str] | None = None,
        IncludeManagedResources: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def run_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: list[dict[str, Any]] | None = None,
        ImageId: str | None = None,
        InstanceType: str | None = None,
        Ipv6AddressCount: int | None = None,
        Ipv6Addresses: list[dict[str, Any]] | None = None,
        KernelId: str | None = None,
        KeyName: str | None = None,
        Monitoring: dict[str, Any] | None = None,
        Placement: dict[str, Any] | None = None,
        RamdiskId: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        SecurityGroups: list[str] | None = None,
        SubnetId: str | None = None,
        UserData: str | None = None,
        ElasticGpuSpecification: list[dict[str, Any]] | None = None,
        ElasticInferenceAccelerators: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        LaunchTemplate: dict[str, Any] | None = None,
        InstanceMarketOptions: dict[str, Any] | None = None,
        CreditSpecification: dict[str, Any] | None = None,
        CpuOptions: dict[str, Any] | None = None,
        CapacityReservationSpecification: dict[str, Any] | None = None,
        HibernationOptions: dict[str, Any] | None = None,
        LicenseSpecifications: list[dict[str, Any]] | None = None,
        MetadataOptions: dict[str, Any] | None = None,
        EnclaveOptions: dict[str, Any] | None = None,
        PrivateDnsNameOptions: dict[str, Any] | None = None,
        MaintenanceOptions: dict[str, Any] | None = None,
        DisableApiStop: bool | None = None,
        EnablePrimaryIpv6: bool | None = None,
        NetworkPerformanceOptions: dict[str, Any] | None = None,
        Operator: dict[str, Any] | None = None,
        SecondaryInterfaces: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        DisableApiTermination: bool | None = None,
        InstanceInitiatedShutdownBehavior: str | None = None,
        PrivateIpAddress: str | None = None,
        ClientToken: str | None = None,
        AdditionalInfo: str | None = None,
        NetworkInterfaces: list[dict[str, Any]] | None = None,
        IamInstanceProfile: dict[str, Any] | None = None,
        EbsOptimized: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_instances(
        self,
        *,
        InstanceIds: list[str],
        AdditionalInfo: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_instances(
        self,
        *,
        InstanceIds: list[str],
        Hibernate: bool | None = None,
        SkipOsShutdown: bool | None = None,
        DryRun: bool | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reboot_instances(
        self,
        *,
        InstanceIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_instances(
        self,
        *,
        InstanceIds: list[str],
        Force: bool | None = None,
        SkipOsShutdown: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpcs(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        VpcIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_subnets(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        SubnetIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_groups(
        self,
        *,
        GroupIds: list[str] | None = None,
        GroupNames: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        VpcId: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_group(
        self,
        *,
        GroupId: str | None = None,
        GroupName: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshots(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        OwnerIds: list[str] | None = None,
        RestorableByUserIds: list[str] | None = None,
        SnapshotIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshot(
        self,
        *,
        VolumeId: str,
        Description: str | None = None,
        OutpostArn: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        Location: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_snapshot(
        self,
        *,
        SnapshotId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tags(
        self,
        *,
        Resources: list[str],
        Tags: list[dict[str, Any]],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        Resources: list[str],
        DryRun: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_key_pairs(
        self,
        *,
        KeyNames: list[str] | None = None,
        KeyPairIds: list[str] | None = None,
        IncludePublicKey: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_address_transfer(
        self,
        *,
        Address: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_capacity_reservation_billing_ownership(
        self,
        *,
        CapacityReservationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_reserved_instances_exchange_quote(
        self,
        *,
        ReservedInstanceIds: list[str],
        DryRun: bool | None = None,
        TargetConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_transit_gateway_client_vpn_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str | None = None,
        TransitGatewayAttachmentId: str | None = None,
        SubnetIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_vpc_endpoint_connections(
        self,
        *,
        ServiceId: str,
        VpcEndpointIds: list[str],
        DryRun: bool | None = None,
        TransitGatewayAttachmentIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_vpc_peering_connection(
        self,
        *,
        VpcPeeringConnectionId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def advertise_byoip_cidr(
        self,
        *,
        Cidr: str,
        Asn: str | None = None,
        DryRun: bool | None = None,
        NetworkBorderGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_address(
        self,
        *,
        Domain: str | None = None,
        Address: str | None = None,
        PublicIpv4Pool: str | None = None,
        NetworkBorderGroup: str | None = None,
        CustomerOwnedIpv4Pool: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        IpamPoolId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_hosts(
        self,
        *,
        InstanceFamily: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        HostRecovery: str | None = None,
        OutpostArn: str | None = None,
        HostMaintenance: str | None = None,
        AssetIds: list[str] | None = None,
        AvailabilityZoneId: str | None = None,
        CpuOptions: dict[str, Any] | None = None,
        AutoPlacement: str | None = None,
        ClientToken: str | None = None,
        InstanceType: str | None = None,
        Quantity: int | None = None,
        AvailabilityZone: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def allocate_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        Cidr: str | None = None,
        NetmaskLength: int | None = None,
        ClientToken: str | None = None,
        Description: str | None = None,
        PreviewNextCidr: bool | None = None,
        AllowedCidrs: list[str] | None = None,
        DisallowedCidrs: list[str] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def apply_security_groups_to_client_vpn_target_network(
        self,
        *,
        ClientVpnEndpointId: str,
        VpcId: str,
        SecurityGroupIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assign_ipv6_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv6PrefixCount: int | None = None,
        Ipv6Prefixes: list[str] | None = None,
        Ipv6Addresses: list[str] | None = None,
        Ipv6AddressCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assign_private_ip_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv4Prefixes: list[str] | None = None,
        Ipv4PrefixCount: int | None = None,
        PrivateIpAddresses: list[str] | None = None,
        SecondaryPrivateIpAddressCount: int | None = None,
        AllowReassignment: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assign_private_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        PrivateIpAddresses: list[str] | None = None,
        PrivateIpAddressCount: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_address(
        self,
        *,
        AllocationId: str | None = None,
        InstanceId: str | None = None,
        PublicIp: str | None = None,
        DryRun: bool | None = None,
        NetworkInterfaceId: str | None = None,
        PrivateIpAddress: str | None = None,
        AllowReassociation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_application_status_check(
        self,
        *,
        ApplicationStatusCheckId: str,
        TargetTagAssociations: list[dict[str, Any]] | None = None,
        InstanceIds: list[str] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_capacity_reservation_billing_owner(
        self,
        *,
        CapacityReservationId: str,
        UnusedReservationBillingOwnerId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_client_vpn_target_network(
        self,
        *,
        ClientVpnEndpointId: str,
        SubnetId: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_dhcp_options(
        self,
        *,
        DhcpOptionsId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_enclave_certificate_iam_role(
        self,
        *,
        CertificateArn: str,
        RoleArn: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_iam_instance_profile(
        self,
        *,
        IamInstanceProfile: dict[str, Any],
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        AssociationTarget: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_ipam_byoasn(
        self,
        *,
        Asn: str,
        Cidr: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_ipam_resource_discovery(
        self,
        *,
        IpamId: str,
        IpamResourceDiscoveryId: str,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_kms_key_id(
        self,
        *,
        KmsKeyId: str,
        SnapshotId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        AllocationIds: list[str],
        PrivateIpAddresses: list[str] | None = None,
        DryRun: bool | None = None,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_networking_flex_cost_allocation_policy(
        self,
        *,
        FcaPolicyId: str,
        NetworkResourceIds: list[str] | None = None,
        NetworkResourceScope: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_route_server(
        self,
        *,
        RouteServerId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_route_table(
        self,
        *,
        RouteTableId: str,
        GatewayId: str | None = None,
        PublicIpv4Pool: str | None = None,
        DryRun: bool | None = None,
        SubnetId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_security_group_vpc(
        self,
        *,
        GroupId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_subnet_cidr_block(
        self,
        *,
        SubnetId: str,
        Ipv6IpamPoolId: str | None = None,
        Ipv6NetmaskLength: int | None = None,
        Ipv6CidrBlock: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        TransitGatewayAttachmentId: str,
        SubnetIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_trunk_interface(
        self,
        *,
        BranchInterfaceId: str,
        TrunkInterfaceId: str,
        VlanId: int | None = None,
        GreKey: int | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_vpc_cidr_block(
        self,
        *,
        VpcId: str,
        CidrBlock: str | None = None,
        Ipv6CidrBlockNetworkBorderGroup: str | None = None,
        Ipv6Pool: str | None = None,
        Ipv6CidrBlock: str | None = None,
        Ipv4IpamPoolId: str | None = None,
        Ipv4NetmaskLength: int | None = None,
        Ipv6IpamPoolId: str | None = None,
        Ipv6NetmaskLength: int | None = None,
        AmazonProvidedIpv6CidrBlock: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_classic_link_vpc(
        self,
        *,
        InstanceId: str,
        VpcId: str,
        Groups: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_image_watermark(
        self,
        *,
        ImageId: str,
        WatermarkName: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_internet_gateway(
        self,
        *,
        InternetGatewayId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_network_interface(
        self,
        *,
        NetworkInterfaceId: str,
        InstanceId: str,
        DeviceIndex: int,
        NetworkCardIndex: int | None = None,
        EnaSrdSpecification: dict[str, Any] | None = None,
        EnaQueueCount: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessInstanceId: str,
        VerifiedAccessTrustProviderId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_vpn_gateway(
        self,
        *,
        VpcId: str,
        VpnGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_client_vpn_ingress(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str | None = None,
        AuthorizeAllGroups: bool | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_security_group_egress(
        self,
        *,
        GroupId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        SourceSecurityGroupName: str | None = None,
        SourceSecurityGroupOwnerId: str | None = None,
        IpProtocol: str | None = None,
        FromPort: int | None = None,
        ToPort: int | None = None,
        CidrIp: str | None = None,
        IpPermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def authorize_security_group_ingress(
        self,
        *,
        CidrIp: str | None = None,
        FromPort: int | None = None,
        GroupId: str | None = None,
        GroupName: str | None = None,
        IpPermissions: list[dict[str, Any]] | None = None,
        IpProtocol: str | None = None,
        SourceSecurityGroupName: str | None = None,
        SourceSecurityGroupOwnerId: str | None = None,
        ToPort: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_modify_ipam_routing_policy_registrations(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DeltaJson: str,
        DryRun: bool | None = None,
        Force: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def bundle_instance(
        self,
        *,
        InstanceId: str,
        Storage: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_bundle_task(
        self,
        *,
        BundleId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        DryRun: bool | None = None,
        ApplyCancellationCharges: str | None = None,
        QuoteId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_capacity_reservation_fleets(
        self,
        *,
        CapacityReservationFleetIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_conversion_task(
        self,
        *,
        ConversionTaskId: str,
        DryRun: bool | None = None,
        ReasonMessage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_declarative_policies_report(
        self,
        *,
        ReportId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_export_task(
        self,
        *,
        ExportTaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_image_launch_permission(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_import_task(
        self,
        *,
        CancelReason: str | None = None,
        DryRun: bool | None = None,
        ImportTaskId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_reserved_instances_listing(
        self,
        *,
        ReservedInstancesListingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_spot_fleet_requests(
        self,
        *,
        SpotFleetRequestIds: list[str],
        TerminateInstances: bool,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_spot_instance_requests(
        self,
        *,
        SpotInstanceRequestIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_product_instance(
        self,
        *,
        InstanceId: str,
        ProductCode: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_fpga_image(
        self,
        *,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        Name: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_image(
        self,
        *,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: str | None = None,
        Description: str | None = None,
        Encrypted: bool | None = None,
        KmsKeyId: str | None = None,
        DestinationOutpostArn: str | None = None,
        CopyImageTags: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        SnapshotCopyCompletionDurationMinutes: int | None = None,
        DestinationAvailabilityZone: str | None = None,
        DestinationAvailabilityZoneId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_snapshot(
        self,
        *,
        SourceRegion: str,
        SourceSnapshotId: str,
        Description: str | None = None,
        DestinationOutpostArn: str | None = None,
        DestinationRegion: str | None = None,
        Encrypted: bool | None = None,
        KmsKeyId: str | None = None,
        PresignedUrl: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        CompletionDurationMinutes: int | None = None,
        DestinationAvailabilityZone: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def copy_volumes(
        self,
        *,
        SourceVolumeId: str,
        Iops: int | None = None,
        Size: int | None = None,
        VolumeType: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        MultiAttachEnabled: bool | None = None,
        Throughput: int | None = None,
        ClientToken: str | None = None,
        Encrypted: bool | None = None,
        KmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_application_status_check(
        self,
        *,
        Protocol: str,
        Port: int,
        HealthCheckPaths: list[dict[str, Any]] | None = None,
        Aggregation: str | None = None,
        Path: str | None = None,
        DeviceIndex: int | None = None,
        IpVersion: str | None = None,
        IpScope: str | None = None,
        Interval: int | None = None,
        Timeout: int | None = None,
        FailureThreshold: int | None = None,
        SuccessThreshold: int | None = None,
        StatusCodeMatcher: str | None = None,
        InitializationGracePeriodSeconds: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_manager_data_export(
        self,
        *,
        S3BucketName: str,
        Schedule: str,
        OutputFormat: str,
        S3BucketPrefix: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_reservation(
        self,
        *,
        InstanceType: str,
        InstancePlatform: str,
        InstanceCount: int,
        ClientToken: str | None = None,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
        Tenancy: str | None = None,
        EbsOptimized: bool | None = None,
        EphemeralStorage: bool | None = None,
        EndDate: datetime.datetime | str | None = None,
        EndDateType: str | None = None,
        InstanceMatchCriteria: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        OutpostArn: str | None = None,
        PlacementGroupArn: str | None = None,
        StartDate: datetime.datetime | str | None = None,
        CommitmentDuration: int | None = None,
        DeliveryPreference: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_reservation_by_splitting(
        self,
        *,
        SourceCapacityReservationId: str,
        InstanceCount: int,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_reservation_cancellation_quote(
        self,
        *,
        CapacityReservationId: str,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_reservation_date_change_quote(
        self,
        *,
        CapacityReservationId: str,
        NewStartDate: datetime.datetime | str,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_reservation_fleet(
        self,
        *,
        TotalTargetCapacity: int,
        AllocationStrategy: str | None = None,
        ClientToken: str | None = None,
        InstanceTypeSpecifications: list[dict[str, Any]] | None = None,
        InstanceRequirements: dict[str, Any] | None = None,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
        Tenancy: str | None = None,
        EndDate: datetime.datetime | str | None = None,
        InstanceMatchCriteria: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_carrier_gateway(
        self,
        *,
        VpcId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_client_vpn_endpoint(
        self,
        *,
        ServerCertificateArn: str,
        AuthenticationOptions: list[dict[str, Any]],
        ConnectionLogOptions: dict[str, Any],
        ClientCidrBlock: str | None = None,
        DnsServers: list[str] | None = None,
        TransportProtocol: str | None = None,
        VpnPort: int | None = None,
        Description: str | None = None,
        SplitTunnel: bool | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        SecurityGroupIds: list[str] | None = None,
        VpcId: str | None = None,
        SelfServicePortal: str | None = None,
        ClientConnectOptions: dict[str, Any] | None = None,
        SessionTimeoutHours: int | None = None,
        ClientLoginBannerOptions: dict[str, Any] | None = None,
        ClientRouteEnforcementOptions: dict[str, Any] | None = None,
        DisconnectOnSessionTimeout: bool | None = None,
        EndpointIpAddressType: str | None = None,
        TrafficIpAddressType: str | None = None,
        TransitGatewayConfiguration: dict[str, Any] | None = None,
        DevicePostureOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_client_vpn_route(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_coip_cidr(
        self,
        *,
        Cidr: str,
        CoipPoolId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_coip_pool(
        self,
        *,
        LocalGatewayRouteTableId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_customer_gateway(
        self,
        *,
        Type: str,
        BgpAsn: int | None = None,
        PublicIp: str | None = None,
        CertificateArn: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DeviceName: str | None = None,
        IpAddress: str | None = None,
        BgpAsnExtended: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_default_subnet(
        self,
        *,
        AvailabilityZone: str | None = None,
        DryRun: bool | None = None,
        Ipv6Native: bool | None = None,
        AvailabilityZoneId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_default_vpc(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_delegate_mac_volume_ownership_task(
        self,
        *,
        InstanceId: str,
        MacCredentials: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dhcp_options(
        self,
        *,
        DhcpConfigurations: list[dict[str, Any]],
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_egress_only_internet_gateway(
        self,
        *,
        VpcId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fleet(
        self,
        *,
        LaunchTemplateConfigs: list[dict[str, Any]],
        TargetCapacitySpecification: dict[str, Any],
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        SpotOptions: dict[str, Any] | None = None,
        OnDemandOptions: dict[str, Any] | None = None,
        ReservedCapacityOptions: dict[str, Any] | None = None,
        ExcessCapacityTerminationPolicy: str | None = None,
        TerminateInstancesWithExpiration: bool | None = None,
        Type: str | None = None,
        ValidFrom: datetime.datetime | str | None = None,
        ValidUntil: datetime.datetime | str | None = None,
        ReplaceUnhealthyInstances: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        Context: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_flow_logs(
        self,
        *,
        ResourceIds: list[str],
        ResourceType: str,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        DeliverLogsPermissionArn: str | None = None,
        DeliverCrossAccountRole: str | None = None,
        LogGroupName: str | None = None,
        TrafficType: str | None = None,
        LogDestinationType: str | None = None,
        LogDestination: str | None = None,
        LogFormat: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        MaxAggregationInterval: int | None = None,
        DestinationOptions: dict[str, Any] | None = None,
        TagFieldSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_fpga_image(
        self,
        *,
        InputStorageLocation: dict[str, Any],
        DryRun: bool | None = None,
        LogsStorageLocation: dict[str, Any] | None = None,
        Description: str | None = None,
        Name: str | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_image(
        self,
        *,
        InstanceId: str,
        Name: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        SnapshotLocation: str | None = None,
        BootModeOverride: str | None = None,
        DryRun: bool | None = None,
        Description: str | None = None,
        NoReboot: bool | None = None,
        BlockDeviceMappings: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_image_usage_report(
        self,
        *,
        ImageId: str,
        ResourceTypes: list[dict[str, Any]],
        DryRun: bool | None = None,
        AccountIds: list[str] | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_connect_endpoint(
        self,
        *,
        SubnetId: str,
        DryRun: bool | None = None,
        SecurityGroupIds: list[str] | None = None,
        PreserveClientIp: bool | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        IpAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_event_window(
        self,
        *,
        DryRun: bool | None = None,
        Name: str | None = None,
        TimeRanges: list[dict[str, Any]] | None = None,
        CronExpression: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_export_task(
        self,
        *,
        InstanceId: str,
        TargetEnvironment: str,
        ExportToS3Task: dict[str, Any],
        TagSpecifications: list[dict[str, Any]] | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_internet_gateway(
        self,
        *,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_interruptible_capacity_reservation_allocation(
        self,
        *,
        CapacityReservationId: str,
        InstanceCount: int,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ZeroSizePreference: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam(
        self,
        *,
        DryRun: bool | None = None,
        Description: str | None = None,
        OperatingRegions: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        Tier: str | None = None,
        EnablePrivateGua: bool | None = None,
        MeteredAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_external_resource_verification_token(
        self,
        *,
        IpamId: str,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_internet_registry_association(
        self,
        *,
        IpamId: str,
        Rir: str,
        OrganizationHandle: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_policy(
        self,
        *,
        IpamId: str,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_pool(
        self,
        *,
        IpamScopeId: str,
        AddressFamily: str,
        DryRun: bool | None = None,
        Locale: str | None = None,
        SourceIpamPoolId: str | None = None,
        Description: str | None = None,
        AutoImport: bool | None = None,
        PubliclyAdvertisable: bool | None = None,
        AllocationMinNetmaskLength: int | None = None,
        AllocationMaxNetmaskLength: int | None = None,
        AllocationDefaultNetmaskLength: int | None = None,
        AllocationResourceTags: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        AwsService: str | None = None,
        PublicIpSource: str | None = None,
        SourceResource: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_prefix_list_resolver(
        self,
        *,
        IpamId: str,
        AddressFamily: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        Rules: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_prefix_list_resolver_target(
        self,
        *,
        IpamPrefixListResolverId: str,
        PrefixListId: str,
        PrefixListRegion: str,
        TrackLatestVersion: bool,
        DryRun: bool | None = None,
        DesiredVersion: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_resource_discovery(
        self,
        *,
        DryRun: bool | None = None,
        Description: str | None = None,
        OperatingRegions: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_routing_policy_registration(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        Cidr: str,
        Asns: list[str],
        DryRun: bool | None = None,
        PermitMoreSpecificAnnouncements: bool | None = None,
        MaxLength: int | None = None,
        Description: str | None = None,
        Force: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ipam_scope(
        self,
        *,
        IpamId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        ExternalAuthorityConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_key_pair(
        self,
        *,
        KeyName: str,
        KeyType: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        KeyFormat: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_launch_template(
        self,
        *,
        LaunchTemplateName: str,
        LaunchTemplateData: dict[str, Any],
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        VersionDescription: str | None = None,
        Operator: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_launch_template_version(
        self,
        *,
        LaunchTemplateData: dict[str, Any],
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        LaunchTemplateId: str | None = None,
        LaunchTemplateName: str | None = None,
        SourceVersion: str | None = None,
        VersionDescription: str | None = None,
        ResolveAlias: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str | None = None,
        LocalGatewayVirtualInterfaceGroupId: str | None = None,
        DryRun: bool | None = None,
        NetworkInterfaceId: str | None = None,
        DestinationPrefixListId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_local_gateway_route_table(
        self,
        *,
        LocalGatewayId: str,
        Mode: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_local_gateway_route_table_virtual_interface_group_association(
        self,
        *,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_local_gateway_route_table_vpc_association(
        self,
        *,
        LocalGatewayRouteTableId: str,
        VpcId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_local_gateway_virtual_interface(
        self,
        *,
        LocalGatewayVirtualInterfaceGroupId: str,
        OutpostLagId: str,
        Vlan: int,
        LocalAddress: str,
        PeerAddress: str,
        PeerBgpAsn: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        PeerBgpAsnExtended: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_local_gateway_virtual_interface_group(
        self,
        *,
        LocalGatewayId: str,
        LocalBgpAsn: int | None = None,
        LocalBgpAsnExtended: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_mac_system_integrity_protection_modification_task(
        self,
        *,
        InstanceId: str,
        MacSystemIntegrityProtectionStatus: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        MacCredentials: str | None = None,
        MacSystemIntegrityProtectionConfiguration: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_managed_prefix_list(
        self,
        *,
        PrefixListName: str,
        MaxEntries: int,
        AddressFamily: str,
        DryRun: bool | None = None,
        Entries: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_metric_category(
        self,
        *,
        Metrics: list[str],
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_nat_gateway(
        self,
        *,
        AvailabilityMode: str | None = None,
        AllocationId: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        SubnetId: str | None = None,
        VpcId: str | None = None,
        AvailabilityZoneAddresses: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ConnectivityType: str | None = None,
        PrivateIpAddress: str | None = None,
        SecondaryAllocationIds: list[str] | None = None,
        SecondaryPrivateIpAddresses: list[str] | None = None,
        SecondaryPrivateIpAddressCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_acl(
        self,
        *,
        VpcId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_acl_entry(
        self,
        *,
        NetworkAclId: str,
        RuleNumber: int,
        Protocol: str,
        RuleAction: str,
        Egress: bool,
        DryRun: bool | None = None,
        CidrBlock: str | None = None,
        Ipv6CidrBlock: str | None = None,
        IcmpTypeCode: dict[str, Any] | None = None,
        PortRange: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_insights_access_scope(
        self,
        *,
        ClientToken: str,
        MatchPaths: list[dict[str, Any]] | None = None,
        ExcludePaths: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_insights_path(
        self,
        *,
        Source: str,
        Protocol: str,
        ClientToken: str,
        SourceIp: str | None = None,
        DestinationIp: str | None = None,
        Destination: str | None = None,
        DestinationPort: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        FilterAtSource: dict[str, Any] | None = None,
        FilterAtDestination: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_interface(
        self,
        *,
        SubnetId: str,
        Ipv4Prefixes: list[dict[str, Any]] | None = None,
        Ipv4PrefixCount: int | None = None,
        Ipv6Prefixes: list[dict[str, Any]] | None = None,
        Ipv6PrefixCount: int | None = None,
        InterfaceType: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        EnablePrimaryIpv6: bool | None = None,
        ConnectionTrackingSpecification: dict[str, Any] | None = None,
        Operator: dict[str, Any] | None = None,
        Description: str | None = None,
        PrivateIpAddress: str | None = None,
        Groups: list[str] | None = None,
        PrivateIpAddresses: list[dict[str, Any]] | None = None,
        SecondaryPrivateIpAddressCount: int | None = None,
        Ipv6Addresses: list[dict[str, Any]] | None = None,
        Ipv6AddressCount: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_network_interface_permission(
        self,
        *,
        NetworkInterfaceId: str,
        Permission: str,
        AwsAccountId: str | None = None,
        AwsService: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_networking_flex_cost_allocation_policy(
        self,
        *,
        NetworkResourceType: str,
        NatFcaPolicyDocument: dict[str, Any] | None = None,
        InstanceFcaPolicyDocument: dict[str, Any] | None = None,
        PcxFcaPolicyDocument: dict[str, Any] | None = None,
        ShowBackEnabled: bool | None = None,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_placement_group(
        self,
        *,
        PartitionCount: int | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        SpreadLevel: str | None = None,
        LinkedGroupId: str | None = None,
        Operator: dict[str, Any] | None = None,
        ParentGroupId: str | None = None,
        DryRun: bool | None = None,
        GroupName: str | None = None,
        Strategy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_public_ipv4_pool(
        self,
        *,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        NetworkBorderGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_replace_root_volume_task(
        self,
        *,
        InstanceId: str,
        SnapshotId: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ImageId: str | None = None,
        DeleteReplacedRootVolume: bool | None = None,
        VolumeInitializationRate: int | None = None,
        VolumeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_reserved_instances_listing(
        self,
        *,
        ReservedInstancesId: str,
        InstanceCount: int,
        PriceSchedules: list[dict[str, Any]],
        ClientToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_restore_image_task(
        self,
        *,
        Bucket: str,
        ObjectKey: str,
        Name: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route(
        self,
        *,
        RouteTableId: str,
        DestinationPrefixListId: str | None = None,
        VpcEndpointId: str | None = None,
        TransitGatewayId: str | None = None,
        LocalGatewayId: str | None = None,
        CarrierGatewayId: str | None = None,
        CoreNetworkArn: str | None = None,
        OdbNetworkArn: str | None = None,
        DryRun: bool | None = None,
        DestinationCidrBlock: str | None = None,
        GatewayId: str | None = None,
        DestinationIpv6CidrBlock: str | None = None,
        EgressOnlyInternetGatewayId: str | None = None,
        InstanceId: str | None = None,
        NetworkInterfaceId: str | None = None,
        VpcPeeringConnectionId: str | None = None,
        NatGatewayId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route_server(
        self,
        *,
        AmazonSideAsn: int,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        PersistRoutes: str | None = None,
        PersistRoutesDuration: int | None = None,
        SnsNotificationsEnabled: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route_server_endpoint(
        self,
        *,
        RouteServerId: str,
        SubnetId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route_server_peer(
        self,
        *,
        RouteServerEndpointId: str,
        PeerAddress: str,
        BgpOptions: dict[str, Any],
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_route_table(
        self,
        *,
        VpcId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_secondary_network(
        self,
        *,
        Ipv4CidrBlock: str,
        NetworkType: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_secondary_subnet(
        self,
        *,
        Ipv4CidrBlock: str,
        SecondaryNetworkId: str,
        ClientToken: str | None = None,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_snapshots(
        self,
        *,
        InstanceSpecification: dict[str, Any],
        Description: str | None = None,
        OutpostArn: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        CopyTagsFromSource: str | None = None,
        Location: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_spot_datafeed_subscription(
        self,
        *,
        Bucket: str,
        DryRun: bool | None = None,
        Prefix: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_store_image_task(
        self,
        *,
        ImageId: str,
        Bucket: str,
        S3ObjectTags: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subnet(
        self,
        *,
        VpcId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        AvailabilityZone: str | None = None,
        AvailabilityZoneId: str | None = None,
        CidrBlock: str | None = None,
        Ipv6CidrBlock: str | None = None,
        OutpostArn: str | None = None,
        Ipv6Native: bool | None = None,
        Ipv4IpamPoolId: str | None = None,
        Ipv4NetmaskLength: int | None = None,
        Ipv6IpamPoolId: str | None = None,
        Ipv6NetmaskLength: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_subnet_cidr_reservation(
        self,
        *,
        SubnetId: str,
        Cidr: str,
        ReservationType: str,
        Description: str | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_mirror_filter(
        self,
        *,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterId: str,
        TrafficDirection: str,
        RuleNumber: int,
        RuleAction: str,
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: dict[str, Any] | None = None,
        SourcePortRange: dict[str, Any] | None = None,
        Protocol: int | None = None,
        Description: str | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_mirror_session(
        self,
        *,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: int | None = None,
        VirtualNetworkId: int | None = None,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_mirror_target(
        self,
        *,
        NetworkInterfaceId: str | None = None,
        NetworkLoadBalancerArn: str | None = None,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        GatewayLoadBalancerEndpointId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway(
        self,
        *,
        Description: str | None = None,
        Options: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_connect(
        self,
        *,
        TransportTransitGatewayAttachmentId: str,
        Options: dict[str, Any],
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_connect_peer(
        self,
        *,
        TransitGatewayAttachmentId: str,
        PeerAddress: str,
        InsideCidrBlocks: list[str],
        TransitGatewayAddress: str | None = None,
        BgpOptions: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_metering_policy(
        self,
        *,
        TransitGatewayId: str,
        MiddleboxAttachmentIds: list[str] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_metering_policy_entry(
        self,
        *,
        TransitGatewayMeteringPolicyId: str,
        PolicyRuleNumber: int,
        MeteredAccount: str,
        SourceTransitGatewayAttachmentId: str | None = None,
        SourceTransitGatewayAttachmentType: str | None = None,
        SourceCidrBlock: str | None = None,
        SourcePortRange: str | None = None,
        DestinationTransitGatewayAttachmentId: str | None = None,
        DestinationTransitGatewayAttachmentType: str | None = None,
        DestinationCidrBlock: str | None = None,
        DestinationPortRange: str | None = None,
        Protocol: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayId: str,
        Options: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_network_function_attachment(
        self,
        *,
        TransitGatewayId: str,
        ServiceName: str,
        AvailabilityZones: list[str] | None = None,
        AvailabilityZoneIds: list[str] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayId: str,
        PeerTransitGatewayId: str,
        PeerAccountId: str,
        PeerRegion: str,
        Options: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_policy_table_entry(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        PolicyRuleNumber: str,
        TargetRouteTableId: str,
        PolicyRule: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str | None = None,
        Blackhole: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_route(
        self,
        *,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str | None = None,
        Blackhole: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_route_table(
        self,
        *,
        TransitGatewayId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_route_table_announcement(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PeeringAttachmentId: str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: list[str],
        Options: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_verified_access_endpoint(
        self,
        *,
        VerifiedAccessGroupId: str,
        EndpointType: str,
        AttachmentType: str,
        DomainCertificateArn: str | None = None,
        ApplicationDomain: str | None = None,
        EndpointDomainPrefix: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        LoadBalancerOptions: dict[str, Any] | None = None,
        NetworkInterfaceOptions: dict[str, Any] | None = None,
        Description: str | None = None,
        PolicyDocument: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        SseSpecification: dict[str, Any] | None = None,
        RdsOptions: dict[str, Any] | None = None,
        CidrOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_verified_access_group(
        self,
        *,
        VerifiedAccessInstanceId: str,
        Description: str | None = None,
        PolicyDocument: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        SseSpecification: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_verified_access_instance(
        self,
        *,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        FIPSEnabled: bool | None = None,
        CidrEndpointsCustomSubDomain: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_verified_access_trust_provider(
        self,
        *,
        TrustProviderType: str,
        PolicyReferenceName: str,
        UserTrustProviderType: str | None = None,
        DeviceTrustProviderType: str | None = None,
        OidcOptions: dict[str, Any] | None = None,
        DeviceOptions: dict[str, Any] | None = None,
        Description: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        SseSpecification: dict[str, Any] | None = None,
        NativeApplicationOidcOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc(
        self,
        *,
        CidrBlock: str | None = None,
        Ipv6Pool: str | None = None,
        Ipv6CidrBlock: str | None = None,
        Ipv4IpamPoolId: str | None = None,
        Ipv4NetmaskLength: int | None = None,
        Ipv6IpamPoolId: str | None = None,
        Ipv6NetmaskLength: int | None = None,
        Ipv6CidrBlockNetworkBorderGroup: str | None = None,
        VpcEncryptionControl: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        InstanceTenancy: str | None = None,
        AmazonProvidedIpv6CidrBlock: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_block_public_access_exclusion(
        self,
        *,
        InternetGatewayExclusionMode: str,
        DryRun: bool | None = None,
        SubnetId: str | None = None,
        VpcId: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_encryption_control(
        self,
        *,
        VpcId: str,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_endpoint(
        self,
        *,
        VpcId: str,
        DryRun: bool | None = None,
        VpcEndpointType: str | None = None,
        ServiceName: str | None = None,
        PolicyDocument: str | None = None,
        RouteTableIds: list[str] | None = None,
        SubnetIds: list[str] | None = None,
        SecurityGroupIds: list[str] | None = None,
        IpAddressType: str | None = None,
        DnsOptions: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        PrivateDnsEnabled: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        SubnetConfigurations: list[dict[str, Any]] | None = None,
        ServiceNetworkArn: str | None = None,
        ResourceConfigurationArn: str | None = None,
        ServiceRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_endpoint_connection_notification(
        self,
        *,
        ConnectionNotificationArn: str,
        ConnectionEvents: list[str],
        DryRun: bool | None = None,
        ServiceId: str | None = None,
        VpcEndpointId: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_endpoint_service_configuration(
        self,
        *,
        DryRun: bool | None = None,
        AcceptanceRequired: bool | None = None,
        PrivateDnsName: str | None = None,
        NetworkLoadBalancerArns: list[str] | None = None,
        GatewayLoadBalancerArns: list[str] | None = None,
        SupportedIpAddressTypes: list[str] | None = None,
        SupportedRegions: list[str] | None = None,
        ClientToken: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_peering_connection(
        self,
        *,
        VpcId: str,
        PeerRegion: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        RequesterPeeringConnectionOptions: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        PeerVpcId: str | None = None,
        PeerOwnerId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpn_concentrator(
        self,
        *,
        Type: str,
        TransitGatewayId: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpn_connection(
        self,
        *,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: str | None = None,
        TransitGatewayId: str | None = None,
        VpnConcentratorId: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        PreSharedKeyStorage: str | None = None,
        DryRun: bool | None = None,
        Options: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpn_connection_route(
        self,
        *,
        DestinationCidrBlock: str,
        VpnConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpn_gateway(
        self,
        *,
        Type: str,
        AvailabilityZone: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        AmazonSideAsn: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_application_status_check(
        self,
        *,
        ApplicationStatusCheckId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_capacity_manager_data_export(
        self,
        *,
        CapacityManagerDataExportId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_carrier_gateway(
        self,
        *,
        CarrierGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_client_vpn_endpoint(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_client_vpn_endpoint_authorization_policy(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_client_vpn_route(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_coip_cidr(
        self,
        *,
        Cidr: str,
        CoipPoolId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_coip_pool(
        self,
        *,
        CoipPoolId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_customer_gateway(
        self,
        *,
        CustomerGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dhcp_options(
        self,
        *,
        DhcpOptionsId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_egress_only_internet_gateway(
        self,
        *,
        EgressOnlyInternetGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fleets(
        self,
        *,
        FleetIds: list[str],
        TerminateInstances: bool,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_flow_logs(
        self,
        *,
        FlowLogIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_fpga_image(
        self,
        *,
        FpgaImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image_usage_report(
        self,
        *,
        ReportId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance_connect_endpoint(
        self,
        *,
        InstanceConnectEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        DryRun: bool | None = None,
        ForceDelete: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_internet_gateway(
        self,
        *,
        InternetGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam(
        self,
        *,
        IpamId: str,
        DryRun: bool | None = None,
        Cascade: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_external_resource_verification_token(
        self,
        *,
        IpamExternalResourceVerificationTokenId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_internet_registry_association(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_policy(
        self,
        *,
        IpamPolicyId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_pool(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        Cascade: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_prefix_list_resolver(
        self,
        *,
        IpamPrefixListResolverId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_prefix_list_resolver_target(
        self,
        *,
        IpamPrefixListResolverTargetId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_resource_discovery(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_routing_policy_registration(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        Cidr: str,
        DryRun: bool | None = None,
        Force: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ipam_scope(
        self,
        *,
        IpamScopeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_key_pair(
        self,
        *,
        KeyName: str | None = None,
        KeyPairId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_launch_template(
        self,
        *,
        DryRun: bool | None = None,
        LaunchTemplateId: str | None = None,
        LaunchTemplateName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_launch_template_versions(
        self,
        *,
        Versions: list[str],
        DryRun: bool | None = None,
        LaunchTemplateId: str | None = None,
        LaunchTemplateName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str | None = None,
        DryRun: bool | None = None,
        DestinationPrefixListId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_local_gateway_route_table(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_local_gateway_route_table_virtual_interface_group_association(
        self,
        *,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_local_gateway_route_table_vpc_association(
        self,
        *,
        LocalGatewayRouteTableVpcAssociationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_local_gateway_virtual_interface(
        self,
        *,
        LocalGatewayVirtualInterfaceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_local_gateway_virtual_interface_group(
        self,
        *,
        LocalGatewayVirtualInterfaceGroupId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_managed_prefix_list(
        self,
        *,
        PrefixListId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric_category(
        self,
        *,
        MetricCategoryId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_nat_gateway(
        self,
        *,
        NatGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_acl(
        self,
        *,
        NetworkAclId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_acl_entry(
        self,
        *,
        NetworkAclId: str,
        RuleNumber: int,
        Egress: bool,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_insights_access_scope(
        self,
        *,
        NetworkInsightsAccessScopeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_insights_access_scope_analysis(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_insights_analysis(
        self,
        *,
        NetworkInsightsAnalysisId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_insights_path(
        self,
        *,
        NetworkInsightsPathId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_interface(
        self,
        *,
        NetworkInterfaceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_network_interface_permission(
        self,
        *,
        NetworkInterfacePermissionId: str,
        Force: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_networking_flex_cost_allocation_policies(
        self,
        *,
        FcaPolicyIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_placement_group(
        self,
        *,
        GroupName: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_public_ipv4_pool(
        self,
        *,
        PoolId: str,
        DryRun: bool | None = None,
        NetworkBorderGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_queued_reserved_instances(
        self,
        *,
        ReservedInstancesIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route(
        self,
        *,
        RouteTableId: str,
        DestinationPrefixListId: str | None = None,
        DryRun: bool | None = None,
        DestinationCidrBlock: str | None = None,
        DestinationIpv6CidrBlock: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_server(
        self,
        *,
        RouteServerId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_server_endpoint(
        self,
        *,
        RouteServerEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_server_peer(
        self,
        *,
        RouteServerPeerId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_route_table(
        self,
        *,
        RouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_secondary_network(
        self,
        *,
        SecondaryNetworkId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_secondary_subnet(
        self,
        *,
        SecondarySubnetId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_spot_datafeed_subscription(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subnet(
        self,
        *,
        SubnetId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_subnet_cidr_reservation(
        self,
        *,
        SubnetCidrReservationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_mirror_filter(
        self,
        *,
        TrafficMirrorFilterId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterRuleId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_mirror_session(
        self,
        *,
        TrafficMirrorSessionId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_mirror_target(
        self,
        *,
        TrafficMirrorTargetId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway(
        self,
        *,
        TransitGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_client_vpn_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_connect(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_connect_peer(
        self,
        *,
        TransitGatewayConnectPeerId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_metering_policy(
        self,
        *,
        TransitGatewayMeteringPolicyId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_metering_policy_entry(
        self,
        *,
        TransitGatewayMeteringPolicyId: str,
        PolicyRuleNumber: int,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_network_function_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_policy_table_entry(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        PolicyRuleNumber: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_route(
        self,
        *,
        TransitGatewayRouteTableId: str,
        DestinationCidrBlock: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_route_table_announcement(
        self,
        *,
        TransitGatewayRouteTableAnnouncementId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_verified_access_endpoint(
        self,
        *,
        VerifiedAccessEndpointId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_verified_access_group(
        self,
        *,
        VerifiedAccessGroupId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_verified_access_instance(
        self,
        *,
        VerifiedAccessInstanceId: str,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessTrustProviderId: str,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc(
        self,
        *,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_block_public_access_exclusion(
        self,
        *,
        ExclusionId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_encryption_control(
        self,
        *,
        VpcEncryptionControlId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_endpoint_connection_notifications(
        self,
        *,
        ConnectionNotificationIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_endpoint_service_configurations(
        self,
        *,
        ServiceIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_endpoints(
        self,
        *,
        VpcEndpointIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_peering_connection(
        self,
        *,
        VpcPeeringConnectionId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpn_concentrator(
        self,
        *,
        VpnConcentratorId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpn_connection(
        self,
        *,
        VpnConnectionId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpn_connection_route(
        self,
        *,
        DestinationCidrBlock: str,
        VpnConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpn_gateway(
        self,
        *,
        VpnGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprovision_byoip_cidr(
        self,
        *,
        Cidr: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprovision_ipam_byoasn(
        self,
        *,
        IpamId: str,
        Asn: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprovision_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        Cidr: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deprovision_public_ipv4_pool_cidr(
        self,
        *,
        PoolId: str,
        Cidr: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_image(
        self,
        *,
        ImageId: str,
        DeleteAssociatedSnapshots: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_instance_event_notification_attributes(
        self,
        *,
        InstanceTagAttribute: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_transit_gateway_multicast_group_members(
        self,
        *,
        TransitGatewayMulticastDomainId: str | None = None,
        GroupIpAddress: str | None = None,
        NetworkInterfaceIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_transit_gateway_multicast_group_sources(
        self,
        *,
        TransitGatewayMulticastDomainId: str | None = None,
        GroupIpAddress: str | None = None,
        NetworkInterfaceIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_attributes(
        self,
        *,
        DryRun: bool | None = None,
        AttributeNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_vpc_encryption_control(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_address_transfers(
        self,
        *,
        AllocationIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_addresses(
        self,
        *,
        PublicIps: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        AllocationIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_addresses_attribute(
        self,
        *,
        AllocationIds: list[str] | None = None,
        Attribute: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_aggregate_id_format(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_status(
        self,
        *,
        InstanceIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_status_check_associations(
        self,
        *,
        ApplicationStatusCheckIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_application_status_checks(
        self,
        *,
        ApplicationStatusCheckIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IncludeAll: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_availability_zones(
        self,
        *,
        ZoneNames: list[str] | None = None,
        ZoneIds: list[str] | None = None,
        AllAvailabilityZones: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_aws_network_performance_metric_subscriptions(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_bundle_tasks(
        self,
        *,
        BundleIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_byoip_cidrs(
        self,
        *,
        MaxResults: int,
        DryRun: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_block_extension_history(
        self,
        *,
        CapacityReservationIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_block_extension_offerings(
        self,
        *,
        CapacityBlockExtensionDurationHours: int,
        CapacityReservationId: str,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_block_offerings(
        self,
        *,
        CapacityDurationHours: int,
        DryRun: bool | None = None,
        InstanceType: str | None = None,
        InstanceCount: int | None = None,
        StartDateRange: datetime.datetime | str | None = None,
        EndDateRange: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        UltraserverType: str | None = None,
        UltraserverCount: int | None = None,
        AllAvailabilityZones: bool | None = None,
        InstanceTypePreferences: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_block_status(
        self,
        *,
        CapacityBlockIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_blocks(
        self,
        *,
        CapacityBlockIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_manager_data_exports(
        self,
        *,
        CapacityManagerDataExportIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation_billing_requests(
        self,
        *,
        Role: str,
        CapacityReservationIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation_cancellation_quotes(
        self,
        *,
        CapacityReservationCancellationQuoteIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation_date_change_quotes(
        self,
        *,
        CapacityReservationModificationQuoteIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation_fleets(
        self,
        *,
        CapacityReservationFleetIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation_topology(
        self,
        *,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CapacityReservationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservations(
        self,
        *,
        CapacityReservationIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_carrier_gateways(
        self,
        *,
        CarrierGatewayIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_classic_link_instances(
        self,
        *,
        DryRun: bool | None = None,
        InstanceIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_vpn_authorization_rules(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_vpn_connections(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_vpn_endpoints(
        self,
        *,
        ClientVpnEndpointIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_vpn_routes(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_client_vpn_target_networks(
        self,
        *,
        ClientVpnEndpointId: str,
        AssociationIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_coip_pools(
        self,
        *,
        PoolIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_conversion_tasks(
        self,
        *,
        DryRun: bool | None = None,
        ConversionTaskIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_customer_gateways(
        self,
        *,
        CustomerGatewayIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_declarative_policies_reports(
        self,
        *,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ReportIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dhcp_options(
        self,
        *,
        DhcpOptionsIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_egress_only_internet_gateways(
        self,
        *,
        DryRun: bool | None = None,
        EgressOnlyInternetGatewayIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_elastic_gpus(
        self,
        *,
        ElasticGpuIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_export_image_tasks(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ExportImageTaskIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_export_tasks(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        ExportTaskIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fast_launch_images(
        self,
        *,
        ImageIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fast_snapshot_restores(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_history(
        self,
        *,
        FleetId: str,
        StartTime: datetime.datetime | str,
        DryRun: bool | None = None,
        EventType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleet_instances(
        self,
        *,
        FleetId: str,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fleets(
        self,
        *,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        FleetIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flow_logs(
        self,
        *,
        DryRun: bool | None = None,
        Filter: list[dict[str, Any]] | None = None,
        FlowLogIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fpga_image_attribute(
        self,
        *,
        FpgaImageId: str,
        Attribute: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_fpga_images(
        self,
        *,
        DryRun: bool | None = None,
        FpgaImageIds: list[str] | None = None,
        Owners: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_host_reservation_offerings(
        self,
        *,
        Filter: list[dict[str, Any]] | None = None,
        MaxDuration: int | None = None,
        MaxResults: int | None = None,
        MinDuration: int | None = None,
        NextToken: str | None = None,
        OfferingId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_host_reservations(
        self,
        *,
        Filter: list[dict[str, Any]] | None = None,
        HostReservationIdSet: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hosts(
        self,
        *,
        HostIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filter: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_iam_instance_profile_associations(
        self,
        *,
        AssociationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_id_format(
        self,
        *,
        Resource: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_identity_id_format(
        self,
        *,
        PrincipalArn: str,
        Resource: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_attribute(
        self,
        *,
        Attribute: str,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_references(
        self,
        *,
        ImageIds: list[str],
        IncludeAllResourceTypes: bool | None = None,
        ResourceTypes: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_usage_report_entries(
        self,
        *,
        ImageIds: list[str] | None = None,
        ReportIds: list[str] | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_usage_reports(
        self,
        *,
        ImageIds: list[str] | None = None,
        ReportIds: list[str] | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_images(
        self,
        *,
        ExecutableUsers: list[str] | None = None,
        ImageIds: list[str] | None = None,
        Owners: list[str] | None = None,
        IncludeDeprecated: bool | None = None,
        IncludeDisabled: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_import_image_tasks(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ImportTaskIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_import_snapshot_tasks(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ImportTaskIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_attribute(
        self,
        *,
        InstanceId: str,
        Attribute: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_connect_endpoints(
        self,
        *,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        InstanceConnectEndpointIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_credit_specifications(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        InstanceIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_event_notification_attributes(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_event_windows(
        self,
        *,
        DryRun: bool | None = None,
        InstanceEventWindowIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_image_metadata(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        InstanceIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_sql_ha_history_states(
        self,
        *,
        InstanceIds: list[str] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_sql_ha_states(
        self,
        *,
        InstanceIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_status(
        self,
        *,
        InstanceIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IncludeManagedResources: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        IncludeAllInstances: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_topology(
        self,
        *,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        InstanceIds: list[str] | None = None,
        GroupNames: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_type_offerings(
        self,
        *,
        DryRun: bool | None = None,
        LocationType: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_types(
        self,
        *,
        DryRun: bool | None = None,
        InstanceTypes: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IncludeUnsupportedInRegion: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_internet_gateways(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        InternetGatewayIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_byoasn(
        self,
        *,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_external_resource_verification_tokens(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IpamExternalResourceVerificationTokenIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_internet_registry_associations(
        self,
        *,
        DryRun: bool | None = None,
        IpamInternetRegistryAssociationIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_policies(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamPolicyIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_pool_allocations(
        self,
        *,
        DryRun: bool | None = None,
        IpamPoolAllocationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_pools(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamPoolIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_prefix_list_resolver_targets(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamPrefixListResolverTargetIds: list[str] | None = None,
        IpamPrefixListResolverId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_prefix_list_resolvers(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamPrefixListResolverIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_resource_discoveries(
        self,
        *,
        DryRun: bool | None = None,
        IpamResourceDiscoveryIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_resource_discovery_associations(
        self,
        *,
        DryRun: bool | None = None,
        IpamResourceDiscoveryAssociationIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipam_scopes(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamScopeIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipams(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ipv6_pools(
        self,
        *,
        PoolIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_launch_template_versions(
        self,
        *,
        DryRun: bool | None = None,
        LaunchTemplateId: str | None = None,
        LaunchTemplateName: str | None = None,
        Versions: list[str] | None = None,
        MinVersion: str | None = None,
        MaxVersion: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ResolveAlias: bool | None = None,
        IncludeManagedResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_launch_templates(
        self,
        *,
        DryRun: bool | None = None,
        LaunchTemplateIds: list[str] | None = None,
        LaunchTemplateNames: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IncludeManagedResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        *,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_local_gateway_route_table_vpc_associations(
        self,
        *,
        LocalGatewayRouteTableVpcAssociationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_local_gateway_route_tables(
        self,
        *,
        LocalGatewayRouteTableIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_local_gateway_virtual_interface_groups(
        self,
        *,
        LocalGatewayVirtualInterfaceGroupIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_local_gateway_virtual_interfaces(
        self,
        *,
        LocalGatewayVirtualInterfaceIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_local_gateways(
        self,
        *,
        LocalGatewayIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_locked_snapshots(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SnapshotIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mac_hosts(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        HostIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mac_modification_tasks(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MacModificationTaskIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_managed_prefix_lists(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        PrefixListIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metric_categories(
        self,
        *,
        MetricCategoryIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_moving_addresses(
        self,
        *,
        DryRun: bool | None = None,
        PublicIps: list[str] | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_nat_gateways(
        self,
        *,
        DryRun: bool | None = None,
        Filter: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NatGatewayIds: list[str] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_acls(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        NetworkAclIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_insights_access_scope_analyses(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisIds: list[str] | None = None,
        NetworkInsightsAccessScopeId: str | None = None,
        AnalysisStartTimeBegin: datetime.datetime | str | None = None,
        AnalysisStartTimeEnd: datetime.datetime | str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_insights_access_scopes(
        self,
        *,
        NetworkInsightsAccessScopeIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_insights_analyses(
        self,
        *,
        NetworkInsightsAnalysisIds: list[str] | None = None,
        NetworkInsightsPathId: str | None = None,
        AnalysisStartTime: datetime.datetime | str | None = None,
        AnalysisEndTime: datetime.datetime | str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_insights_paths(
        self,
        *,
        NetworkInsightsPathIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        DryRun: bool | None = None,
        Attribute: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_interface_permissions(
        self,
        *,
        NetworkInterfacePermissionIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_network_interfaces(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IncludeManagedResources: bool | None = None,
        DryRun: bool | None = None,
        NetworkInterfaceIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_networking_flex_cost_allocation_policies(
        self,
        *,
        FcaPolicyIds: list[str] | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_networking_flex_cost_allocation_policy_associations(
        self,
        *,
        FcaPolicyAssociationIds: list[str] | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_outpost_lags(
        self,
        *,
        OutpostLagIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_placement_groups(
        self,
        *,
        GroupIds: list[str] | None = None,
        DryRun: bool | None = None,
        GroupNames: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_prefix_lists(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        PrefixListIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_principal_id_format(
        self,
        *,
        DryRun: bool | None = None,
        Resources: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_public_ipv4_pools(
        self,
        *,
        PoolIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_regions(
        self,
        *,
        RegionNames: list[str] | None = None,
        AllRegions: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_replace_root_volume_tasks(
        self,
        *,
        ReplaceRootVolumeTaskIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_instances(
        self,
        *,
        OfferingClass: str | None = None,
        ReservedInstancesIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        OfferingType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_instances_listings(
        self,
        *,
        ReservedInstancesId: str | None = None,
        ReservedInstancesListingId: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_instances_modifications(
        self,
        *,
        ReservedInstancesModificationIds: list[str] | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_instances_offerings(
        self,
        *,
        AvailabilityZone: str | None = None,
        IncludeMarketplace: bool | None = None,
        InstanceType: str | None = None,
        MaxDuration: int | None = None,
        MaxInstanceCount: int | None = None,
        MinDuration: int | None = None,
        OfferingClass: str | None = None,
        ProductDescription: str | None = None,
        ReservedInstancesOfferingIds: list[str] | None = None,
        AvailabilityZoneId: str | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        InstanceTenancy: str | None = None,
        OfferingType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_route_server_endpoints(
        self,
        *,
        RouteServerEndpointIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_route_server_peers(
        self,
        *,
        RouteServerPeerIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_route_servers(
        self,
        *,
        RouteServerIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_route_tables(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        RouteTableIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduled_instance_availability(
        self,
        *,
        FirstSlotStartTimeRange: dict[str, Any],
        Recurrence: dict[str, Any],
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        MaxSlotDurationInHours: int | None = None,
        MinSlotDurationInHours: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scheduled_instances(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ScheduledInstanceIds: list[str] | None = None,
        SlotStartTimeRange: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_secondary_interfaces(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SecondaryInterfaceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_secondary_networks(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SecondaryNetworkIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_secondary_subnets(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SecondarySubnetIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_group_references(
        self,
        *,
        GroupId: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_group_rules(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        SecurityGroupRuleIds: list[str] | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_group_vpc_associations(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_link_virtual_interfaces(
        self,
        *,
        ServiceLinkVirtualInterfaceIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_attribute(
        self,
        *,
        Attribute: str,
        SnapshotId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_snapshot_tier_status(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spot_datafeed_subscription(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spot_fleet_instances(
        self,
        *,
        SpotFleetRequestId: str,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spot_fleet_request_history(
        self,
        *,
        SpotFleetRequestId: str,
        StartTime: datetime.datetime | str,
        DryRun: bool | None = None,
        EventType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spot_fleet_requests(
        self,
        *,
        DryRun: bool | None = None,
        SpotFleetRequestIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spot_instance_requests(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        SpotInstanceRequestIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spot_price_history(
        self,
        *,
        AvailabilityZoneId: str | None = None,
        DryRun: bool | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        InstanceTypes: list[str] | None = None,
        ProductDescriptions: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        AvailabilityZone: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stale_security_groups(
        self,
        *,
        VpcId: str,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_store_image_tasks(
        self,
        *,
        ImageIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tags(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_traffic_mirror_filter_rules(
        self,
        *,
        TrafficMirrorFilterRuleIds: list[str] | None = None,
        TrafficMirrorFilterId: str | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_traffic_mirror_filters(
        self,
        *,
        TrafficMirrorFilterIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_traffic_mirror_sessions(
        self,
        *,
        TrafficMirrorSessionIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_traffic_mirror_targets(
        self,
        *,
        TrafficMirrorTargetIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_connect_peers(
        self,
        *,
        TransitGatewayConnectPeerIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_connects(
        self,
        *,
        TransitGatewayAttachmentIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_metering_policies(
        self,
        *,
        TransitGatewayMeteringPolicyIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_multicast_domains(
        self,
        *,
        TransitGatewayMulticastDomainIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_network_function_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_peering_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_policy_tables(
        self,
        *,
        TransitGatewayPolicyTableIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_route_table_announcements(
        self,
        *,
        TransitGatewayRouteTableAnnouncementIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_route_tables(
        self,
        *,
        TransitGatewayRouteTableIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateway_vpc_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transit_gateways(
        self,
        *,
        TransitGatewayIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trunk_interface_associations(
        self,
        *,
        AssociationIds: list[str] | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_verified_access_endpoints(
        self,
        *,
        VerifiedAccessEndpointIds: list[str] | None = None,
        VerifiedAccessInstanceId: str | None = None,
        VerifiedAccessGroupId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_verified_access_groups(
        self,
        *,
        VerifiedAccessGroupIds: list[str] | None = None,
        VerifiedAccessInstanceId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_verified_access_instance_logging_configurations(
        self,
        *,
        VerifiedAccessInstanceIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_verified_access_instances(
        self,
        *,
        VerifiedAccessInstanceIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_verified_access_trust_providers(
        self,
        *,
        VerifiedAccessTrustProviderIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_volume_attribute(
        self,
        *,
        Attribute: str,
        VolumeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_volume_status(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        VolumeIds: list[str] | None = None,
        IncludeManagedResources: bool | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_volumes_modifications(
        self,
        *,
        DryRun: bool | None = None,
        VolumeIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IncludeManagedResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_attribute(
        self,
        *,
        Attribute: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_block_public_access_exclusions(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        ExclusionIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_block_public_access_options(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_classic_link(
        self,
        *,
        DryRun: bool | None = None,
        VpcIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_classic_link_dns_support(
        self,
        *,
        VpcIds: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_encryption_controls(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        VpcEncryptionControlIds: list[str] | None = None,
        VpcIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoint_associations(
        self,
        *,
        DryRun: bool | None = None,
        VpcEndpointIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoint_connection_notifications(
        self,
        *,
        DryRun: bool | None = None,
        ConnectionNotificationId: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoint_connections(
        self,
        *,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoint_service_configurations(
        self,
        *,
        DryRun: bool | None = None,
        ServiceIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoint_service_permissions(
        self,
        *,
        ServiceId: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoint_services(
        self,
        *,
        DryRun: bool | None = None,
        ServiceNames: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ServiceRegions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_endpoints(
        self,
        *,
        DryRun: bool | None = None,
        VpcEndpointIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_peering_connections(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        VpcPeeringConnectionIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpn_concentrators(
        self,
        *,
        VpnConcentratorIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpn_connections(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        VpnConnectionIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpn_gateways(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        VpnGatewayIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_classic_link_vpc(
        self,
        *,
        InstanceId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_image_watermark(
        self,
        *,
        ImageId: str,
        WatermarkKey: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_internet_gateway(
        self,
        *,
        InternetGatewayId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_network_interface(
        self,
        *,
        AttachmentId: str,
        DryRun: bool | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessInstanceId: str,
        VerifiedAccessTrustProviderId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_vpn_gateway(
        self,
        *,
        VpcId: str,
        VpnGatewayId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_address_transfer(
        self,
        *,
        AllocationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_allowed_images_settings(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_application_status_check_suppression(
        self,
        *,
        InstanceIds: list[str] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_aws_network_performance_metric_subscription(
        self,
        *,
        Source: str | None = None,
        Destination: str | None = None,
        Metric: str | None = None,
        Statistic: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_capacity_manager(
        self,
        *,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_ebs_encryption_by_default(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_fast_launch(
        self,
        *,
        ImageId: str,
        Force: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_fast_snapshot_restores(
        self,
        *,
        SourceSnapshotIds: list[str],
        AvailabilityZones: list[str] | None = None,
        AvailabilityZoneIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_image(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_image_block_public_access(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_image_deprecation(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_image_deregistration_protection(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_instance_sql_ha_standby_detections(
        self,
        *,
        InstanceIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_ipam_organization_admin_account(
        self,
        *,
        DelegatedAdminAccountId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_ipam_policy(
        self,
        *,
        IpamPolicyId: str,
        DryRun: bool | None = None,
        OrganizationTargetId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_route_server_propagation(
        self,
        *,
        RouteServerId: str,
        RouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_serial_console_access(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_snapshot_block_public_access(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_transit_gateway_route_table_propagation(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str | None = None,
        DryRun: bool | None = None,
        TransitGatewayRouteTableAnnouncementId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_vgw_route_propagation(
        self,
        *,
        GatewayId: str,
        RouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_vpc_classic_link(
        self,
        *,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_vpc_classic_link_dns_support(
        self,
        *,
        VpcId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_address(
        self,
        *,
        AssociationId: str | None = None,
        PublicIp: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_application_status_check(
        self,
        *,
        ApplicationStatusCheckId: str,
        TargetTagAssociations: list[dict[str, Any]] | None = None,
        InstanceIds: list[str] | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_capacity_reservation_billing_owner(
        self,
        *,
        CapacityReservationId: str,
        UnusedReservationBillingOwnerId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_client_vpn_target_network(
        self,
        *,
        ClientVpnEndpointId: str,
        AssociationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_enclave_certificate_iam_role(
        self,
        *,
        CertificateArn: str,
        RoleArn: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_iam_instance_profile(
        self,
        *,
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        AssociationTarget: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_ipam_byoasn(
        self,
        *,
        Asn: str,
        Cidr: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_ipam_resource_discovery(
        self,
        *,
        IpamResourceDiscoveryAssociationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_kms_key_id(
        self,
        *,
        KmsKeyId: str,
        SnapshotId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        AssociationIds: list[str],
        MaxDrainDurationSeconds: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_networking_flex_cost_allocation_policy(
        self,
        *,
        FcaPolicyAssociationIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_route_server(
        self,
        *,
        RouteServerId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_route_table(
        self,
        *,
        AssociationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_security_group_vpc(
        self,
        *,
        GroupId: str,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_subnet_cidr_block(
        self,
        *,
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        TransitGatewayAttachmentId: str,
        SubnetIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_trunk_interface(
        self,
        *,
        AssociationId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_vpc_cidr_block(
        self,
        *,
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_address_transfer(
        self,
        *,
        AllocationId: str,
        TransferAccountId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_allowed_images_settings(
        self,
        *,
        AllowedImagesSettingsState: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_application_status_check_suppression(
        self,
        *,
        InstanceIds: list[str] | None = None,
        DurationSeconds: int | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_aws_network_performance_metric_subscription(
        self,
        *,
        Source: str | None = None,
        Destination: str | None = None,
        Metric: str | None = None,
        Statistic: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_capacity_manager(
        self,
        *,
        OrganizationsAccess: bool | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_ebs_encryption_by_default(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_fast_launch(
        self,
        *,
        ImageId: str,
        ResourceType: str | None = None,
        SnapshotConfiguration: dict[str, Any] | None = None,
        LaunchTemplate: dict[str, Any] | None = None,
        MaxParallelLaunches: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_fast_snapshot_restores(
        self,
        *,
        SourceSnapshotIds: list[str],
        AvailabilityZones: list[str] | None = None,
        AvailabilityZoneIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_image(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_image_block_public_access(
        self,
        *,
        ImageBlockPublicAccessState: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_image_deprecation(
        self,
        *,
        ImageId: str,
        DeprecateAt: datetime.datetime | str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_image_deregistration_protection(
        self,
        *,
        ImageId: str,
        WithCooldown: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_instance_sql_ha_standby_detections(
        self,
        *,
        InstanceIds: list[str],
        SqlServerCredentials: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_ipam_internet_registry_association(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        RpkiVersion: str,
        ServiceUri: str,
        ChildHandle: str,
        ParentHandle: str,
        ParentBpkiTa: str,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_ipam_organization_admin_account(
        self,
        *,
        DelegatedAdminAccountId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_ipam_policy(
        self,
        *,
        IpamPolicyId: str,
        DryRun: bool | None = None,
        OrganizationTargetId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_reachability_analyzer_organization_sharing(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_route_server_propagation(
        self,
        *,
        RouteServerId: str,
        RouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_serial_console_access(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_snapshot_block_public_access(
        self,
        *,
        State: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_transit_gateway_route_table_propagation(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str | None = None,
        DryRun: bool | None = None,
        TransitGatewayRouteTableAnnouncementId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_vgw_route_propagation(
        self,
        *,
        GatewayId: str,
        RouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_volume_io(
        self,
        *,
        VolumeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_vpc_classic_link(
        self,
        *,
        VpcId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_vpc_classic_link_dns_support(
        self,
        *,
        VpcId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_client_vpn_client_certificate_revocation_list(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_client_vpn_client_configuration(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_image(
        self,
        *,
        DiskImageFormat: str,
        ImageId: str,
        S3ExportLocation: dict[str, Any],
        ClientToken: str | None = None,
        Description: str | None = None,
        DryRun: bool | None = None,
        RoleName: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_transit_gateway_routes(
        self,
        *,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_verified_access_instance_client_configuration(
        self,
        *,
        VerifiedAccessInstanceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_active_vpn_tunnel_status(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_allowed_images_settings(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_associated_enclave_certificate_iam_roles(
        self,
        *,
        CertificateArn: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_associated_ipv6_pool_cidrs(
        self,
        *,
        PoolId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_aws_network_performance_data(
        self,
        *,
        DataQueries: list[dict[str, Any]] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_manager_attributes(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_manager_metric_data(
        self,
        *,
        MetricNames: list[str],
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Period: int,
        GroupBy: list[str] | None = None,
        FilterBy: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_manager_metric_dimensions(
        self,
        *,
        GroupBy: list[str],
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        MetricNames: list[str],
        FilterBy: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_manager_monitored_tag_keys(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_manager_supportability_scores(
        self,
        *,
        MarketType: str,
        CapacityAmount: int,
        CapacityUnit: str,
        CapacityAvailabilityZoneIds: list[str],
        InstanceTypes: list[str] | None = None,
        InstanceRequirementsWithMetadata: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_reservation_usage(
        self,
        *,
        CapacityReservationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_client_vpn_endpoint_authorization_policy(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_coip_pool_usage(
        self,
        *,
        PoolId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_console_output(
        self,
        *,
        InstanceId: str,
        Latest: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_console_screenshot(
        self,
        *,
        InstanceId: str,
        DryRun: bool | None = None,
        WakeUp: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_declarative_policies_report_summary(
        self,
        *,
        ReportId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_default_credit_specification(
        self,
        *,
        InstanceFamily: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ebs_default_kms_key_id(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ebs_encryption_by_default(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_enabled_ipam_policy(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_flow_logs_integration_template(
        self,
        *,
        FlowLogId: str,
        ConfigDeliveryS3DestinationArn: str,
        IntegrateServices: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_groups_for_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_host_reservation_purchase_preview(
        self,
        *,
        HostIdSet: list[str],
        OfferingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_image_ancestry(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_image_block_public_access_state(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_image_findings(
        self,
        *,
        ImageId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_metadata_defaults(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_tpm_ek_pub(
        self,
        *,
        InstanceId: str,
        KeyType: str,
        KeyFormat: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_types_from_instance_requirements(
        self,
        *,
        ArchitectureTypes: list[str],
        VirtualizationTypes: list[str],
        InstanceRequirements: dict[str, Any],
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Context: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_uefi_data(
        self,
        *,
        InstanceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_address_history(
        self,
        *,
        Cidr: str,
        IpamScopeId: str,
        DryRun: bool | None = None,
        VpcId: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_discovered_accounts(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DiscoveryRegion: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_discovered_public_addresses(
        self,
        *,
        IpamResourceDiscoveryId: str,
        AddressRegion: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_discovered_resource_cidrs(
        self,
        *,
        IpamResourceDiscoveryId: str,
        ResourceRegion: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_discovered_routes(
        self,
        *,
        IpamResourceDiscoveryId: str,
        ResourceRegion: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_internet_registry_association_asns(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_internet_registry_association_cidrs(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_policy_allocation_rules(
        self,
        *,
        IpamPolicyId: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Locale: str | None = None,
        ResourceType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_policy_organization_targets(
        self,
        *,
        IpamPolicyId: str,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_pool_allocations(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        IpamPoolAllocationId: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_pool_cidrs(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_prefix_list_resolver_rules(
        self,
        *,
        IpamPrefixListResolverId: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_prefix_list_resolver_version_entries(
        self,
        *,
        IpamPrefixListResolverId: str,
        IpamPrefixListResolverVersion: int,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_prefix_list_resolver_versions(
        self,
        *,
        IpamPrefixListResolverId: str,
        DryRun: bool | None = None,
        IpamPrefixListResolverVersions: list[int] | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_resource_cidrs(
        self,
        *,
        IpamScopeId: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IpamPoolId: str | None = None,
        ResourceId: str | None = None,
        ResourceType: str | None = None,
        ResourceTag: dict[str, Any] | None = None,
        ResourceOwner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_route_origin_authorizations(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DryRun: bool | None = None,
        Cidr: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_route_protection_findings(
        self,
        *,
        IpamId: str,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_routing_policy_registration_deltas(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DryRun: bool | None = None,
        DeltaId: str | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        ChronologicalOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ipam_routing_policy_registrations(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        DryRun: bool | None = None,
        Cidr: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_launch_template_data(
        self,
        *,
        InstanceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_managed_prefix_list_associations(
        self,
        *,
        PrefixListId: str,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_managed_prefix_list_entries(
        self,
        *,
        PrefixListId: str,
        DryRun: bool | None = None,
        TargetVersion: int | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_managed_resource_visibility(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_insights_access_scope_analysis_findings(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_network_insights_access_scope_content(
        self,
        *,
        NetworkInsightsAccessScopeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_networking_flex_cost_allocation_policy_versions(
        self,
        *,
        FcaPolicyId: str,
        VersionsToInclude: list[int] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_password_data(
        self,
        *,
        InstanceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reserved_instances_exchange_quote(
        self,
        *,
        ReservedInstanceIds: list[str],
        DryRun: bool | None = None,
        TargetConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route_server_associations(
        self,
        *,
        RouteServerId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route_server_propagations(
        self,
        *,
        RouteServerId: str,
        RouteTableId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_route_server_routing_database(
        self,
        *,
        RouteServerId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_security_groups_for_vpc(
        self,
        *,
        VpcId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_serial_console_access_status(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_snapshot_block_public_access_state(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_spot_placement_scores(
        self,
        *,
        TargetCapacity: int,
        InstanceTypes: list[str] | None = None,
        TargetCapacityUnitType: str | None = None,
        SingleAvailabilityZone: bool | None = None,
        RegionNames: list[str] | None = None,
        InstanceRequirementsWithMetadata: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        IncludeLocalZones: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subnet_cidr_reservations(
        self,
        *,
        SubnetId: str,
        Filters: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_attachment_nat_configuration(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_attachment_propagations(
        self,
        *,
        TransitGatewayAttachmentId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_metering_policy_entries(
        self,
        *,
        TransitGatewayMeteringPolicyId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_policy_table_associations(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_policy_table_entries(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_prefix_list_references(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_route_table_associations(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_transit_gateway_route_table_propagations(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_verified_access_endpoint_policy(
        self,
        *,
        VerifiedAccessEndpointId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_verified_access_endpoint_targets(
        self,
        *,
        VerifiedAccessEndpointId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_verified_access_group_policy(
        self,
        *,
        VerifiedAccessGroupId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpc_resources_blocking_encryption_enforcement(
        self,
        *,
        VpcId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpn_connection_device_sample_configuration(
        self,
        *,
        VpnConnectionId: str,
        VpnConnectionDeviceTypeId: str,
        InternetKeyExchangeVersion: str | None = None,
        SampleType: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpn_connection_device_types(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_vpn_tunnel_replacement_status(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_client_vpn_client_certificate_revocation_list(
        self,
        *,
        ClientVpnEndpointId: str,
        CertificateRevocationList: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_image(
        self,
        *,
        Architecture: str | None = None,
        ClientData: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Description: str | None = None,
        DiskContainers: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        Encrypted: bool | None = None,
        Hypervisor: str | None = None,
        KmsKeyId: str | None = None,
        LicenseType: str | None = None,
        Platform: str | None = None,
        RoleName: str | None = None,
        LicenseSpecifications: list[dict[str, Any]] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        UsageOperation: str | None = None,
        BootMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_instance(
        self,
        *,
        Platform: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        LaunchSpecification: dict[str, Any] | None = None,
        DiskImages: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_key_pair(
        self,
        *,
        KeyName: str,
        PublicKeyMaterial: bytes | BinaryIO | str,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_snapshot(
        self,
        *,
        ClientData: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Description: str | None = None,
        DiskContainer: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        Encrypted: bool | None = None,
        KmsKeyId: str | None = None,
        RoleName: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_volume(
        self,
        *,
        Image: dict[str, Any],
        Volume: dict[str, Any],
        AvailabilityZoneId: str | None = None,
        DryRun: bool | None = None,
        AvailabilityZone: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_images_in_recycle_bin(
        self,
        *,
        ImageIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_snapshots_in_recycle_bin(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SnapshotIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_volumes_in_recycle_bin(
        self,
        *,
        VolumeIds: list[str] | None = None,
        DryRun: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def lock_snapshot(
        self,
        *,
        SnapshotId: str,
        LockMode: str,
        DryRun: bool | None = None,
        CoolOffPeriod: int | None = None,
        LockDuration: int | None = None,
        ExpirationDate: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_account_vpc_encryption_control(
        self,
        *,
        DryRun: bool | None = None,
        Mode: str | None = None,
        InternetGateway: str | None = None,
        EgressOnlyInternetGateway: str | None = None,
        NatGateway: str | None = None,
        VirtualPrivateGateway: str | None = None,
        VpcPeering: str | None = None,
        Lambda: str | None = None,
        VpcLattice: str | None = None,
        ElasticFileSystem: str | None = None,
        GlobalAccelerator: str | None = None,
        ApiGatewayV2: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_address_attribute(
        self,
        *,
        AllocationId: str,
        DomainName: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_application_status_check(
        self,
        *,
        ApplicationStatusCheckId: str,
        Aggregation: str | None = None,
        HealthCheckPaths: list[dict[str, Any]] | None = None,
        Protocol: str | None = None,
        Port: int | None = None,
        Path: str | None = None,
        DeviceIndex: int | None = None,
        IpVersion: str | None = None,
        IpScope: str | None = None,
        Interval: int | None = None,
        Timeout: int | None = None,
        FailureThreshold: int | None = None,
        SuccessThreshold: int | None = None,
        StatusCodeMatcher: str | None = None,
        InitializationGracePeriodSeconds: int | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_availability_zone_group(
        self,
        *,
        GroupName: str,
        OptInStatus: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        InstanceCount: int | None = None,
        EndDate: datetime.datetime | str | None = None,
        EndDateType: str | None = None,
        Accept: bool | None = None,
        DryRun: bool | None = None,
        AdditionalInfo: str | None = None,
        InstanceMatchCriteria: str | None = None,
        AcceptModificationTerms: bool | None = None,
        StartDate: datetime.datetime | str | None = None,
        QuoteId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_capacity_reservation_fleet(
        self,
        *,
        CapacityReservationFleetId: str,
        TotalTargetCapacity: int | None = None,
        EndDate: datetime.datetime | str | None = None,
        DryRun: bool | None = None,
        RemoveEndDate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_client_vpn_endpoint(
        self,
        *,
        ClientVpnEndpointId: str,
        ServerCertificateArn: str | None = None,
        ConnectionLogOptions: dict[str, Any] | None = None,
        DnsServers: dict[str, Any] | None = None,
        VpnPort: int | None = None,
        Description: str | None = None,
        SplitTunnel: bool | None = None,
        DryRun: bool | None = None,
        SecurityGroupIds: list[str] | None = None,
        VpcId: str | None = None,
        SelfServicePortal: str | None = None,
        ClientConnectOptions: dict[str, Any] | None = None,
        SessionTimeoutHours: int | None = None,
        ClientLoginBannerOptions: dict[str, Any] | None = None,
        ClientRouteEnforcementOptions: dict[str, Any] | None = None,
        DisconnectOnSessionTimeout: bool | None = None,
        TransitGatewayConfiguration: dict[str, Any] | None = None,
        DevicePostureOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_client_vpn_endpoint_authorization_policy(
        self,
        *,
        ClientVpnEndpointId: str,
        PolicyDocument: str | None = None,
        Description: str | None = None,
        ShadowMode: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_default_credit_specification(
        self,
        *,
        InstanceFamily: str,
        CpuCredits: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ebs_default_kms_key_id(
        self,
        *,
        KmsKeyId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_fleet(
        self,
        *,
        FleetId: str,
        DryRun: bool | None = None,
        ExcessCapacityTerminationPolicy: str | None = None,
        LaunchTemplateConfigs: list[dict[str, Any]] | None = None,
        TargetCapacitySpecification: dict[str, Any] | None = None,
        Context: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_fpga_image_attribute(
        self,
        *,
        FpgaImageId: str,
        DryRun: bool | None = None,
        Attribute: str | None = None,
        OperationType: str | None = None,
        UserIds: list[str] | None = None,
        UserGroups: list[str] | None = None,
        ProductCodes: list[str] | None = None,
        LoadPermission: dict[str, Any] | None = None,
        Description: str | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_hosts(
        self,
        *,
        HostIds: list[str],
        HostRecovery: str | None = None,
        InstanceType: str | None = None,
        InstanceFamily: str | None = None,
        HostMaintenance: str | None = None,
        AutoPlacement: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_id_format(
        self,
        *,
        Resource: str,
        UseLongIds: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_identity_id_format(
        self,
        *,
        Resource: str,
        UseLongIds: bool,
        PrincipalArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_image_attribute(
        self,
        *,
        ImageId: str,
        Attribute: str | None = None,
        Description: dict[str, Any] | None = None,
        LaunchPermission: dict[str, Any] | None = None,
        OperationType: str | None = None,
        ProductCodes: list[str] | None = None,
        UserGroups: list[str] | None = None,
        UserIds: list[str] | None = None,
        Value: str | None = None,
        OrganizationArns: list[str] | None = None,
        OrganizationalUnitArns: list[str] | None = None,
        ImdsSupport: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_attribute(
        self,
        *,
        InstanceId: str,
        SourceDestCheck: dict[str, Any] | None = None,
        EnclaveOptions: dict[str, Any] | None = None,
        DisableApiStop: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        Attribute: str | None = None,
        Value: str | None = None,
        BlockDeviceMappings: list[dict[str, Any]] | None = None,
        DisableApiTermination: dict[str, Any] | None = None,
        InstanceType: dict[str, Any] | None = None,
        Kernel: dict[str, Any] | None = None,
        Ramdisk: dict[str, Any] | None = None,
        UserData: dict[str, Any] | None = None,
        InstanceInitiatedShutdownBehavior: dict[str, Any] | None = None,
        Groups: list[str] | None = None,
        EbsOptimized: dict[str, Any] | None = None,
        SriovNetSupport: dict[str, Any] | None = None,
        EnaSupport: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_capacity_reservation_attributes(
        self,
        *,
        InstanceId: str,
        CapacityReservationSpecification: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_connect_endpoint(
        self,
        *,
        InstanceConnectEndpointId: str,
        DryRun: bool | None = None,
        IpAddressType: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        PreserveClientIp: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_cpu_options(
        self,
        *,
        InstanceId: str,
        CoreCount: int | None = None,
        ThreadsPerCore: int | None = None,
        NestedVirtualization: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_credit_specification(
        self,
        *,
        InstanceCreditSpecifications: list[dict[str, Any]],
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_event_start_time(
        self,
        *,
        InstanceId: str,
        InstanceEventId: str,
        NotBefore: datetime.datetime | str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        DryRun: bool | None = None,
        Name: str | None = None,
        TimeRanges: list[dict[str, Any]] | None = None,
        CronExpression: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_maintenance_options(
        self,
        *,
        InstanceId: str,
        AutoRecovery: str | None = None,
        RebootMigration: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_metadata_defaults(
        self,
        *,
        HttpTokens: str | None = None,
        HttpPutResponseHopLimit: int | None = None,
        HttpEndpoint: str | None = None,
        InstanceMetadataTags: str | None = None,
        DryRun: bool | None = None,
        HttpTokensEnforced: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_metadata_options(
        self,
        *,
        InstanceId: str,
        HttpTokens: str | None = None,
        HttpPutResponseHopLimit: int | None = None,
        HttpEndpoint: str | None = None,
        DryRun: bool | None = None,
        HttpProtocolIpv6: str | None = None,
        InstanceMetadataTags: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_network_performance_options(
        self,
        *,
        InstanceId: str,
        BandwidthWeighting: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_instance_placement(
        self,
        *,
        InstanceId: str,
        GroupName: str | None = None,
        PartitionNumber: int | None = None,
        HostResourceGroupArn: str | None = None,
        GroupId: str | None = None,
        Tenancy: str | None = None,
        Affinity: str | None = None,
        HostId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam(
        self,
        *,
        IpamId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        AddOperatingRegions: list[dict[str, Any]] | None = None,
        RemoveOperatingRegions: list[dict[str, Any]] | None = None,
        Tier: str | None = None,
        EnablePrivateGua: bool | None = None,
        MeteredAccount: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_policy_allocation_rules(
        self,
        *,
        IpamPolicyId: str,
        Locale: str,
        ResourceType: str,
        DryRun: bool | None = None,
        AllocationRules: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_pool(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        AutoImport: bool | None = None,
        AllocationMinNetmaskLength: int | None = None,
        AllocationMaxNetmaskLength: int | None = None,
        AllocationDefaultNetmaskLength: int | None = None,
        ClearAllocationDefaultNetmaskLength: bool | None = None,
        AddAllocationResourceTags: list[dict[str, Any]] | None = None,
        RemoveAllocationResourceTags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_pool_allocation(
        self,
        *,
        IpamPoolAllocationId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_prefix_list_resolver(
        self,
        *,
        IpamPrefixListResolverId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        Rules: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_prefix_list_resolver_target(
        self,
        *,
        IpamPrefixListResolverTargetId: str,
        DryRun: bool | None = None,
        DesiredVersion: int | None = None,
        TrackLatestVersion: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_resource_cidr(
        self,
        *,
        ResourceId: str,
        ResourceCidr: str,
        ResourceRegion: str,
        CurrentIpamScopeId: str,
        Monitored: bool,
        DryRun: bool | None = None,
        DestinationIpamScopeId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_resource_discovery(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        AddOperatingRegions: list[dict[str, Any]] | None = None,
        RemoveOperatingRegions: list[dict[str, Any]] | None = None,
        AddOrganizationalUnitExclusions: list[dict[str, Any]] | None = None,
        RemoveOrganizationalUnitExclusions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_routing_policy_registration(
        self,
        *,
        IpamInternetRegistryAssociationId: str,
        Cidr: str,
        Asns: list[str],
        DryRun: bool | None = None,
        PermitMoreSpecificAnnouncements: bool | None = None,
        MaxLength: int | None = None,
        Description: str | None = None,
        Force: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_ipam_scope(
        self,
        *,
        IpamScopeId: str,
        DryRun: bool | None = None,
        Description: str | None = None,
        ExternalAuthorityConfiguration: dict[str, Any] | None = None,
        RemoveExternalAuthorityConfiguration: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_launch_template(
        self,
        *,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        LaunchTemplateId: str | None = None,
        LaunchTemplateName: str | None = None,
        DefaultVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str | None = None,
        LocalGatewayVirtualInterfaceGroupId: str | None = None,
        NetworkInterfaceId: str | None = None,
        DryRun: bool | None = None,
        DestinationPrefixListId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_managed_prefix_list(
        self,
        *,
        PrefixListId: str,
        DryRun: bool | None = None,
        CurrentVersion: int | None = None,
        PrefixListName: str | None = None,
        AddEntries: list[dict[str, Any]] | None = None,
        RemoveEntries: list[dict[str, Any]] | None = None,
        MaxEntries: int | None = None,
        IpamPrefixListResolverSyncEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_managed_resource_visibility(
        self,
        *,
        DefaultVisibility: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_metric_category(
        self,
        *,
        MetricCategoryId: str,
        Metrics: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        EnaSrdSpecification: dict[str, Any] | None = None,
        EnablePrimaryIpv6: bool | None = None,
        ConnectionTrackingSpecification: dict[str, Any] | None = None,
        AssociatePublicIpAddress: bool | None = None,
        AssociatedSubnetIds: list[str] | None = None,
        DryRun: bool | None = None,
        Description: dict[str, Any] | None = None,
        SourceDestCheck: dict[str, Any] | None = None,
        Groups: list[str] | None = None,
        Attachment: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_networking_flex_cost_allocation_policy(
        self,
        *,
        FcaPolicyId: str,
        NatFcaPolicyDocument: dict[str, Any] | None = None,
        InstanceFcaPolicyDocument: dict[str, Any] | None = None,
        PcxFcaPolicyDocument: dict[str, Any] | None = None,
        ShowBackEnabled: bool | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_private_dns_name_options(
        self,
        *,
        InstanceId: str,
        DryRun: bool | None = None,
        PrivateDnsHostnameType: str | None = None,
        EnableResourceNameDnsARecord: bool | None = None,
        EnableResourceNameDnsAAAARecord: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_public_ip_dns_name_options(
        self,
        *,
        NetworkInterfaceId: str,
        HostnameType: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_reserved_instances(
        self,
        *,
        ReservedInstancesIds: list[str],
        TargetConfigurations: list[dict[str, Any]],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_route_server(
        self,
        *,
        RouteServerId: str,
        PersistRoutes: str | None = None,
        PersistRoutesDuration: int | None = None,
        SnsNotificationsEnabled: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_security_group_rules(
        self,
        *,
        GroupId: str,
        SecurityGroupRules: list[dict[str, Any]],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_snapshot_attribute(
        self,
        *,
        SnapshotId: str,
        Attribute: str | None = None,
        CreateVolumePermission: dict[str, Any] | None = None,
        GroupNames: list[str] | None = None,
        OperationType: str | None = None,
        UserIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_snapshot_tier(
        self,
        *,
        SnapshotId: str,
        StorageTier: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_spot_fleet_request(
        self,
        *,
        SpotFleetRequestId: str,
        LaunchTemplateConfigs: list[dict[str, Any]] | None = None,
        OnDemandTargetCapacity: int | None = None,
        Context: str | None = None,
        TargetCapacity: int | None = None,
        ExcessCapacityTerminationPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_subnet_attribute(
        self,
        *,
        SubnetId: str,
        AssignIpv6AddressOnCreation: dict[str, Any] | None = None,
        MapPublicIpOnLaunch: dict[str, Any] | None = None,
        MapCustomerOwnedIpOnLaunch: dict[str, Any] | None = None,
        CustomerOwnedIpv4Pool: str | None = None,
        EnableDns64: dict[str, Any] | None = None,
        PrivateDnsHostnameTypeOnLaunch: str | None = None,
        EnableResourceNameDnsARecordOnLaunch: dict[str, Any] | None = None,
        EnableResourceNameDnsAAAARecordOnLaunch: dict[str, Any] | None = None,
        EnableLniAtDeviceIndex: int | None = None,
        DisableLniAtDeviceIndex: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_traffic_mirror_filter_network_services(
        self,
        *,
        TrafficMirrorFilterId: str,
        AddNetworkServices: list[str] | None = None,
        RemoveNetworkServices: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: str | None = None,
        RuleNumber: int | None = None,
        RuleAction: str | None = None,
        DestinationPortRange: dict[str, Any] | None = None,
        SourcePortRange: dict[str, Any] | None = None,
        Protocol: int | None = None,
        DestinationCidrBlock: str | None = None,
        SourceCidrBlock: str | None = None,
        Description: str | None = None,
        RemoveFields: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_traffic_mirror_session(
        self,
        *,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: str | None = None,
        TrafficMirrorFilterId: str | None = None,
        PacketLength: int | None = None,
        SessionNumber: int | None = None,
        VirtualNetworkId: int | None = None,
        Description: str | None = None,
        RemoveFields: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway(
        self,
        *,
        TransitGatewayId: str,
        Description: str | None = None,
        Options: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_attachment_nat_configuration(
        self,
        *,
        TransitGatewayAttachmentId: str,
        NatGatewaySupport: str | None = None,
        NatSystemRouteSupport: str | None = None,
        NatGatewayRules: list[dict[str, Any]] | None = None,
        ResetNatGatewayRules: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_metering_policy(
        self,
        *,
        TransitGatewayMeteringPolicyId: str,
        AddMiddleboxAttachmentIds: list[str] | None = None,
        RemoveMiddleboxAttachmentIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_network_function_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        AddAvailabilityZones: list[str] | None = None,
        AddAvailabilityZoneIds: list[str] | None = None,
        RemoveAvailabilityZones: list[str] | None = None,
        RemoveAvailabilityZoneIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        Options: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_policy_table_entry(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        PolicyRuleNumber: str,
        PolicyRule: dict[str, Any] | None = None,
        TargetRouteTableId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str | None = None,
        Blackhole: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: list[str] | None = None,
        RemoveSubnetIds: list[str] | None = None,
        Options: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_endpoint(
        self,
        *,
        VerifiedAccessEndpointId: str,
        VerifiedAccessGroupId: str | None = None,
        LoadBalancerOptions: dict[str, Any] | None = None,
        NetworkInterfaceOptions: dict[str, Any] | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        RdsOptions: dict[str, Any] | None = None,
        CidrOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_endpoint_policy(
        self,
        *,
        VerifiedAccessEndpointId: str,
        PolicyEnabled: bool | None = None,
        PolicyDocument: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        SseSpecification: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_group(
        self,
        *,
        VerifiedAccessGroupId: str,
        VerifiedAccessInstanceId: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_group_policy(
        self,
        *,
        VerifiedAccessGroupId: str,
        PolicyEnabled: bool | None = None,
        PolicyDocument: str | None = None,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        SseSpecification: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_instance(
        self,
        *,
        VerifiedAccessInstanceId: str,
        Description: str | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        CidrEndpointsCustomSubDomain: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_instance_logging_configuration(
        self,
        *,
        VerifiedAccessInstanceId: str,
        AccessLogs: dict[str, Any],
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessTrustProviderId: str,
        OidcOptions: dict[str, Any] | None = None,
        DeviceOptions: dict[str, Any] | None = None,
        Description: str | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
        SseSpecification: dict[str, Any] | None = None,
        NativeApplicationOidcOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_volume(
        self,
        *,
        VolumeId: str,
        DryRun: bool | None = None,
        Size: int | None = None,
        VolumeType: str | None = None,
        Iops: int | None = None,
        Throughput: int | None = None,
        MultiAttachEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_volume_attribute(
        self,
        *,
        VolumeId: str,
        AutoEnableIO: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_attribute(
        self,
        *,
        VpcId: str,
        EnableDnsHostnames: dict[str, Any] | None = None,
        EnableDnsSupport: dict[str, Any] | None = None,
        EnableNetworkAddressUsageMetrics: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_block_public_access_exclusion(
        self,
        *,
        ExclusionId: str,
        InternetGatewayExclusionMode: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_block_public_access_options(
        self,
        *,
        InternetGatewayBlockMode: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_encryption_control(
        self,
        *,
        VpcEncryptionControlId: str,
        DryRun: bool | None = None,
        Mode: str | None = None,
        InternetGatewayExclusion: str | None = None,
        EgressOnlyInternetGatewayExclusion: str | None = None,
        NatGatewayExclusion: str | None = None,
        VirtualPrivateGatewayExclusion: str | None = None,
        VpcPeeringExclusion: str | None = None,
        LambdaExclusion: str | None = None,
        VpcLatticeExclusion: str | None = None,
        ElasticFileSystemExclusion: str | None = None,
        GlobalAcceleratorExclusion: str | None = None,
        ApiGatewayV2Exclusion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_endpoint(
        self,
        *,
        VpcEndpointId: str,
        DryRun: bool | None = None,
        ResetPolicy: bool | None = None,
        PolicyDocument: str | None = None,
        AddRouteTableIds: list[str] | None = None,
        RemoveRouteTableIds: list[str] | None = None,
        AddSubnetIds: list[str] | None = None,
        RemoveSubnetIds: list[str] | None = None,
        AddSecurityGroupIds: list[str] | None = None,
        RemoveSecurityGroupIds: list[str] | None = None,
        IpAddressType: str | None = None,
        DnsOptions: dict[str, Any] | None = None,
        PrivateDnsEnabled: bool | None = None,
        SubnetConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_endpoint_connection_notification(
        self,
        *,
        ConnectionNotificationId: str,
        DryRun: bool | None = None,
        ConnectionNotificationArn: str | None = None,
        ConnectionEvents: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_endpoint_payer_responsibility(
        self,
        *,
        VpcEndpointId: str,
        PayerResponsibility: str,
        Scope: str,
        DryRun: bool | None = None,
        ServiceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_endpoint_service_configuration(
        self,
        *,
        ServiceId: str,
        DryRun: bool | None = None,
        PrivateDnsName: str | None = None,
        RemovePrivateDnsName: bool | None = None,
        AcceptanceRequired: bool | None = None,
        AddNetworkLoadBalancerArns: list[str] | None = None,
        RemoveNetworkLoadBalancerArns: list[str] | None = None,
        AddGatewayLoadBalancerArns: list[str] | None = None,
        RemoveGatewayLoadBalancerArns: list[str] | None = None,
        AddSupportedIpAddressTypes: list[str] | None = None,
        RemoveSupportedIpAddressTypes: list[str] | None = None,
        AddSupportedRegions: list[str] | None = None,
        RemoveSupportedRegions: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_endpoint_service_payer_responsibility(
        self,
        *,
        ServiceId: str,
        PayerResponsibility: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_endpoint_service_permissions(
        self,
        *,
        ServiceId: str,
        DryRun: bool | None = None,
        AddAllowedPrincipals: list[str] | None = None,
        RemoveAllowedPrincipals: list[str] | None = None,
        PermissionType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_peering_connection_options(
        self,
        *,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: dict[str, Any] | None = None,
        DryRun: bool | None = None,
        RequesterPeeringConnectionOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpc_tenancy(
        self,
        *,
        VpcId: str,
        InstanceTenancy: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpn_connection(
        self,
        *,
        VpnConnectionId: str,
        TransitGatewayId: str | None = None,
        CustomerGatewayId: str | None = None,
        VpnGatewayId: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpn_connection_options(
        self,
        *,
        VpnConnectionId: str,
        LocalIpv4NetworkCidr: str | None = None,
        RemoteIpv4NetworkCidr: str | None = None,
        LocalIpv6NetworkCidr: str | None = None,
        RemoteIpv6NetworkCidr: str | None = None,
        TunnelBandwidth: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpn_tunnel_certificate(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_vpn_tunnel_options(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: dict[str, Any],
        DryRun: bool | None = None,
        SkipTunnelReplacement: bool | None = None,
        PreSharedKeyStorage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def monitor_instances(
        self,
        *,
        InstanceIds: list[str],
        MetricCategoryIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def move_address_to_vpc(
        self,
        *,
        PublicIp: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def move_byoip_cidr_to_ipam(
        self,
        *,
        Cidr: str,
        IpamPoolId: str,
        IpamPoolOwner: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def move_capacity_reservation_instances(
        self,
        *,
        SourceCapacityReservationId: str,
        DestinationCapacityReservationId: str,
        InstanceCount: int,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def provision_byoip_cidr(
        self,
        *,
        Cidr: str,
        CidrAuthorizationContext: dict[str, Any] | None = None,
        PubliclyAdvertisable: bool | None = None,
        Description: str | None = None,
        DryRun: bool | None = None,
        PoolTagSpecifications: list[dict[str, Any]] | None = None,
        MultiRegion: bool | None = None,
        NetworkBorderGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def provision_ipam_byoasn(
        self,
        *,
        IpamId: str,
        Asn: str,
        AsnAuthorizationContext: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def provision_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool | None = None,
        Cidr: str | None = None,
        CidrAuthorizationContext: dict[str, Any] | None = None,
        NetmaskLength: int | None = None,
        ClientToken: str | None = None,
        VerificationMethod: str | None = None,
        IpamExternalResourceVerificationTokenId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def provision_public_ipv4_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        PoolId: str,
        NetmaskLength: int,
        DryRun: bool | None = None,
        NetworkBorderGroup: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_capacity_block(
        self,
        *,
        CapacityBlockOfferingId: str,
        InstancePlatform: str,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_capacity_block_extension(
        self,
        *,
        CapacityBlockExtensionOfferingId: str,
        CapacityReservationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_host_reservation(
        self,
        *,
        HostIdSet: list[str],
        OfferingId: str,
        ClientToken: str | None = None,
        CurrencyCode: str | None = None,
        LimitPrice: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_reserved_instances_offering(
        self,
        *,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        PurchaseTime: datetime.datetime | str | None = None,
        DryRun: bool | None = None,
        LimitPrice: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purchase_scheduled_instances(
        self,
        *,
        PurchaseRequests: list[dict[str, Any]],
        ClientToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_image(
        self,
        *,
        Name: str,
        ImageLocation: str | None = None,
        BillingProducts: list[str] | None = None,
        BootMode: str | None = None,
        TpmSupport: str | None = None,
        UefiData: str | None = None,
        ImdsSupport: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
        Description: str | None = None,
        Architecture: str | None = None,
        KernelId: str | None = None,
        RamdiskId: str | None = None,
        RootDeviceName: str | None = None,
        BlockDeviceMappings: list[dict[str, Any]] | None = None,
        VirtualizationType: str | None = None,
        SriovNetSupport: str | None = None,
        EnaSupport: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_instance_event_notification_attributes(
        self,
        *,
        InstanceTagAttribute: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_transit_gateway_multicast_group_members(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        NetworkInterfaceIds: list[str],
        GroupIpAddress: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_transit_gateway_multicast_group_sources(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        NetworkInterfaceIds: list[str],
        GroupIpAddress: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_capacity_reservation_billing_ownership(
        self,
        *,
        CapacityReservationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_transit_gateway_client_vpn_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str | None = None,
        TransitGatewayAttachmentId: str | None = None,
        SubnetIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_vpc_endpoint_connections(
        self,
        *,
        ServiceId: str,
        VpcEndpointIds: list[str],
        DryRun: bool | None = None,
        TransitGatewayAttachmentIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_vpc_peering_connection(
        self,
        *,
        VpcPeeringConnectionId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_address(
        self,
        *,
        AllocationId: str | None = None,
        PublicIp: str | None = None,
        NetworkBorderGroup: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_hosts(
        self,
        *,
        HostIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_ipam_pool_allocation(
        self,
        *,
        IpamPoolId: str,
        Cidr: str,
        IpamPoolAllocationId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_iam_instance_profile_association(
        self,
        *,
        IamInstanceProfile: dict[str, Any],
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_image_criteria_in_allowed_images_settings(
        self,
        *,
        ImageCriteria: list[dict[str, Any]] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_image_instance_type_specification(
        self,
        *,
        ImageId: str,
        InstanceTypeSpecification: dict[str, Any] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_network_acl_association(
        self,
        *,
        AssociationId: str,
        NetworkAclId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_network_acl_entry(
        self,
        *,
        NetworkAclId: str,
        RuleNumber: int,
        Protocol: str,
        RuleAction: str,
        Egress: bool,
        DryRun: bool | None = None,
        CidrBlock: str | None = None,
        Ipv6CidrBlock: str | None = None,
        IcmpTypeCode: dict[str, Any] | None = None,
        PortRange: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_route(
        self,
        *,
        RouteTableId: str,
        DestinationPrefixListId: str | None = None,
        VpcEndpointId: str | None = None,
        LocalTarget: bool | None = None,
        TransitGatewayId: str | None = None,
        LocalGatewayId: str | None = None,
        CarrierGatewayId: str | None = None,
        CoreNetworkArn: str | None = None,
        OdbNetworkArn: str | None = None,
        DryRun: bool | None = None,
        DestinationCidrBlock: str | None = None,
        GatewayId: str | None = None,
        DestinationIpv6CidrBlock: str | None = None,
        EgressOnlyInternetGatewayId: str | None = None,
        InstanceId: str | None = None,
        NetworkInterfaceId: str | None = None,
        VpcPeeringConnectionId: str | None = None,
        NatGatewayId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_route_table_association(
        self,
        *,
        AssociationId: str,
        RouteTableId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_transit_gateway_route(
        self,
        *,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str | None = None,
        Blackhole: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replace_vpn_tunnel(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        ApplyPendingMaintenance: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def report_instance_status(
        self,
        *,
        Instances: list[str],
        Status: str,
        ReasonCodes: list[str],
        DryRun: bool | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def request_spot_fleet(
        self,
        *,
        SpotFleetRequestConfig: dict[str, Any],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def request_spot_instances(
        self,
        *,
        LaunchSpecification: dict[str, Any] | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
        InstanceInterruptionBehavior: str | None = None,
        DryRun: bool | None = None,
        SpotPrice: str | None = None,
        ClientToken: str | None = None,
        InstanceCount: int | None = None,
        Type: str | None = None,
        ValidFrom: datetime.datetime | str | None = None,
        ValidUntil: datetime.datetime | str | None = None,
        LaunchGroup: str | None = None,
        AvailabilityZoneGroup: str | None = None,
        BlockDurationMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_address_attribute(
        self,
        *,
        AllocationId: str,
        Attribute: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_ebs_default_kms_key_id(
        self,
        *,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_fpga_image_attribute(
        self,
        *,
        FpgaImageId: str,
        DryRun: bool | None = None,
        Attribute: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_image_attribute(
        self,
        *,
        Attribute: str,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_instance_attribute(
        self,
        *,
        InstanceId: str,
        Attribute: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        DryRun: bool | None = None,
        SourceDestCheck: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_snapshot_attribute(
        self,
        *,
        Attribute: str,
        SnapshotId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_address_to_classic(
        self,
        *,
        PublicIp: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_image_from_recycle_bin(
        self,
        *,
        ImageId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_managed_prefix_list_version(
        self,
        *,
        PrefixListId: str,
        PreviousVersion: int,
        CurrentVersion: int,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_snapshot_from_recycle_bin(
        self,
        *,
        SnapshotId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_snapshot_tier(
        self,
        *,
        SnapshotId: str,
        TemporaryRestoreDays: int | None = None,
        PermanentRestore: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_volume_from_recycle_bin(
        self,
        *,
        VolumeId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_client_vpn_ingress(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str | None = None,
        RevokeAllGroups: bool | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_security_group_egress(
        self,
        *,
        GroupId: str,
        SecurityGroupRuleIds: list[str] | None = None,
        DryRun: bool | None = None,
        SourceSecurityGroupName: str | None = None,
        SourceSecurityGroupOwnerId: str | None = None,
        IpProtocol: str | None = None,
        FromPort: int | None = None,
        ToPort: int | None = None,
        CidrIp: str | None = None,
        IpPermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_security_group_ingress(
        self,
        *,
        CidrIp: str | None = None,
        FromPort: int | None = None,
        GroupId: str | None = None,
        GroupName: str | None = None,
        IpPermissions: list[dict[str, Any]] | None = None,
        IpProtocol: str | None = None,
        SourceSecurityGroupName: str | None = None,
        SourceSecurityGroupOwnerId: str | None = None,
        ToPort: int | None = None,
        SecurityGroupRuleIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def run_scheduled_instances(
        self,
        *,
        LaunchSpecification: dict[str, Any],
        ScheduledInstanceId: str,
        ClientToken: str | None = None,
        DryRun: bool | None = None,
        InstanceCount: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_local_gateway_routes(
        self,
        *,
        LocalGatewayRouteTableId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_transit_gateway_multicast_groups(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_transit_gateway_routes(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: list[dict[str, Any]],
        MaxResults: int | None = None,
        DryRun: bool | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_diagnostic_interrupt(
        self,
        *,
        InstanceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_declarative_policies_report(
        self,
        *,
        S3Bucket: str,
        TargetId: str,
        DryRun: bool | None = None,
        S3Prefix: str | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_network_insights_access_scope_analysis(
        self,
        *,
        NetworkInsightsAccessScopeId: str,
        ClientToken: str,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_network_insights_analysis(
        self,
        *,
        NetworkInsightsPathId: str,
        ClientToken: str,
        AdditionalAccounts: list[str] | None = None,
        FilterInArns: list[str] | None = None,
        FilterOutArns: list[str] | None = None,
        DryRun: bool | None = None,
        TagSpecifications: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_vpc_endpoint_service_private_dns_verification(
        self,
        *,
        ServiceId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_client_vpn_connections(
        self,
        *,
        ClientVpnEndpointId: str,
        ConnectionId: str | None = None,
        Username: str | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unassign_ipv6_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv6Prefixes: list[str] | None = None,
        Ipv6Addresses: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unassign_private_ip_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv4Prefixes: list[str] | None = None,
        PrivateIpAddresses: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unassign_private_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        PrivateIpAddresses: list[str],
        MaxDrainDurationSeconds: int | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unlock_snapshot(
        self,
        *,
        SnapshotId: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unmonitor_instances(
        self,
        *,
        InstanceIds: list[str],
        MetricCategoryIds: list[str] | None = None,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_capacity_manager_monitored_tag_keys(
        self,
        *,
        ActivateTagKeys: list[str] | None = None,
        DeactivateTagKeys: list[str] | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_capacity_manager_organizations_access(
        self,
        *,
        OrganizationsAccess: bool,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_interruptible_capacity_reservation_allocation(
        self,
        *,
        CapacityReservationId: str,
        TargetInstanceCount: int | None = None,
        DryRun: bool | None = None,
        ZeroSizePreference: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_group_rule_descriptions_egress(
        self,
        *,
        DryRun: bool | None = None,
        GroupId: str | None = None,
        GroupName: str | None = None,
        IpPermissions: list[dict[str, Any]] | None = None,
        SecurityGroupRuleDescriptions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_group_rule_descriptions_ingress(
        self,
        *,
        DryRun: bool | None = None,
        GroupId: str | None = None,
        GroupName: str | None = None,
        IpPermissions: list[dict[str, Any]] | None = None,
        SecurityGroupRuleDescriptions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_security_group_quotas_for_interface(
        self,
        *,
        SecurityGroupIds: list[str],
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def withdraw_byoip_cidr(
        self,
        *,
        Cidr: str,
        DryRun: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
