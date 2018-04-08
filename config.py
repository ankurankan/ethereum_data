# Connection type to blockchain. Can be either HTTPProvider or IPCProvider
CONN = 'IPCProvider'

# If CONN='HTTPProvider', address of the node
HTTP_ADDRESS = None

# If CONN='IPCProvider', address of the IPC file
IPC_ADDRESS = '/home/ankur_gcloud/ssd/.ethereum/geth.ipc'

# File name where to store the data
FILENAME = '/home/ankur_gcloud/blockchain.csv'
