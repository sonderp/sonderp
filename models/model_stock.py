# -*- coding: utf-8 -*-

from odoo import models, fields, api

class categoria(models.Model):
    _name = "sonderp.categoria"
    _description = "Productos y su categoría"

    categoria_producto = fields.Char(String="Producto", required=True, help='Escriba el nombre del producto.\n Ej: Chocolatina')
    categoria_grupo = fields.Char(String="Categoria", required=True, help='Escriba la categoría a la que pertenece el producto.\n Ej: Dulces')
    categoria_imagen = fields.Binary(String="Imagen", help='Agregue una imagen/foto del producto.')
    categoria_state = fields.Selection(String="Estado", default="enable", selection=[('enable', 'En Venta'), ('disable', 'En Reserva')], required=True, help='Seleccione en qué estado estará el producto.\n Ej: En venta')
    categoria_requerido_umbral = fields.Integer(String="Cantidad requerida", required=True, help='Escriba la cantidad que desea tener de su producto.\n Ej: 50')
    categoria_agotado_umbral = fields.Integer(String="Cantidad mínima", required=True, help='Escriba la cantidad a partir de la cual su producto se considera en escasez.\n Ej: 10')
    #proveedores = fields.Many2many('sonderp.proveedores', string="Proveedores")

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s' % (rec.categoria_producto)))
        return res

class stock(models.Model):

    _name = "sonderp.stock"
    _description = "Productos y su cantidad"

    stock_date = fields.Datetime(String="Fecha", required=True)
    stock_cantidad_enable = fields.Integer(String="Cantidad disponible", default=0)
    stock_cantidad_total = fields.Integer(String="Cantidad total")
    stock_state = fields.Selection(String="Estado", selection=[('a1', 'Agotado'), ('a2', 'Escaso'), ('a3', 'En Orden'), ('a4', 'No en venta')], compute='_compute_state', copy=False, index=True, readonly=True, store=True, tracking=True)
    stock_place = fields.Char(String="Ubicacion")
    stock_cantidad_disable = fields.Integer(String="Cantidad reservada")
    stock_note = fields.Html()

    stock_producto = fields.Many2one("sonderp.categoria", ondelete="cascade", string="Producto", index=True)
    stock_grupo = fields.Char(String="Categoria", related="stock_producto.categoria_grupo")
    stock_requerido_umbral = fields.Integer(related="stock_producto.categoria_requerido_umbral")
    stock_agotado_umbral = fields.Integer(related="stock_producto.categoria_agotado_umbral")
    stock_state_1 = fields.Selection(related="stock_producto.categoria_state")

    @api.depends('stock_cantidad_enable', 'stock_state_1')
    def _compute_state(self):
        for x in self:
            if x.stock_state_1 == "enable":
                if x.stock_cantidad_enable > x.stock_agotado_umbral:
                    x.stock_state = 'a3'
                elif x.stock_agotado_umbral >= x.stock_cantidad_enable >= 1:
                    x.stock_state = 'a2'
                else:
                    x.stock_state = 'a1'
            else:
                x.stock_state = 'a4'