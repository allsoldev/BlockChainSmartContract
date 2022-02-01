from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_script import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_NETWORKS
from web3 import Web3


def deploy_FundMe():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        # kdeploy = FundMe.deploy(price_feed_address, {"from": account})
        print(network.show_active())

    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

        # etprice = config (["networks"][network.show_active()]["eth_usd_price_feed"])

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify"),
    )
    return fund_me
   # print(f"Contact Deployed to {fund_me.address}")


def main():
    deploy_FundMe()
