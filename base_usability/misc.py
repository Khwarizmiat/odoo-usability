# -*- coding: utf-8 -*-
##############################################################################
#
#    Base Usability module for Odoo
#    Copyright (C) 2016 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class BaseLanguageExport(models.TransientModel):
    _inherit = 'base.language.export'

    # Default format for language files = format used by OpenERP modules
    format = fields.Selection(default='po')


class BaseLanguageInstall(models.TransientModel):
    _inherit = 'base.language.install'

    overwrite = fields.Boolean(default=True)
