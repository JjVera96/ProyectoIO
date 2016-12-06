import wx
import sys
import wx.grid

cantVar = 0
cantRes = 0
opcionn = ""
Filas = 2
Columnas = 2

class matriz(wx.Frame):   
    def __init__ (self, *args, **kwargs):       
        super(matriz, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Variables')
        self.SetSize((500, 600))
        self.panel = wx.Panel(self)
        self.tabla = wx.grid.Grid(self.panel)
        
        self.tabla.CreateGrid(Filas, Columnas)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.tabla,1,wx.ALIGN_CENTRE|wx.ALL,35)
        self.panel.SetSizer(self.sizer)
        self.bt=wx.Button(self.panel,-1,"Continuar", pos = (220, 500))
        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)
        for i in range(Filas):
           for j in range(Columnas):
            self.tabla.SetCellValue(i, j, '0')
            
        self.Show(True)

    def onContinuar(self, event):
        global opcion
        self.tablero = []
        for i in range(cantRes):
            self.linea = []
            for j in range(cantVar):
                self.linea.append(self.tabla.GetCellValue(i, j))
            self.tablero.append(self.linea)
        
        opcion = self.edit.GetValue()

if __name__ == '__main__':
    app = wx.App()
    matriz(None)
    app.MainLoop()
