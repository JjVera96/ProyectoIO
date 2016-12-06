import wx
import sys
import wx.grid

cantVar = 0
cantRes = 0
opcionn = ""
Filas = 6
Columnas = 0
sol=1
util=0

numero = 0.7
class matriz(wx.Frame):   
    def __init__ (self, *args, **kwargs):       
        super(matriz, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Variables')
        self.SetSize((500, 600))
        self.panel = wx.Panel(self)
        self.Utilidad=wx.StaticText(self.panel,-1,"Utilidad",(190,10))
        self.val=wx.StaticText(self.panel,-1,""+str(util),(190,40))
        

        
        for i in range(Filas):
            self.st1=wx.StaticText(self.panel,-1,"x"+str(i)+" = " + str(numero),(190 ,60*(i+1)))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(self.sizer)
        self.bt=wx.Button(self.panel,-1,"Continuar", pos = (190, 500))
        self.Bind(wx.EVT_BUTTON, self.onContinuar, self.bt)
        self.Show(True)

    def onContinuar(self, event):
        pas3
if __name__ == '__main__':
    app = wx.App()
    matriz(None)
    app.MainLoop()
