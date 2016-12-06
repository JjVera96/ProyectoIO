#-*- coding: utf-8 -*-
import wx
import sys
import wx.grid

cantVar = 0
cantRes = 0
opcionn = ""
Filas = 0
Columnas = 0

class DosFases():
    def __init__(self, matriz):
        self.matriz = matriz
        self.Iniciar()

    def Iniciar(self):
        global Filas
        global Columnas
        self.tabla = []
        for i in range(cantRes+1):
            self.linea = []
            for j in range(cantVar+1):
                self.linea.append(int(self.matriz[i][j]))
            self.tabla.append(self.linea)

        for i in range(cantRes+1):
            if(self.matriz[i][cantVar+1] == "<=" or self.matriz[i][cantVar+1] == "="):
                self.tabla[i].append(1)
                for k in range(cantRes+1):
                    if(i != k):
                        self.tabla[k].append(0)
            if(self.matriz[i][cantVar+1] == ">="):
                self.tabla[i].append(1)
                self.tabla[i].append(1)
                for k in range(cantRes+1):
                    if(i != k):
                        self.tabla[k].append(0)
                        self.tabla[k].append(0)
        Filas = len(self.tabla)
        Columnas = len(self.tabla[0])
        print Filas, Columnas

    def PrimeraFase(self):
        pass

    def SegundaFase(self):
        pass

    def __str__(self):
        cadena = "["
        for i in range(cantRes+1):
            for j in range(cantVar+2):
                cadena += str(self.matriz[i][j]) + ", "
            cadena += "]\n"
        return cadena

class RestriccionesUI(wx.Frame):   
    def __init__ (self, *args, **kwargs):       
        super(RestriccionesUI, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Variables')
        self.SetSize((500, 600))
        self.panel = wx.Panel(self)
        self.tabla = wx.grid.Grid(self.panel)
        self.tabla.CreateGrid(cantRes+1, cantVar+2)
        self.tabla.SetCellValue(0, cantVar+1, 'objetivo')
        self.tabla.SetCellValue(0, cantVar, '0')
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.tabla,1,wx.ALIGN_CENTRE|wx.ALL,35)
        self.panel.SetSizer(self.sizer)
        self.bt=wx.Button(self.panel,-1,"Continuar", pos = (220, 500))
        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)
        self.opcion = ['Max', 'Min']
        self.text = wx.StaticText(self.panel, -1, "Objetivo", (220,400))
        self.edit = wx.ComboBox(self.panel, pos = (220, 450), choices = self.opcion,)
        self.list = ['<=', '=', '>=']
        self.choices=wx.grid.GridCellChoiceEditor(self.list, True)
        for i in range(1, cantRes+1):
            self.tabla.SetCellEditor(i, cantVar+1, self.choices)
        self.Centre()
        self.Show(True)

    def onContinuar(self, event):
        global opcion
        self.tablero = []
        for i in range(cantRes+1):
            self.linea = []
            for j in range(cantVar+2):
                self.linea.append(self.tabla.GetCellValue(i, j))
            self.tablero.append(self.linea)
        matrix = DosFases(self.tablero)
        opcion = self.edit.GetValue()

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
        cantVar = int(self.txt1.GetValue())
        cantRes = int(self.txt2.GetValue())
        RestriccionesUI(None)
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
        global cantVar
        global cantRes
        cantVar = self.txt1.GetValue()
        cantRes = self.txt2.GetValue()
        RestriccionesUI(None)
        self.Destroy()

class ventanaInicio(wx.Frame):
    def __init__ (self, *args, **kwargs):
        super(ventanaInicio, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.SetTitle('Investigacion de Operaciones')
        self.SetSize((600,600))
        self.Titulo = wx.StaticText(self.panel, -1, "Investigacion De Operaciones", (190,10))    
        self.sz=wx.BoxSizer(wx.VERTICAL)
        self.boton1 = wx.Button(self.panel,-1, u"Dos Fases")
        self.boton2 = wx.Button(self.panel,-1, u"Lagrange")
        self.boton3 = wx.Button(self.panel,-1, u"Salir")       
        self.sz.Add(self.boton1,1,wx.EXPAND|wx.ALL,40)
        self.sz.Add(self.boton2,1,wx.EXPAND|wx.ALL,40)
        self.sz.Add(self.boton3,1,wx.EXPAND|wx.ALL,60)
        self.Bind(wx.EVT_BUTTON, self.onClickButton1, self.boton1)
        self.Bind(wx.EVT_BUTTON, self.onClickButton2, self.boton2)
        self.Bind(wx.EVT_BUTTON, self.onQuit, self.boton3)
        self.SetSizer(self.sz)
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