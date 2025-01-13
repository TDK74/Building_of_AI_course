portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    # Base case - if there are no more ports left
    if not ports:
        # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
        return
        
    for i in range(len(ports)):
        new_route = route + [ports[i]]
        new_ports = ports[: i] + ports[i+1 :]
        permutations(new_route, new_ports)

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
