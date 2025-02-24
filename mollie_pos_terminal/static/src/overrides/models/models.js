/** @odoo-module */

import { register_payment_method } from "@point_of_sale/app/store/pos_store";
import { PaymentMollie } from "@mollie_pos_terminal/app/payment_mollie";
import { PosPayment } from "@point_of_sale/app/models/pos_payment";
import { patch } from "@web/core/utils/patch";

register_payment_method("mollie", PaymentMollie);

patch(PosPayment.prototype, {
    setMollieUID(id) {
            this.mollieUID = id;
        },
});
