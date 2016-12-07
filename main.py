#-*- coding: utf-8 -*-
import wx
import sys
import wx.grid

cantVar = 0
cantRes = 0
opcion = ""
Filas = 0
Columnas = 0
resultado = []

class enConstruccion(wx.Frame):   
    def __init__ (self, *args, **kwargs):       
        super(enConstruccion, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Resultado')
        self.SetSize((500, 600))
        self.panel = wx.Panel(self)
        self.Utilidad=wx.StaticText(self.panel,-1,"Ventana En Construccion",(190,10))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(self.sizer)
        self.bt=wx.Button(self.panel,-1,"Continuar", pos = (190, 500))
        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)
        self.Centre()
        self.Show(True)

    def onContinuar(self, event):
        ventanaInicio(None)
        self.Destroy()

class ventanaFinal(wx.Frame):   
    def __init__ (self, *args, **kwargs):       
        super(ventanaFinal, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Resultado')
        self.SetSize((500, 600))
        self.panel = wx.Panel(self)
        self.Utilidad=wx.StaticText(self.panel,-1,"Utilidad = "+str(resultado[0]),(190,10))
        for i in range(cantVar):
            self.st1=wx.StaticText(self.panel,-1,"x"+str(i)+" = " + str(resultado[i+1]),(190 ,60*(i+1)))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(self.sizer)
        self.bt=wx.Button(self.panel,-1,"Continuar", pos = (190, 500))
        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)
        self.Centre()
        self.Show(True)

    def onContinuar(self, event):
        ventanaInicio(None)
        self.Destroy()

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
            for j in range(cantVar):
                self.linea.append(float(self.matriz[i][j]))
            self.tabla.append(self.linea)
        for i in range(cantRes+1):
            if(self.matriz[i][cantVar+1] == "<=" or self.matriz[i][cantVar+1] == "="):
                self.tabla[i].append(1)
                for k in range(cantRes+1):
                    if(i != k):
                        self.tabla[k].append(0)
            if(self.matriz[i][cantVar+1] == ">="):
                self.tabla[i].append(1)
                self.tabla[i].append(-1.0)
                for k in range(cantRes+1):
                    if(i != k):
                        self.tabla[k].append(0)
                        self.tabla[k].append(0)
        for i in range(cantRes+1):
            self.tabla[i].append(float(self.matriz[i][cantVar]))
        Filas = len(self.tabla)
        Columnas = len(self.tabla[0])

    def PrimeraFase(self):
        self.tablaPrimera = []
        self.linea = []
        self.arti = []
        self.artj = []
        for i in range(cantVar):
            self.linea.append(0)
        self.tablaPrimera.append(self.linea)
        for i in range(cantRes+1):
            if(self.matriz[i][cantVar+1] == "<="):
                self.tablaPrimera[0].append(0)
            if(self.matriz[i][cantVar+1] == ">="):
                self.tablaPrimera[0].append(-1.0)
                self.tablaPrimera[0].append(0)
                self.arti.append(i)
            if(self.matriz[i][cantVar+1] == "="):
                self.tablaPrimera[0].append(-1.0)
                self.arti.append(i)
        self.tablaPrimera[0].append(0)
        for i in range(1, Filas):
            self.linea = []
            for j in range(Columnas):
                self.linea.append(self.tabla[i][j])
            self.tablaPrimera.append(self.linea)
        for j in range(Columnas):
            if(self.tablaPrimera[0][j] == -1.0):
                self.f1 = self.tablaPrimera[0]
                for i in range(Filas):
                    self.linea = []
                    if(self.tablaPrimera[i][j] == 1):
                        self.artj.append(j)
                        self.f2 = self.tablaPrimera[i]
                        for k in range(Columnas):
                            num = float(self.f1[k]) + float(self.f2[k])
                            self.linea.append(num)
                            self.tablaPrimera[0] = self.linea
        self.SimplexPrimeraParte()

    def SimplexPrimeraParte(self):
        self.posx = 0
        self.posy = 0
        self.infinito = 99999999999
        while(len(self.arti) > 0):
            self.linea = []
            for j in range(Columnas-1):
                self.linea.append(self.tablaPrimera[0][j])
            self.maximo = max(self.linea)
            self.posy = self.linea.index(self.maximo)
            self.division = [self.infinito]
            for i in range(1, Filas):
                self.division.append(self.tablaPrimera[i][Columnas-1]/self.tablaPrimera[i][self.posy])
            self.minimo = min(self.division)
            self.posx = self.division.index(self.minimo)
            self.newarti = []
            for i in self.arti:
                if(int(i) != int(self.posx)):
                    self.newarti.append(i)
            self.arti = self.newarti
            self.DividirPivotePrimeraParte()

    def DividirPivotePrimeraParte(self):
        self.puntopivote = self.tablaPrimera[self.posx][self.posy]
        for j in range(Columnas):
            self.tablaPrimera[self.posx][j] = self.tablaPrimera[self.posx][j]/self.puntopivote
        for i in range(Filas):
            self.multi = self.tablaPrimera[i][self.posy]
            for j in range(Columnas):
                if(i != self.posx):
                    self.tablaPrimera[i][j] = self.tablaPrimera[i][j] - self.multi*self.tablaPrimera[self.posx][j]

    def SegundaFase(self):
        global resultado
        self.tablaSegunda = []
        self.linea = []
        for j in range(cantVar):
            self.linea.append(float(self.matriz[0][j]))
        for j in range(cantVar, Columnas):
            if((j in self.artj)== False):
                self.linea.append(round(self.tablaPrimera[0][j],1))
        self.tablaSegunda.append(self.linea)
        for i in range(1,Filas):
            self.linea =[]
            for j in range(Columnas):
                if((j in self.artj)== False):
                    self.linea.append(round(self.tablaPrimera[i][j],1))
            self.tablaSegunda.append(self.linea)
        self.SimplexSegundaParte()
        for i in range(Filas):
            resultado.append(self.tablaSegunda[i][Columnas-len(self.artj)-1])

    def SimplexSegundaParte(self):
        self.posx = 0
        self.posy = 0
        while(self.HayNegativo()):
            self.linea = []
            for j in range(Columnas-len(self.artj)-1):
                self.linea.append(self.tablaSegunda[0][j])
            self.minimo = min(self.linea)
            self.posy = self.linea.index(self.minimo)
            for i in range(Filas):
                if(self.tablaSegunda[i][self.posy] == 1.0):
                    self.posx = i
            self.pivot = self.tablaSegunda[0][self.posy]*-1
            for j in range(Columnas-len(self.artj)):
                self.tablaSegunda[0][j] = self.tablaSegunda[0][j]+(self.pivot*self.tablaSegunda[self.posx][j])
        while(self.HayPositivo()):
            self.linea = []
            for j in range(len(self.tablaSegunda[0])-1):
                self.linea.append(self.tablaSegunda[0][j])
            self.maximo = max(self.linea)
            self.posy = self.linea.index(self.maximo)
            self.division = [self.infinito]
            for i in range(1, Filas):
                self.result  = self.tablaSegunda[i][Columnas-len(self.artj)-1]/self.tablaSegunda[i][self.posy]
                if(self.result > 0):
                    self.division.append(self.result)
                else:
                    self.division.append(self.infinito)
            self.minimo = min(self.division)
            self.posx = self.division.index(self.minimo)
            self.Gauss()

    def Gauss(self):
        self.puntopivote = self.tablaSegunda[self.posx][self.posy]
        for j in range(Columnas-len(self.artj)-1):
            self.tablaSegunda[self.posx][j] = self.tablaSegunda[self.posx][j]/self.puntopivote
        for i in range(Filas):
            self.multi = self.tablaSegunda[i][self.posy]
            for j in range(Columnas-len(self.artj)):
                if(i != self.posx):
                    self.tablaSegunda[i][j] = self.tablaSegunda[i][j] - self.multi*self.tablaSegunda[self.posx][j]

    def HayNegativo(self):
        bandera = False
        for j in range(len(self.tablaSegunda[0])-1):
            if(self.tablaSegunda[0][j] < 0):
                bandera = True
                break
        return bandera

    def HayPositivo(self):
        bandera = False
        for j in range(len(self.tablaSegunda[0])-1):
            if(self.tablaSegunda[0][j] > 0):
                bandera = True
                break
        return bandera

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
        self.aviso= wx.StaticText(self.panel, -1, "Primero seleccione las restricciones en la ultima columna", (100,200))
        self.edit = wx.ComboBox(self.panel, pos = (220, 450), choices = self.opcion,)
        self.list = ['<=', '=', '>=']
        self.choices=wx.grid.GridCellChoiceEditor(self.list, True)
        for i in range(1, cantRes+1):
            self.tabla.SetCellEditor(i, cantVar+1, self.choices)
        self.Centre()
        self.Show(True)

    def onContinuar(self, event):
        global opcion
        opcion = self.edit.GetValue()
        if(opcion == 'Min'):
            for j in range(cantVar):
                self.dato = float(self.tabla.GetCellValue(0, j))
                self.dato *= -1
                self.tabla.SetCellValue(0,j, str(self.dato))
        self.tablero = []
        for i in range(cantRes+1):
            self.linea = []
            for j in range(cantVar+2):
                self.linea.append(self.tabla.GetCellValue(i, j))
            self.tablero.append(self.linea)
        matrix = DosFases(self.tablero)
        matrix.PrimeraFase()
        matrix.SegundaFase()
        ventanaFinal(None)
        self.Destroy()

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
        self.SetTitle('Algoritmo de LaGrange')
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
        enConstruccion(None)
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