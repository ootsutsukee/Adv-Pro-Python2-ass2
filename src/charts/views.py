from django.shortcuts import render
from .models import AccountInfo

# def index(request):
#     # accountinfos = AccountInfo.objects.all()

#     # context = {
#     #     "accountinfos" : accountinfos
#     # }


#     for i in range(100):
#         AccountInfo.objects.create(address=addres[i], balance=balanc[i])
#     accountinfos = AccountInfo.objects.all()
#     context = {
#         "accountinfos" : accountinfos
#     }


#     return render(request, 'chart_page/index.html', context)


import requests

import re

from bs4 import BeautifulSoup

from etherscan import Etherscan





def index(request):
    AccountInfo.delete_everything(self=AccountInfo)


    eth = Etherscan("USFBEVTA1M1BHWR5Z8W9DGVI56FNUV98RZ")

    data = []

    balance = []

    for i in range(4):

        url = "https://etherscan.io/accounts/%s"

        new_url = url %(i + 1)

        cookies = dict(BCPermissionLevel='PERSONAL')

        req = requests.get(new_url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies)

        soup = BeautifulSoup(req.content, 'html.parser')

        temp = soup.select("td a")

        for i in temp:

            data.append(i.get_text())
        

    cnt = 0





    for j in data:

        bal = eth.get_eth_balance(j)

        balance.append(float(bal) / 1000000000000000000)

    for k in range(0, 100):

        AccountInfo.save(AccountInfo.objects.create(account_name=data[k], account_summ=balance[k]))
    

    accountinfos = AccountInfo.objects.all()
    context = {

        "accountinfos": accountinfos

    }

    return render(request, 'chart_page/index.html', context)