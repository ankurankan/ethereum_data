# Connection type to blockchain. Can be either HTTPProvider or IPCProvider
CONN = 'IPCProvider'

# If CONN='HTTPProvider', address of the node
ADDRESS = None

# If CONN='IPCProvider', address of the IPC file
ADDRESS = '/home/ankur_gcloud/ssd/.ethereum/geth.ipc'

# File name where to store the data
FILENAME = 'blockchain.csv'
