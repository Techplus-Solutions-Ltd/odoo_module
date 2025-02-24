# -*- coding: utf-8 -*-

from odoo import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _create_split_account_payment(self, payment, amounts):
        payment_aml = super()._create_split_account_payment(payment, amounts)
        if payment and payment.payment_method_id.use_payment_terminal == 'mollie':
            for aml in payment_aml.move_id.line_ids:
                aml.name = aml.name + ' - ' + payment.pos_order_id.pos_reference
        return payment_aml
