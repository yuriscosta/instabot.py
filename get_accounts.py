# coding: utf-8

""" Modulo que irá listar todas as contas cadastradas no banco """

from pymongo import MongoClient

def list_accounts():
    """ Função de listar contas """
    client = MongoClient('localhost', 27017)
    database = client.accounts_db
    account_set = database.accounts_collection
    account_set = database.account_set

    accounts = []
    for account in account_set.find():
        accounts.append(account)

    return accounts

if __name__ == '__main__':
    print(list_accounts())
