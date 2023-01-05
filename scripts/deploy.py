from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    #for using MetaMask accounts, maybe ledger as well
    # account = accounts.load("goerli-account1")
    # print(account)
    #use this method for serious accounts, because you encrypt the private keys with a separate password
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(14, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()