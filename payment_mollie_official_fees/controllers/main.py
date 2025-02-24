# -*- coding: utf-8 -*-

from odoo.http import request, route

from odoo.addons.website_sale.controllers.main import WebsiteSale


class MollieFeesWebsiteSale(WebsiteSale):

    @route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        order = request.website.sale_get_order()
        order._remove_mollie_fees_line()
        return super().cart(access_token=access_token, revive=revive, **post)

    @route('/shop/checkout', type='http', methods=['GET'], auth='public', website=True, sitemap=False)
    def shop_checkout(self, try_skip_step=None, **query_params):
        order = request.website.sale_get_order()
        order._remove_mollie_fees_line()
        return super().shop_checkout(try_skip_step=try_skip_step, **query_params)

    @route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    def shop_payment(self, **post):
        order = request.website.sale_get_order()
        order._remove_mollie_fees_line()
        return super().shop_payment(**post)
