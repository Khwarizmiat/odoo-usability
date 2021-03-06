# -*- coding: utf-8 -*-
##############################################################################
#
#    HR Expense Usability module for Odoo
#    Copyright (C) 2015 Akretion (http://www.akretion.com)
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


{
    'name': 'HR Expense Usability',
    'version': '0.1',
    'category': 'Human Resources',
    'license': 'AGPL-3',
    'summary': 'Better usability for the management of expenses',
    'description': '',
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['hr_expense'],
    'data': [
        'security/expense_security.xml',
        ],
    'installable': True,
}
