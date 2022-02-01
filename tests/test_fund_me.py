from scripts.helpful_script import get_account, LOCAL_BLOCKCHAIN_NETWORKS
from scripts.deploy import deploy_FundMe
from brownie import accounts, network, exceptions
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_FundMe()
    entraceFee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entraceFee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entraceFee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    #assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORKS:
        pytest.skip("Only for Local Testing")

    #account = get_account()
    fund_me = deploy_FundMe()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
