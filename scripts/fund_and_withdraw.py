from webbrowser import get
from brownie import accounts, FundMe
from scripts.helpful_script import get_account


def fund():
    fund = FundMe[-1]
    account = get_account()
    entracefee = fund.getEntranceFee()
    print(f"The entry fee is {entracefee}")
    fund.fund({"from": account, "value": entracefee})


def withdraw():
    fund = FundMe[-1]
    account = get_account(
    )
    entracefee = fund.getEntranceFee()
    fund.withdraw({"from": account})


def main():
    fund()
    withdraw()
