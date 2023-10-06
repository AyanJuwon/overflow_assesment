# Example Project README

## Challenge 1A String Compression:
##        TIME COMPLEXITY 
# The string compression algorithm has a time complexity of O(n),
# where n is the length of the input string.
# It iterates through the string once (O(n)),
# appends characters and counts to a list (O(n)),
# and then joins the compressed characters (O(n)).
# Overall, it operates linearly with the length of the input string. 


## Challenge 1B Network Test:
##        TIME COMPLEXITY 
# The time complexity of identifying the router with the highest connections in the directed graph is O(n), where n is the number of nodes. It iterates through each node to calculate the total connections, determining the routers with the highest number of connections. This linear complexity arises from iterating over the nodes and comparing their connections to find the maximum. The edge additions have negligible impact on the overall time complexity.


## Challenge 2 Etherscan Test:
##        TIME COMPLEXITY 
## Installation for Etherscan

1. Install dependencies using `pip`:
   ```bash
   pip install -r requirements.txt

2. export your api key
    ```bash
   export API_KEY="api_key"

3. ```bash
     python etherscan.py
