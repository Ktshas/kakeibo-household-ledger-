# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from Account.models import AccountList


# 통장 일람.
def getaccountlist(request):
    dbResult = AccountList.objects.filter(delete_flg = "N")
    context = {'accounts': dbResult}
    
    return render(request, "Account/accountlist.html", context)
    
# 통장 등록화면
def accountreg(request):
    return render(request, "Account/accountreg.html")

# 통장 등록처리
def executeAccountRegist(request):

    try:
        req_account_name = request.POST['inp_account_name']
        req_bank = request.POST['inp_bank_name']
        req_account_num = request.POST['inp_account_num']
        req_account_kind = request.POST['sel_account_kind']
        req_account_kind_other = request.POST['inp_account_kind_other']
        req_account_purpose = request.POST['sel_account_purpose']
        req_account_purpose_other = request.POST['inp_account_purpose_other']

        model = AccountList(
            account_name = req_account_name, 
            bank = req_bank,
            account_num = None if req_account_num == "" else int(req_account_num),
            account_kind = None if req_account_kind == "" else int(req_account_kind),
            account_kind_other = None if req_account_kind_other == "" else req_account_kind_other,
            account_purpose = None if req_account_purpose == "" else int(req_account_purpose),
            account_purpose_other = None if req_account_purpose_other == ""  else req_account_purpose_other
        )

        model.save();
    
    except Exception as ex:
        print(ex)
        
    return redirect("getaccountlist") 

# 통장삭제
def accountdel(request):
    
    req_account_id = request.POST['account_id']
    dbObj = AccountList.objects.get(account_id=req_account_id)
    dbObj.delete()
    return redirect('/') 

# 통장수정
def accountupdate(request):
    
    req_account_id = request.POST['account_id']
    dbObj = AccountList.objects.get(account_id=req_account_id)
    
    req_account_name = request.POST['inp_account_name']
    req_bank = request.POST['inp_bank_name']
    req_account_num = request.POST['inp_account_num']
    req_account_kind = request.POST['sel_account_kind']
    req_account_kind_other = request.POST['inp_account_kind_other']
    req_account_purpose = request.POST['sel_account_purpose']
    req_account_purpose_other = request.POST['inp_account_purpose_other']
    
    dbObj.update(
            account_name = req_account_name, 
            bank = req_bank,
            account_num = None if req_account_num == "" else int(req_account_num),
            account_kind = None if req_account_kind == "" else int(req_account_kind),
            account_kind_other = None if req_account_kind_other == "" else req_account_kind_other,
            account_purpose = None if req_account_purpose == "" else int(req_account_purpose),
            account_purpose_other = None if req_account_purpose_other == ""  else req_account_purpose_other)
    
    return redirect("/") 

    