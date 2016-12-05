#-*- coding: utf-8 -*-
import wx
import sys

class NumeroVariables(wx.Frame):
    def __init__ (self, *args, **kwargs):
        super(NumeroVariables, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Investigacion de Operaciones')
        self.SetSize((400,400))
        Titulo = wx.StaticText(self, -1, "Investigacion De Operaciones", (190,10))

        p1=wx.Panel(self)
        p2=wx.Panel(self)
        
       

        mainsz = wx.BoxSizer(wx.VERTICAL)
        p1sz = wx.BoxSizer(wx.VERTICAL)
        p2sz = wx.BoxSizer(wx.VERTICAL)


        st1=wx.StaticText(p1,-1,"Inserte El Numero De Variables",(0,10))
        txt1=wx.TextCtrl(p1,-1)
        st2=wx.StaticText(p2,-1,"Inserte El Numero De Restricciones")
        txt2=wx.TextCtrl(p2,-1)
        bt=wx.Button(self,-1,"Continuar")

        

        p1sz.Add(st1,1,wx.EXPAND|wx.ALL,10)
        p1sz.Add(txt1,1,wx.EXPAND|wx.ALL,10)
        p2sz.Add(st2,1,wx.EXPAND|wx.ALL,10)
        p2sz.Add(txt2,1,wx.EXPAND|wx.ALL,10)
        mainsz.Add(p1,1,wx.EXPAND)
        mainsz.Add(p2,1,wx.EXPAND)
        mainsz.Add(bt,1,wx.ALIGN_CENTRE|wx.ALL,30)

        p1.SetSizer(p1sz)
        p2.SetSizer(p2sz)
        


        self.SetSizer(mainsz)
        self.Centre()
        self.Show(True)


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

        self.SetSizer(sz)
        self.Centre()
        self.Show(True)

    def  onClickButton1(self,event):
         NumeroVariables(None)
       
    def onClickButton2(self,event):
        print "Lagrange"



if __name__ == '__main__':
    app = wx.App()
    ventanaInicio(None)
    app.MainLoop()
