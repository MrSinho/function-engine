import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys 
import re
import ast
import concurrent.futures
import traceback

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

from kivymd.uix.textfield import MDTextField, MDTextFieldRect, MDTextFieldRound
from kivy.lang import Builder
from kivy_ import algorithm_helper, variable_helper, point_x_helper, point_y_helper, point_z_helper, start_helper, edges_checkbox, points_checkbox
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.list import ThreeLineListItem, ThreeLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

class App(MDApp): 
    def call_exec_algorithm(self,obj):
        print(self.algorithm_builder.text)     
        print(self.points_x_builder.text, self.points_y_builder.text, self.points_z_builder.text)  
        ln = "\n"
        self.entire_class = f"""
class Simulation(object):
    def __init__({self._class}, *args):
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget() #create a window
        self.window.setGeometry(480, 270, 800, 600) #set the geometry of the window(padding x, padding y, scale x, scale y)
        self.window.setWindowTitle("Simulation")    #set the window title
        self.window.setCameraPosition(distance=30, elevation=100) #set the camera position
        self.window.show() #show the window
        {str(["self."+str(name) for name in self.names_list]).replace("[", "").replace("]", "").replace("'", "")} = {str([str(name) for name in self.names_list]).replace("[", "").replace("]", "").replace("'", "")}
        self.how = how
        self.points_list = [] #create an empty points_list
        self.point_mesh = np.array([
            [0, 0, 0],
            [2, 0, 0],
            [1, 2, 0],
            [1, 1, 1]
        ])
        self.faces = np.array([
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3]
        ])

        {(self.start_builder.text).replace(ln, (ln+"        "))}

    #Update is called once per frame
    def Update(self):
        #here ends the algorithm 
        {self.algorithm_builder.text.replace(ln, (ln+"        "))}
        self.newpoint = (self.{self.points_x_builder.text}, self.{self.points_y_builder.text}, self.{self.points_z_builder.text}) # create a newpoint tuple
        #add the new point to the points list
        self.points_list.append(self.newpoint) #add the tuple to the points_list
        self.points = np.array(self.points_list) #convert the points list to an array of tuples
        self.draw()
    def draw(self):
        if self.how == 1:
            self._point_mesh = gl.GLMeshItem(vertexes = self.point_mesh, faces = self.faces, smooth=False, drawFaces=False, drawEdges=True, edgeColor=(1,1,1,1))
            self._point_mesh.scale(.001, .001, .001)
            self._point_mesh.translate(self.newpoint[0], self.newpoint[1], self.newpoint[2])
            self.window.addItem(self._point_mesh)
        elif self.how == 2:
            try: 
                self.window.removeItem(self.drawpoints)
                #print("removed")
            except Exception: pass
            self.drawpoints = gl.GLLinePlotItem(pos=self.points, width=1, antialias=True) #make a variable to store drawing data(specify the points, set antialiasing)
            self.window.addItem(self.drawpoints) #draw the item
  
    #start properly
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                QtGui.QApplication.instance().exec_()
    #animate and update
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.Update)
        timer.start(10)
        self.start()

if __name__ == "__main__":
    {str(self.call)}
"""
        try:
            print(self.entire_class)
            #Clock.schedule_interval(self.execute_class, 0.1)
            exec(self.entire_class)
            App().run()
        except Exception: traceback.print_exc()
        #exec(self.entire_class)
    
    #def execute_class(self, *args):
    #    try: exec(self.entire_class)
    #    except Exception: traceback.print_exc()

    def confirm_variable(self, obj):
        self.can_add_var = True
        self.screen.remove_widget(self.confirm_button)
        self.screen.remove_widget(self.variable_builder)
        self.screen.remove_widget(self.var_table)
        try: 
            self.variable = self.variable_builder.text.split()
            print(self.variable)
            try: 
                float(self.variable[-1])
                print("can convert to float")
            except Exception: 
                print("Invalid sintax!!")
                self.update_all_widgets()
                return
            if(self.variable[0].isalpha() and self.variable[1].isalpha()): #(self.variable[-1].isalpha() or self.variable[-1].isdigit())):
                self.variables_list.append(self.variable_builder.text)
                self.types_list.append(self.variable[0])
                print(self.types_list)
                self.names_list.append(self.variable[1])
                self.values_list.append(self.variable[-1])
                i = 0
                var_lines = [] 
                for _ in self.variables_list:
                    var_line = "("+'"'+str(self.names_list[i])+'"'+", "+'"'+str(self.types_list[i])+'"'+", "+'"'+str(self.values_list[i])+'"'+")"
                    if i < (len(var_lines)-1): var_line+","
                    var_lines.append(var_line)
                    i += 1
                var_lines = (str(var_lines)).replace("'", "").replace("[", "").replace("]", "")
                print(var_lines)
                self.dinamic_table = 'self.var_table = MDDataTable(check = True, pos_hint={"center_x":0.7, "center_y":0.65}, rows_num = 20, size_hint=(0.2,0.5), column_data=[("Name", dp(30)), ("Type", dp(15)),("Value", dp(15))], row_data=['+var_lines+'])'
                print(self.dinamic_table)
                exec(self.dinamic_table)
                self.var_table.bind(on_check_press = self.add_check_press)
                self.call = f"Simulation({str([str(value) for value in self.values_list])}, {str(self.how)}).animation()".replace("[", "").replace("]", "").replace("'", "")
                self._class = f"self, {str([str(name) for name in self.names_list])}, how".replace("[", "").replace("]", "").replace("'", "")        
                print(self.call)
                print(self._class)
                self.update_all_widgets()
            else: 
                print("Invalid sintax!!")
                self.update_all_widgets()
                return
        except Exception: traceback.print_exc()


    def update_all_widgets(self):
        self.screen.remove_widget(self.algorithm_builder)
        self.screen.remove_widget(self.run_button)
        self.screen.remove_widget(self.add_var_button)
        self.screen.remove_widget(self.remv_var_button)
        self.screen.remove_widget(self.start_builder)
        self.screen.remove_widget(self.points_x_builder)
        self.screen.remove_widget(self.points_y_builder)
        self.screen.remove_widget(self.points_z_builder)

        self.screen.add_widget(self.var_table)
        self.screen.add_widget(self.algorithm_builder)
        self.screen.add_widget(self.start_builder)
        self.screen.add_widget(self.run_button)
        self.screen.add_widget(self.add_var_button)
        self.screen.add_widget(self.remv_var_button)
        self.screen.add_widget(self.points_x_builder)
        self.screen.add_widget(self.points_y_builder)
        self.screen.add_widget(self.points_z_builder)
        self.update_checkbox()

    def add_variable(self, obj):
        if self.can_add_var:
            self.variable_builder = Builder.load_string(variable_helper)
            self.confirm_button = MDRectangleFlatButton(text = "Add", pos_hint={"center_x":0.9,"center_y":0.57},
                                                   on_release=self.confirm_variable)
            self.can_add_var = False
            self.screen.add_widget(self.variable_builder)
            self.screen.add_widget(self.confirm_button)
    
    def add_check_press(self, instance_table, instance_row):
        if(self.can_remv_var == False):
            self.can_remv_var = True
            print(instance_row)
        elif(self.can_remv_var == True):
            self.can_remv_var = False
            print("deselected ", str(instance_row))

    def draw_edges(self):
        if ((not self.edges) or self.points):
            print("edges")
            self.edges = True
            self.points = False
            self.how = "2"
        elif(self.edges or (not self.points)):
            self.draw_points()
        self.update_checkbox()
        

    def draw_points(self):
        if (self.edges or (not self.points)):
            print("points")
            self.points = True
            self.edges = False
            self.how = "1"
        elif((not self.edges) or self.points):
            self.draw_edges()
        self.update_checkbox()

    def update_checkbox(self):
        self.screen.remove_widget(self.edges_checkbox_builder)
        self.screen.remove_widget(self.points_checkbox_builder)
        self.edges_checkbox_builder = Builder.load_string(edges_checkbox)
        self.points_checkbox_builder = Builder.load_string(points_checkbox)
        self.screen.add_widget(self.edges_checkbox_builder)
        self.screen.add_widget(self.points_checkbox_builder)

    def build(self):
        self.how = "2"

        self.can_add_var = True
        self.can_remv_var = False
        self.edges = True
        self.points = False

        Window.size=(1400, 700)
        self.title = "Algorithm Engine"
        self.variables_list = []#"float x = 0.5", "float yy = 3.0", "float z 0", "float c 1", "float y = 0"]
        self.types_list     = []#"float", "float", "float", "float", "float"                               ]
        self.values_list    = []#"0.5", "3.0", "0", "1", "0"                                               ]
        self.names_list     = []#"x", "yy", "z", "c","y"                                                   ]

        #theme
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"

        self.screen = Screen()

        self.run_button = MDRectangleFlatButton(text = "Run", 
                                       pos_hint={"center_x": 0.086, "center_y": 0.317},
                                       on_release = self.call_exec_algorithm)

        self.add_var_button = MDIconButton(icon = "plus", pos_hint={"center_x":0.882, "center_y": 0.71},
                                      on_release = self.add_variable)

        self.remv_var_button = MDIconButton(icon = "minus", pos_hint={"center_x":0.912, "center_y":0.71}) 
            
        self.var_table = MDDataTable(check = True,
                                pos_hint={"center_x":0.7, "center_y":0.55+.1},
                                rows_num = 20,
                                size_hint=(.2,0.5),
                                column_data=[
                                ("Name", dp(30)), 
                                ("Type", dp(15)), 
                                ("Value", dp(15)), 
        ],
                                row_data=[

        ])
        
        self.points_x_builder = Builder.load_string(point_x_helper)
        self.points_y_builder = Builder.load_string(point_y_helper)
        self.points_z_builder = Builder.load_string(point_z_helper)

        #script_builder
        self.algorithm_builder = Builder.load_string(algorithm_helper)
        self.start_builder = Builder.load_string(start_helper)
        self.edges_checkbox_builder = Builder.load_string(edges_checkbox)
        self.points_checkbox_builder = Builder.load_string(points_checkbox)


        #var_table
        self.screen.add_widget(self.var_table)
        #script_builder
        self.screen.add_widget(self.algorithm_builder)
        self.screen.add_widget(self.start_builder)
        self.screen.add_widget(self.edges_checkbox_builder)
        self.screen.add_widget(self.points_checkbox_builder)
        #run_button
        self.screen.add_widget(self.run_button)
        #plus_button
        self.screen.add_widget(self.add_var_button)
        #minus_button
        self.screen.add_widget(self.remv_var_button)
        #points_input
        self.screen.add_widget(self.points_x_builder)
        self.screen.add_widget(self.points_y_builder)
        self.screen.add_widget(self.points_z_builder)
        
        
        return self.screen

if __name__ == "__main__":
    app = App()
    app.run()
        

