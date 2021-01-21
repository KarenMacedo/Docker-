# -*- coding: utf-8 -*-
from odoo import models, fields, api


class report_bibliteca_libro(models.AbstractModel):
    _name = 'biblioteca_report_libro.report_biblioteca_libro'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('biblioteca.report_biblioteca_libro')
        return {
            'doc_ids': docids,
            'doc_model': self.env['biblioteca.libro'],
            'docs': self.env['biblioteca.libro'].browse(docids)
        }





# class biblioteca_report(models.Model):
#
#     _name = 'biblioteca.report'