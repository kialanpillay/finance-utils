import argparse

parser = argparse.ArgumentParser(description='Calculate salary tax, UIF and taxable income.')

def monthly(value):
    return value/12

def tax_deductible(pension, annual_gross_salary):
    return min(pension, min(annual_gross_salary * 0.275, 350000))

def income_tax(taxable_income):
    if 337801 < taxable_income < 467500 :
        return 70532 + 0.31 * (taxable_income - 337800)
    elif 467501 < taxable_income < 613600 :
        return 110739 + 0.36 * (taxable_income - 467500)
    elif 613601 < taxable_income < 782200 :
        return 163335 + 0.39 * (taxable_income - 613600)
    else:
        return 0.18 * taxable_income

def tax_rebate(tax_threshold):
    return 0.18 * tax_threshold

tax_threshold = 87300
annual_gross_salary = 743000
monthly_pension_contribution_percentage = 0.01
annual_pension_contribution = annual_gross_salary * monthly_pension_contribution_percentage
travel_allowance = 0
uif = min(monthly(annual_gross_salary * 0.01), 148.72)

for i in range(1,15):
    monthly_pension_contribution_percentage = i * 0.01
    annual_pension_contribution = annual_gross_salary * monthly_pension_contribution_percentage
    
    taxable_income = annual_gross_salary - tax_deductible(annual_pension_contribution , annual_gross_salary) - 0.2 * travel_allowance

    monthly_taxable_income = monthly(taxable_income)
    paye = monthly(income_tax(taxable_income) - tax_rebate(tax_threshold))
    take_home_pay = monthly(annual_gross_salary) - paye - uif - monthly(annual_pension_contribution)
    print("Monthly pension contribution percentage: " + "{:,.2f}%". format(monthly_pension_contribution_percentage * 100))
    print("Taxable income for the year: " + "R{:,.2f}". format(taxable_income))
    print("Monthly pension contribution: " + "R{:,.2f}". format(monthly(annual_pension_contribution)))
    print("PAYE: " + "R{:,.2f}". format(paye))
    print("Take home pay: " + "R{:,.2f}". format(take_home_pay))
    print()