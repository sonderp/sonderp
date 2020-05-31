# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Clientes(models.Model):
    _name = "sonderp.clientes"
    _description = "Registro de clientes"

    client_name = fields.Char(String="Nombre", required=True)
    client_id = fields.Char(String="Id", required=True)
    client_type = fields.Selection([('0', 'tipo1'), ('1', 'tipo2')], String="Tipo", required=True)
    client_address = fields.Char(String="Direccion")
    client_city = fields.Char(String="Ciudad")
    client_contacto1 = fields.Integer(String="Telefono")
    client_contacto2 = fields.Char(String="Correo")
    client_venta = fields.One2many("sonderp.venta", "venta_client", string="Ordenes de venta")

class Precios(models.Model):
    _name = "sonderp.precios"
    _description = "Registro de precios"

    precios_ganancia = fields.Float(String="Ganancia", required=True)
    precios_promocion = fields.Float(String="Promocion")
    precios_ofertas = fields.Float(String="Precio")
    precios_fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    #precios_costo = fields.Many2one(String="Costo")

class Ordenesventa(models.Model):
    _name = "sonderp.venta"
    _description = "Registro de ventas"

    venta_cantidad = fields.Integer(String="Cantidad")
    venta_cuotas = fields.Integer(String="Cuotas")
    venta_cuotas_vendidas = fields.Integer(String="Cuotas vendidad")
    venta_costo_cuotas = fields.Float(String="Costo por cuota")
    venta_total = fields.Float(String="Total")
    venta_state = fields.Selection([('a1', 'tipo1'), ('a2', 'tipo2')], String="Estado", required=True)
    venta_date = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    venta_oferta = fields.Many2many("sonderp.precios", string="Asistentes")
    #venta_factura = fields.One2many()
    venta_client = fields.Many2one("sonderp.clientes", ondelete="cascade", string="Cliente", index=True)

