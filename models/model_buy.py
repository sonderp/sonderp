from odoo import fields, models, api


class Ordenescompra (models.Model):
    _name = 'sonderp.compra'
    _description = 'Tabla de records de la Ordenes de Compra'

    # Campos de la tabla sonderp.compra
    compra_id = fields.Char(
        string="ID Orden"
    )
    compra_date = fields.Datetime(
        string="Fecha de Orden de Compra"
    )
    compra_costo = fields.Float(
        string="Costo de la compra"
    )
    compra_cantidad = fields.Integer(
        string="Cantidad"
    )
    compra_cuotas = fields.Integer(
        string="Cuotas"
    )
    compra_cuotas_pagadas = fields.Integer(
        string="Cuotas Pagadas"
    )

    compra_costo_cuotas = fields.Integer(
        string="Valor por cuota",
        compute="",
        default="0"
    )
    compra_total = fields.Integer(
        string="Valor Total",
        compute="",
        default="0"
    )
    compra_state = fields.Char(
        string="Estado",
        compute="",
        default="NA"
    )

    # Campos Relacionales de la tabla sonderp.compra

    compra_proveedores_name = fields.Many2many(
        comodel_name="sonderp.proveedores",
        string="Proveedores"
    )
    compra_stock_enable = fields.Many2many(
        comodel_name="sonderp.stock",
        string="Productos Disponibles"
    )


class Proveedores (models.Model):
    _name = 'sonderp.proveedores'
    _description = 'Tabla de records de los proveedores'
    _rec_name = "proveedor_name"

    # Campos de la tabla sonderp.proveedores
    proveedor_name = fields.Char(
        string="Nombre de la empresa/proveedor",
        required=True
    )
    proveedor_nit = fields.Integer(
        string="NIT",
        required=True
    )
    proveedor_address = fields.Char(
        string="Direccion de la empresa/Proveedor"
    )
    proveedor_city = fields.Char(
        string="Ciudad"
    )
    proveedor_type = fields.Char(
        string="Tipo de proveedor"
    )

    # Campos Relacionales de la tabla sonderp.proveedores

    proveedor_bill_buy = fields.One2many(
        comodel_name="sonderp.facturacioncompras",
        inverse_name="billc_proveedor_name"
    )
    proveedor_categoria = fields.Many2many(
        comodel_name="sonderp.categoria",
        string="Productos"
    )
