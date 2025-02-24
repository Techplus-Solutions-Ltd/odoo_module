/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { Dialog } from '@web/core/dialog/dialog';

export class MollieBalanceJsonDataTable extends Component {
    setup() {
        super.setup();
    }
    formatCamelCase(text) {
        var result = text.replace(/([A-Z])/g, " $1");
        return result.charAt(0).toUpperCase() + result.slice(1);
    }
    get tableVal() {
        return JSON.parse(this.props.record.data[this.props.name]);
    }
}
MollieBalanceJsonDataTable.components = { Dialog }
MollieBalanceJsonDataTable.template = 'drg_balance_payment_info';

export class mollieBalanceJsonDataComponent extends Component {
    setup() {
        this.dialog = useService("dialog");
        this.data = JSON.parse(this.props.record.data[this.props.name]);
        super.setup();
    }
    openDialog() {
        this.dialog.add(MollieBalanceJsonDataTable, this.props);
    }
}

mollieBalanceJsonDataComponent.template = "mollieBalanceSync.mollieBalanceJsonDataComponent";
mollieBalanceJsonDataComponent.supportedTypes = ["char"];
mollieBalanceJsonDataComponent.components = ["MollieBalanceJsonDataTable"];

export const MollieBalanceJsonDataComponent = {
    component: mollieBalanceJsonDataComponent,
};
registry.category("fields").add("balance_payment_info", MollieBalanceJsonDataComponent);
