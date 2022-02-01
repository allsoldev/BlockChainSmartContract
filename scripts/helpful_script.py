from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3
DECIMLS = 8
StartValue = 200000000
FORKED_MAINNET_ENVIRNOMENT = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_NETWORKS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_NETWORKS or network.show_active() in FORKED_MAINNET_ENVIRNOMENT:
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"This is a Mock Network {network.show_active()}")
    print("Deploying Mock")
    if len(MockV3Aggregator) <= 0:
        mockAggregator = MockV3Aggregator.deploy(
            DECIMLS, Web3.toWei(StartValue, "ether"), {"from": get_account()})

    print(network.show_active())
