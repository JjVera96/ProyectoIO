    # -*- coding: utf-8 -*-
# El viaje del navegante.
# Ejemplo de paso de parámetros entre 2 frames en wxPython.

# Importamos las wx
import wx

# Creamos una clase frame que pide un dato.
class frame_secundario(wx.Frame):
    def __init__(self, parent):
    # Este es el constructor. Darse cuenta que se pasa como 
    # parámetro parent, esto es, la referencia del frame que instancia
    # a esta clase. La guardamos.
        self.padre = parent
    # Llamamos al constructor de la clase de la que hereda.
        wx.Frame.__init__(self, None, -1, title = "Introduce un valor")
    # Creamos un sizer horizontal.
        sizer = wx.BoxSizer( wx.HORIZONTAL )
    # Creamos una caja de texto.
        self.caja_texto = wx.TextCtrl(self, -1)
    # Creamos un botón.
        self.boton = wx.Button(self, -1,"ACEPTAR")
    # Añadimos al sizer la caja y el botón.
        sizer.Add(self.caja_texto, 0, wx.ALL, 5)
        sizer.Add(self.boton, 0, wx.ALL, 5)
    # Incluimos el sizer en el frame.
        self.SetSizer(sizer)
    # Creamos el binding. Cuando se haga click en el 
    # botón se lanzará el manejador de eventos correspondiente.
        self.boton.Bind(wx.EVT_BUTTON, self.OnClickBoton)

  # Manejador de eventos.    
    def OnClickBoton(self, event):
    # Obtenemos datos de la caja de texto.
        dato = self.caja_texto.GetValue()
    # Podríamos escribir directamente en el objeto
    # que se desease.
        self.padre.caja_texto.SetValue(dato)
    # Nos vamos.
        self.Destroy()
   
# Creamos la clase de la ventana principal.    
class frame_principal(wx.Frame):
    def __init__(self):
    # Constructor. Llamamos al constructor de la clase wx.Frame.
        wx.Frame.__init__(self, None, -1, title = 'Ventana Principal')
    # Creamos un sizer horizontal.
        sizer = wx.BoxSizer( wx.HORIZONTAL )
    # Creamos un botón.
        self.boton = wx.Button(self, -1, "Crear Frame Secundario")
    # Creamos una caja de texto de solo lectura.
        self.caja_texto = wx.TextCtrl(self, -1, style = wx.TE_READONLY)
    # Añadimos al sizer la caja y el botón.
        sizer.Add(self.boton, 0, wx.ALL, 5)
        sizer.Add(self.caja_texto, 0, wx.ALL, 5)
    # Asociamos el sizer al frame.
        self.SetSizer(sizer)
    # Creamos el binding. Cuando se haga click en el 
    # botón se lanzará el manejador de eventos correspondiente.
        self.boton.Bind(wx.EVT_BUTTON, self.OnClickBoton)
      
  # Manejador de eventos.    
    def OnClickBoton(self, event):
    # Si se hace click se crea una instancia del frame_secundario.
        frame = frame_secundario(self)
    # Mostramos.
        frame.Show()
       
# Creamos una aplicación wxPython.
aplicacion = wx.PySimpleApp()
# Instanciamos el frame principal.
frame = frame_principal()
# Y por supuesto, no olvidar mostrarlo.
frame.Show()
# Esperamos a capturar eventos.
aplicacion.MainLoop()