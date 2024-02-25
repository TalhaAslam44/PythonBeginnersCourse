#has_high_income = False
has_good_credit = True
has_criminal_record = True
# if applicant had good  credit and has high income
# if applicant has good credit and has no criminal record
# And: both , OR: at least one true , Not:
#if has_high_income and has_good_credit:
  #  print("elgible for laon")
#if has_high_income or has_good_credit:
if has_good_credit and not has_criminal_record:
    print("elgible for laon")