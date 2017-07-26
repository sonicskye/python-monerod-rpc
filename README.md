# python-monerod-rpc
Using python to create monerod RPC requests and read the results, then put them to MySQL database for further analysis.

The local testnet monero nodes are run by the following commands:
First node: monerod --testnet --no-igd --hide-my-port --testnet-data-dir testnet --p2p-bind-ip 127.0.0.1
Second node: monerod --testnet --testnet-p2p-bind-port 38080 --testnet-rpc-bind-port 38081 --no-igd --hide-my-port --testnet-data-dir testnet2 --p2p-bind-ip 127.0.0.1 --add-exclusive-node 127.0.0.1:2