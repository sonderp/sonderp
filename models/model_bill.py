from odoo import fields, models, api


class Facturacionventas(models.Model):
    _name = 'sonderp.facturacionventas'
    _description = 'Tabla de records de la facturacion de ventas'

    # Campos de la tabla sonderp.facturacionventas

    billv_client_name = fields.Char(
        related="billv_name_client.client_name",
        string="Nombre del cliente"
    )
    billv_cuotas = fields.Integer(
        string="Numero de Cuotas",
        related="billv_bill_sell.venta_cuotas"
    )

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
    billv_impuesto_names = fields.Many2many(
        comodel_name='sonderp.impuestos',
        string="Impuestos Disponibles"
    )
    billv_name_client = fields.Many2one(
        comodel_name='sonderp.clientes',
        string="Cliente"
    )
    billv_bill_sell = fields.Many2one(
        comodel_name="sonderp.venta",
        string="Orden de Venta"
    )


class Facturacioncompras(models.Model):
    _name = 'sonderp.facturacioncompras'
    _description = 'Tabla de records de la facturacion de Compras'
    _rec_name = "billc_id"

    # Campos de la tabla sonderp.facturacioncompras

    billc_fecha = fields.Datetime(
        string="Fecha de Factura",
    )
    billc_id = fields.Char(
        string="Factura ID",
        required=True
    )
    billc_cuota = fields.Integer(
        related="billc_compra_cuotas.compra_cuotas",
        string="No de Cuotas"
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

    billc_proveedor_name = fields.Many2one(
        comodel_name="sonderp.proveedores",
        string="Nombre del Proveedor",
    )

    billc_compra_cuotas = fields.Many2one(
        comodel_name="sonderp.compra")


class Impuestos(models.Model):
    _name = 'sonderp.impuestos'
    _description = 'Tabla de records de los impuestos asociados al negocio'
    _rec_name = "impuesto_name"

    # Campos de la tabla sonderp.impuestos

    impuesto_name = fields.Char(
        string="Nombre del impuesto"
    )
    impuesto_tipo = fields.Selection(
        [('0', 'IVA'),
         ('1', '4X100')],
        string="Tipo de impuesto"
    )
    impuesto_valor = fields.Float(
        string="Valor del impuesto"
    )
    impuesto_momento = fields.Selection(
        [('0', 'Momento 0'),
         ('1', 'Momento 1')],
        string="Impuesto Momento"
    )

    # Campos Relacionales de la tabla sonderp.impuestos
