from web3 import Web3, HTTPProvider, IPCProvider
from tqdm import tqdm
import pandas as pd

from config import CONN, ADDRESS, FILENAME


def fetch_data(conn):
    web3 = Web3(conn)
    curr_block = 0
    while True:
        print("Fetching block no: ", str(curr_block))
        block_data = dict(web3.eth.getBlock(curr_block, full_transactions=True))
        transactions = block_data['transactions']
        df_trans = pd.DataFrame(transactions)
        df_trans[['totalDifficulty', 'mixHash', 'size', 'nonce', 'extraData', 'gasLimit', 'timestamp', 'hash',
            'miner', 'gasUsed', 'receiptsRoot', 'number', 'parentHash', 'logsBloom', 'transactionsRoot', 'sha3Uncles',
            'uncles', 'difficulty', 'stateRoot']] = pd.DataFrame([[block_data['totalDifficulty'],
                block_data['mixHash'], block_data['size'], block_data['nonce'], block_data['extraData'],
                block_data['gasLimit'], block_data['timestamp'], block_data['hash'], block_data['miner'],
                block_data['gasUsed'], block_data['receiptsRoot'], block_data['number'], 
                block_data['parentHash'], block_data['logsBloom'], block_data['transactionsRoot'],
                block_data['sha3Uncles'], block_data['uncles'], block_data['difficulty'],
                block_data['stateRoot']]], index=df_trans.index)

        with open(FILENAME, 'a') as f:
            df_trans.to_csv(f, header=False)

        while curr_block >= web3.eth.blockNumber:
            print("Waiting for a new block. Last fetched block: ", str(curr_block))
            time.sleep(60)
        curr_block += 1

def initialize_headers(headers):
    df = pd.DataFrame(columns=headers)
    df.to_csv(FILENAME, columns=headers)

if __name__ == '__main__':
    if CONN='IPCProvider'
        conn = IPCProvider()
    elif CONN='HTTPProvider':
        conn = HTTPProvider(ADDRESS)
    else:
        raise ValueError("Please set CONN if config.py")

    headers = ['blockHash', 'blockNumber', 'from', 'gas', 'gasPrice', 'hash', 'input', 'nonce', 'r', 's', 'to',
               'transactionIndex', 'v', 'value',
               'totalDifficulty', 'mixHash', 'size', 'nonce', 'extraData', 'gasLimit', 'timestamp', 'hash', 'miner',
               'gasUsed', 'receiptsRoot', 'number', 'parentHash', 'logsBloom', 'transactionsRoot', 'sha3Uncles',
               'uncles', 'difficulty', 'stateRoot']
    _ = initialize_headers(headers)
    fetch_data()
