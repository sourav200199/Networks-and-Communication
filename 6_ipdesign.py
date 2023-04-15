import ipaddress
import math

startip = input("Enter the starting IP Address: ")
cidr = int(input("Enter the CIDR value: "))
n = int(input("Enter the no. of groups: "))
customers = []

allocated = 0

for i in range(n):
    x = int(input("Group " + str(i+1) + ": "))
    customers.append(x)
    allocated = allocated + x


def get_ip_range(startip, customers, gropuno):
    ip = ipaddress.ip_address(startip)
    start = ip
    end = ip + customers[gropuno]

    return start, end

def get_count(startip, cidr):
    ip = ipaddress.ip_network(startip + "/" + str(cidr), strict=False)

    total = ip.num_addresses
    remaining = total - allocated

    return total, allocated, remaining

print("*****************************************************************")
groups = 0

while groups < n:
    subgroup = []
    x = int(input("Enter the no. of subgroups in group " + str(groups+1) + ": "))

    for i in range(x):
        subgroup.append(int(input("Enter no. of customers in subgroup " + str(i+1) + ": ")))

    print("---------------------- Group " +  str(groups + 1) + " ----------------------")
    for i in range(x):
        start, end = get_ip_range(startip, subgroup, i)
        rcidr = 32 - int(math.log2(subgroup[i]))
        subnet = ipaddress.ip_network(str(start)+"/"+str(rcidr), strict=False).netmask
        print("IP range for the subgroup " + str(i+1) + "----------> " + str(start) + " - " + str(end - 1))
        print("CIDR value: " + str(rcidr))
        print("Subnet mask: " + str(subnet))
        print("-------------------------------------------------------")
        startip = str(end)

    groups = groups + 1

print("*****************************************************************")
total, alloted, remaining = get_count(startip,cidr)
print("Total IP addresses: " + str(total)) 
print("Alloted IP addresses: " + str(alloted)) 
print("Remaining IP addresses: " + str(remaining))





