# -*- coding: utf-8 -*-
{
    'name' : 'Biblioteca',
    'version' : '1.0',
    'author' : 'Karen Lizbeth',
    'summary' : 'Modulo de odoo prueba',
    'description' : 'modulo prueba',
    'images': [
            'static/src/img/icon.png'
        ],
    'depends' : ['base',],
    'data' : ['views/biblioteca_libros_view.xml',
              'views/biblioteca_categoria_view.xml',
              'views/biblioteca_menu_view.xml',
              'views/biblioteca_report.xml',
              'report/report.xml'
        # 'security/ir.model.access.csv',
    ],
    'installable' : True,
    'aplication' : True

}

