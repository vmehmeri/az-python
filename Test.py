from Subnet import Subnet
from IpAddress import AzureIpAddress
from ApplicationSecurityGroup import ApplicationSecurityGroup
from NetworkSecurityRule import NetworkSecurityRule
from NetworkEnvironment import NetworkEnvironment, Env

if __name__ == '__main__':
    dev_env = NetworkEnvironment(Env.DEV)
    
    print(f"Subscription {dev_env.subscription_name} [id: {dev_env.subscription_id}]")

    app_subnet = Subnet(dev_env, "app-subnet")
    an_ip_addr = AzureIpAddress(dev_env, "10.0.0.10")
    an_asg = ApplicationSecurityGroup(dev_env, "asg-rg", "some-asg")
    
    if (an_ip_addr.is_in_range("10.0.0.0/24")):
        print("IP Address is in range")
    else:
        print("IP Address not in range!")

    print(app_subnet.ip_range)
    
    nsg_in = NetworkSecurityRule("allow-ssh", "Just a test security rule", 100, an_asg, app_subnet, "TCP", 22, "Inbound")
    
    print(f"Network Security Rule:\n {nsg_in.to_json_object()}")
