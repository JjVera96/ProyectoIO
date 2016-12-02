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
		self.Centre()
		self.Show(True)


if __name__ == '__main__':
	app = wx.App()
	ventanaInicio(None)
	app.MainLoop()
