/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
    async setup() {
        await super.setup(...arguments);
        this.data.connectWebSocket("MOLLIE_TERMINAL_RESPONSE", () => {
            let pendingLine = this.getPendingPaymentLine("mollie");
            if (pendingLine) {
                pendingLine.payment_method_id.payment_terminal.handleMollieStatusResponse();
            }
        });
    },
});
