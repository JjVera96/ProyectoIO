#-*- coding: utf-8 -*-
import wx
import sys

class ventanaInicio(wx.Frame):
	def __init__ (self, *args, **kwargs):
		super(ventanaInicio, self).__init__(*args, **kwargs)
		self.InitUI()

	def InitUI(self):
		panel = wx.Panel(self)
		self.SetTitle('Investigacion de Operaciones')
		self.SetSize((600,600))
		Titulo = wx.StaticText(panel, -1, "Investigacion De Operaciones", (190,10))
		
		sz=wx.BoxSizer(wx.VERTICAL)
		boton1 = wx.Button(panel,-1, u"Dos Fases")
		boton2 = wx.Button(panel,-1, u"Lagrange")
		boton3 = wx.Button(panel,-1, u"Salir")

		
		sz.Add(boton1,1,wx.EXPAND|wx.ALL,40)
		sz.Add(boton2,1,wx.EXPAND|wx.ALL,40)
		sz.Add(boton3,1,wx.EXPAND|wx.ALL,60)

		self.SetSizer(sz)
		self.Centre()
		self.Show(True)


if __name__ == '__main__':
	app = wx.App()
	ventanaInicio(None)
	app.MainLoop()
