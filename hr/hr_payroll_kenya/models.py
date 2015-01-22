from openerp import models,fields

class kenya_payroll(models.Model):
    _inherit='hr.payslip'
   
    cash_pay=fields.Float('Cash pay Kshs')
    benefits=fields.Float('Benefits Non cash Kshs')
    house_status=fields.Selection(selection=[(0,'Not Housed'),(1,'Employer owned house'),(2,'Employer rented house'),(3,'Agricultural farm')])
    val_quat=fields.Float('Value of Quarters')
    comp_quat=fields.Integer('Computed value of Quarters')
    rent_emp=fields.Float('Rent Recovered from Employee')
    net_house=fields.Float('Net Value Of Housing')
    gross_pay=fields.Float('Total Gross pay C+D+E')
    ben_calc_30=fields.Float('Defined Contribution Benefit Calculation 30%OF C')
    ben_calc_act=fields.Float('Defined Contribution Benefit Calculation Actual Cont')
    ben_calc_llimit=fields.Float('Defined Contribution Benefit Calculation Legal Limit')
    oci_hosp=fields.Float('Owner Occupied Interest or HOSP')
    ocuupier_inter_hosp=fields.Float('Defined Contribution & owner occupier Interest or HOSP')
    charge_pay=fields.Float('Chargeable pay (F-H)')
    tax_charge=fields.Float('Tax Charged')
    relief=fields.Float('Monthly Relief + Insurance Relief')
    ins_relief=fields.Float('Insurance Relief')
    pa_ye=fields.Float('P.A.Y.E TAX')
    