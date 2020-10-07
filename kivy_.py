start_helper = '''
MDTextFieldRect:
    text : str(app.file_start)
    hint_text: "Start"
    helper_text: "for some examples: www.sinhographics.com"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.30, "center_y":0.765-.05}
    size_hint_x: .55
    size_hint_y: .27
    width: 300    
    '''

algorithm_helper = '''
MDTextFieldRect:
    text : str(app.file_eq)
    hint_text: "Update is called once per frame"
    helper_text: "for some examples: www.sinhographics.com"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.30, "center_y":0.535-.1}
    size_hint_x: .55
    size_hint_y: .27
    width: 300
    '''

variable_helper = '''
MDTextField:
    #hint_text: "Give a name"
    #helper_text: "rename the variable"
    helper_text_mode: "on_focus"
    #icon_right: "language-python"
    #icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .9, "center_y":0.55+.025}
    size_hint_x: 0.13
    width: 50   
    '''

point_x_helper = '''
MDTextField:
    hint_text: ""
    icon_right: "axis-x-arrow"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": .35-.02, "center_y":0.31-.1}
    size_hint_x: 0.08
    width: 300
'''

point_y_helper = '''
MDTextField:
    hint_text: ""
    icon_right: "axis-y-arrow"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.45-.02, "center_y":0.31-.1}
    size_hint_x: 0.08
    width: 300
'''
point_z_helper = '''
MDTextField:
    hint_text: ""
    icon_right: "axis-z-arrow"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x": 0.55-.02, "center_y":0.31-.1}
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
    pos_hint: {"center_x": 0.2-.06, "center_y":0.31-.092}

'''

points_checkbox = '''
MDCheckbox:
    size_hint: None, None
    size: dp(40), dp(40)
    active: app.points
    on_active:
        app.draw_points()
    pos_hint: {"center_x": 0.25-.04, "center_y":0.31-.092}
'''

toolbar = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["content-save-all", lambda x: app.save_popup()], ["folder", lambda x: app.load_popup()], ["application-import", lambda x: app.imports()]]
            elevation:5
'''

directory_helper = '''
MDTextField:
    hint_text: "Directory"
    #helper_text: "Directory: "
    helper_text_mode: "on_focus"
    icon_right: "folder"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {"center_x":0.5, "center_y":0.5} 
    '''
