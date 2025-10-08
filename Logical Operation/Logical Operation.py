has_high_income = False
has_good_credit = True
has_criminal_record = True

# and , or
if has_high_income or has_good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for Loan1")
else:
    print("Not Eligible for Loan2")
