from odoo import fields, models, api


class Facturacionventas(models.Model):
    _name = 'sonderp.facturacionventas'
    _description = 'Tabla de records de la facturacion de ventas'

    # Campos de la tabla sonderp.facturacionventas

    billv_fecha = fields.Datetime(
        string="Fecha de Factura",
    )
    billv_id = fields.Char(
        string="Factura ID"
    )
    billv_cuota = fields.Float(
        string="No de Cuota"
    )
    billv_total = fields.Float(
        string="Valor Total"
    )
    billv_sin_impuesto = fields.Float(
        string="Valor sin impuesto"
    )
    billv_impuesto = fields.Float(
        string="Valor con impuesto"
    )
    billv_medio_de_pago = fields.Selection(
        [('0', 'Efectivo'),
         ('1', 'Consignacion'),
         ('2', 'Tarjeta Debito/Credito')],
        string="Medio de Pago"
    )
    billv_cuenta_pago = fields.Integer(
        string="Cuenta Bancaria"
    )

    # Campos Relacionales de la tabla sonderp.facturacionventas


class Facturacioncompras(models.Model):
    _name = 'sonderp.facturacioncompras'
    _description = 'Tabla de records de la facturacion de Compras'

    # Campos de la tabla sonderp.facturacioncompras

    billc_fecha = fields.Datetime(
        string="Fecha de Factura",
    )
    billc_id = fields.Char(
        string="Factura ID"
    )
    billc_cuota = fields.Float(
        string="No de Cuota"
    )
    billc_total = fields.Integer(
        string="Valor Total"
    )
    billc_medio_de_pago = fields.Selection(
        [('0', 'Efectivo'),
         ('1', 'Consignacion'),
         ('2', 'Tarjeta Debito/Credito')],
        string="Medio de Pago"
    )

    # Campos Relacionales de la tabla sonderp.facturacioncompras


class Impuestos(models.Model):
    _name = 'sonderp.impuestos'
    _description = 'Tabla de records de los impuestos asociados al negocio'

    # Campos de la tabla sonderp.impuestos

    impuesto_name = fields.Char(
        string="Nombre del impuesto"
    )
    impuesto_tipo = fields.Selection(
        [('0', 'IVA'),
         ('1', '4X100')],
        string="Tipo de impuesto"
    )
    impuesto_valor = fields.Field(
        string="Valor del impuesto"
    )
    impuesto_momento = fields.Selection(
        [('0', 'Momento 0'),
         ('1', 'Momento 1')],
        string="Impuesto Momento"
    )

    # Campos Relacionales de la tabla sonderp.impuestos
