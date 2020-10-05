start_helper = """
MDTextFieldRect:
    hint_text: "func Start"
    helper_text: "for some examples: www.sinhographics.com"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.30, "center_y":0.765}
    size_hint_x: .55
    size_hint_y: .22
    width: 300    
    """

algorithm_helper = """
MDTextFieldRect:
    hint_text: "func Update"
    helper_text: "for some examples: www.sinhographics.com"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.30, "center_y":0.535}
    size_hint_x: .55
    size_hint_y: .22
    width: 300
    """

variable_helper = """
MDTextField:
    #hint_text: "Give a name"
    #helper_text: "rename the variable"
    helper_text_mode: "on_focus"
    #icon_right: "language-python"
    #icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .9, "center_y":0.65}
    size_hint_x: 0.13
    width: 50   
    """

point_x_helper = """
MDTextField:
    hint_text: ""
    icon_right: "axis-x-arrow"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .35, "center_y":0.31}
    size_hint_x: 0.08
    width: 300
"""

point_y_helper = '''
MDTextField:
    hint_text: ""
    icon_right: "axis-y-arrow"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.45, "center_y":0.31}
    size_hint_x: 0.08
    width: 300
'''
point_z_helper = '''
MDTextField:
    hint_text: ""
    icon_right: "axis-z-arrow"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.55, "center_y":0.31}
    size_hint_x: 0.08
    width: 300
'''

edges_checkbox = '''
MDCheckbox:
    size_hint: None, None
    size: dp(40), dp(40)
    active: app.edges
    on_active:
        app.draw_edges()
    pos_hint: {"center_x": 0.2, "center_y":0.31}

'''

points_checkbox = '''
MDCheckbox:
    size_hint: None, None
    size: dp(40), dp(40)
    active: app.points
    on_active:
        app.draw_points()
    pos_hint: {"center_x": 0.25, "center_y":0.31}
'''
