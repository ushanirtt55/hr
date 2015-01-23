from openerp import models,fields
from openerp import api
from IPython.external.jsonschema._jsonschema import ValidationError

class kenya_payroll(models.Model):
    _inherit='hr.contract'
   
    #cash_pay=fields.Float('Cash pay Kshs')
    benefits=fields.Float('Benefits Non cash Kshs')
    #house_status=fields.Selection(selection=[(0,'Not Housed'),(1,'Employer owned house'),(2,'Employer rented house'),(3,'Agricultural farm')])
    house=fields.Float('Housing')
    val_quat=fields.Float('Value of Quarters')
    comp_quat=fields.Integer('Computed value of Quarters')
    rent_emp=fields.Float('Rent Recovered from Employee')
    net_house=fields.Float('Net Value Of Housing')
    #gross_pay=fields.Float('Total Gross pay C+D+E')
    #ben_calc_30=fields.Float('Defined Contribution Benefit Calculation 30%OF C')
    #ben_calc_act=fields.Float('Defined Contribution Benefit Calculation Actual Cont')
    #ben_calc_llimit=fields.Float('Defined Contribution Benefit Calculation Legal Limit')
    oci_hosp=fields.Float('Owner Occupied Interest or HOSP')
    ocupier_inter_hosp=fields.Float('Defined Contribution & owner occupier Interest or HOSP')
    #charge_pay=fields.Float('Chargeable pay')
    #tax_charge=fields.Float('Tax Charged')
    relief=fields.Float('Monthly Relief(monthly)')
    ins_relief=fields.Float('Insurance Relief(monthly)')
    #pa_ye=fields.Float('P.A.Y.E TAX')
    
    @api.one
    @api.constrains('relief')
    def check_relief(self):
        if self.relief>1162:
            raise ValidationError('Monthly Relief must be less than 1,162')    
    
    @api.one
    @api.constrains('ins_relief')
    def check_ins_relief(self):
        if self.ins_relief>5000:
            raise ValidationError('Insurance Relief should not exceed 5000')   
   