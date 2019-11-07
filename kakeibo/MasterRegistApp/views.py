from django.shortcuts import render

from MasterRegistApp.models import AccountList


# Create your views here.
def accountlist():
    return render("accountlist.html")
    

def accountreg(request):
    return render(request, "accountreg.html")

# 통장등록
def executeAccountRegist(request):

    try:
        req_account_name = request.POST['inp_account_name']
        req_bank = request.POST['inp_bank_name']
        req_account_num = request.POST['inp_account_num']
        req_account_kind = request.POST['sel_account_kind']
        req_account_kind_other = request.POST['inp_account_kind_other']
        req_account_purpose = request.POST['sel_account_purpose']
        req_account_purpose_other = request.POST['inp_account_purpose_other']

        model = AccountList(account_name = req_account_name, 
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
        
    return render(request, "accountreg.html") 

    