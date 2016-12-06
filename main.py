#-*- coding: utf-8 -*-
import wx
import sys

cantVar = 0
cantRes = 0

class IntermedioUI(wx.Frame):
    
    def __init__ (self, *args, **kwargs):       
        super(IntermedioUI, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Pidiendo')
        self.SetSize((400,400))
        print cantVar, cantRes
        self.Centre()
        self.Show(True)


class DosFasesUI(wx.Frame):
    
    def __init__ (self, *args, **kwargs):       
        super(DosFasesUI, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Metodo Dos Fases')
        self.SetSize((400,400))
        self.Titulo = wx.StaticText(self, -1, "Investigacion De Operaciones", (190,10))

        self.p1=wx.Panel(self)
        self.p2=wx.Panel(self)
        
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.p1sz = wx.BoxSizer(wx.VERTICAL)
        self.p2sz = wx.BoxSizer(wx.VERTICAL)

        self.st1=wx.StaticText(self.p1,-1,"Inserte El Numero De Variables",(0,10))
        self.txt1=wx.TextCtrl(self.p1,-1)
        self.st2=wx.StaticText(self.p2,-1,"Inserte El Numero De Restricciones")
        self.txt2=wx.TextCtrl(self.p2,-1)
        self.bt=wx.Button(self,-1,"Continuar")

        self.p1sz.Add(self.st1,1,wx.EXPAND|wx.ALL,10)
        self.p1sz.Add(self.txt1,1,wx.EXPAND|wx.ALL,10)
        self.p2sz.Add(self.st2,1,wx.EXPAND|wx.ALL,10)
        self.p2sz.Add(self.txt2,1,wx.EXPAND|wx.ALL,10)
        self.mainsz.Add(self.p1,1,wx.EXPAND)
        self.mainsz.Add(self.p2,1,wx.EXPAND)
        self.mainsz.Add(self.bt,1,wx.ALIGN_CENTRE|wx.ALL,30)

        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)

        self.p1.SetSizer(self.p1sz)
        self.p2.SetSizer(self.p2sz)

        self.SetSizer(self.mainsz)
        self.Centre()
        self.Show(True)

    def onContinuar(self, event):
        global cantVar 
        global cantRes
        cantVar = self.txt1.GetValue()
        cantRes = self.txt2.GetValue()
        IntermedioUI(None)
        self.Destroy()

class LagrangeUI(wx.Frame):
    def __init__ (self, *args, **kwargs):
        super(LagrangeUI, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Metodo Dos Fases')
        self.SetSize((400,400))
        self.Titulo = wx.StaticText(self, -1, "Investigacion De Operaciones", (190,10))

        self.p1=wx.Panel(self)
        self.p2=wx.Panel(self)
        
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.p1sz = wx.BoxSizer(wx.VERTICAL)
        self.p2sz = wx.BoxSizer(wx.VERTICAL)

        self.st1=wx.StaticText(self.p1,-1,"Inserte El Numero De Variables",(0,10))
        self.txt1=wx.TextCtrl(self.p1,-1)
        self.st2=wx.StaticText(self.p2,-1,"Inserte El Numero De Restricciones")
        self.txt2=wx.TextCtrl(self.p2,-1)
        self.bt=wx.Button(self,-1,"Continuar")

        self.p1sz.Add(self.st1,1,wx.EXPAND|wx.ALL,10)
        self.p1sz.Add(self.txt1,1,wx.EXPAND|wx.ALL,10)
        self.p2sz.Add(self.st2,1,wx.EXPAND|wx.ALL,10)
        self.p2sz.Add(self.txt2,1,wx.EXPAND|wx.ALL,10)
        self.mainsz.Add(self.p1,1,wx.EXPAND)
        self.mainsz.Add(self.p2,1,wx.EXPAND)
        self.mainsz.Add(self.bt,1,wx.ALIGN_CENTRE|wx.ALL,30)

        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)

        self.p1.SetSizer(self.p1sz)
        self.p2.SetSizer(self.p2sz)

        self.SetSizer(self.mainsz)
        self.Centre()

    def onContinuar(self, event):
        cantVar = self.txt1.GetValue()
        cantRes = self.txt2.GetValue()

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

        self.Bind(wx.EVT_BUTTON, self.onClickButton1,boton1)
        self.Bind(wx.EVT_BUTTON, self.onClickButton2,boton2)
        self.Bind(wx.EVT_BUTTON, self.onQuit, boton3)

        self.SetSizer(sz)
        self.Centre()
        self.Show(True)

    def  onClickButton1(self,event):
        DosFasesUI(None)
        self.Destroy()
       
    def onClickButton2(self,event):
        LagrangeUI(None)
        self.Destroy()

    def onQuit(self,event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    ventanaInicio(None)
    app.MainLoop()
