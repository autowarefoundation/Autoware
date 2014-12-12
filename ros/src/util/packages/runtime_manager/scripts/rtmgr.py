#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Fri Dec 12 13:21:06 2014
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
		self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
		self.label_5_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Mobile IP"))
		self.label_6_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Tablet IP"))
		self.label_7_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Vehicle IP"))
		self.label_7_copy_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Database IP"))
		self.text_ctrl_ip_a_0 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_4 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_a_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_copy_2 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_a_2 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_1_copy_2 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_a_3 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.text_ctrl_ip_b_0 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_5 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_b_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_copy_3 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_b_2 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_1_copy_3 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_b_3 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.text_ctrl_ip_c_0 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_6 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_c_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_copy_4 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_c_2 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_1_copy_4 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_c_3 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.text_ctrl_ip_d_0 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_6_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_d_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_copy_4_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_d_2 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_4_copy_1_copy_4_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("."))
		self.text_ctrl_ip_d_3 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.button_conn_a = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Connect"))
		self.button_conn_b = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Connect"))
		self.button_conn_c = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Connect"))
		self.button_conn_d = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Connect"))
		self.button_disconn_a = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Disconnect"))
		self.button_disconn_b = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Disconnect"))
		self.button_disconn_c = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Disconnect"))
		self.button_disconn_d = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Disconnect"))
		self.label_1 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("State Check"))
		self.button_statchk_d = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, _("D"))
		self.button_statchk_r = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, _("R"))
		self.button_statchk_b = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, _("B"))
		self.button_statchk_n = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, _("N"))
		self.button_statchk_prog = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, _("Program"))
		self.button_statchk_manu = wx.ToggleButton(self.notebook_1_pane_1, wx.ID_ANY, _("Manual"))
		self.label_13_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Accel"))
		self.label_14_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Brake"))
		self.label_15_copy = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Steer"))
		self.slider_statchk_accel = wx.Slider(self.notebook_1_pane_1, wx.ID_ANY, 0, 0, 100)
		self.slider_statchk_brake = wx.Slider(self.notebook_1_pane_1, wx.ID_ANY, 0, 0, 100)
		self.slider_statchk_steer = wx.Slider(self.notebook_1_pane_1, wx.ID_ANY, 0, -120, 120)
		self.label_11 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Veloc"))
		self.slider_statchk_veloc = wx.Slider(self.notebook_1_pane_1, wx.ID_ANY, 0, 0, 300)
		self.label_12 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Indicator"))
		self.button_statchk_indi_l = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("L"))
		self.button_statchk_indi_r = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("R"))
		self.sizer_6_staticbox = wx.StaticBox(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_16 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Route to"))
		self.text_ctrl_route_to_lat = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.text_ctrl_route_to_lon = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_17 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("from"))
		self.text_ctrl_route_from_lat = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.text_ctrl_route_from_lon = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.button_map = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Map"))
		self.label_error = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Errors : 0"))
		self.sizer_18_staticbox = wx.StaticBox(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_mode = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Mode : P"))
		self.sizer_19_staticbox = wx.StaticBox(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.label_gear = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, _("Gear : D"))
		self.sizer_20_staticbox = wx.StaticBox(self.notebook_1_pane_1, wx.ID_ANY, "")
		self.button_start = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Start"))
		self.button_stop = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Stop"))
		self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
		self.notebook_1_pane_3 = wx.Panel(self.notebook_1, wx.ID_ANY)
		self.tree_ctrl = wx.TreeCtrl(self.notebook_1_pane_3, wx.ID_ANY, style=wx.TR_HAS_BUTTONS | wx.TR_NO_LINES | wx.TR_DEFAULT_STYLE | wx.SUNKEN_BORDER)
		self.button_2 = wx.ToggleButton(self.notebook_1_pane_3, wx.ID_ANY, _("Test"))
		self.notebook_1_pane_4 = wx.Panel(self.notebook_1, wx.ID_ANY)
		self.notebook_1_pane_5 = wx.Panel(self.notebook_1, wx.ID_ANY)
		self.panel_1 = wx.ScrolledWindow(self.notebook_1_pane_5, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
		self.checkbox_camera_pggh3_usb1 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("PointGrey Grasshopper 3 (USB1)"))
		self.checkbox_camera_pggh3_usb2 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("PointGrey Grasshopper 3 (USB2)"))
		self.checkbox_camera_pglb5 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("PointGrey LadyBug 5"))
		self.checkbox_camera_usb_gen = wx.CheckBox(self.panel_1, wx.ID_ANY, _("USB Generic"))
		self.checkbox_camera_ieee1394 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("IEEE1394"))
		self.sizer_13_copy_staticbox = wx.StaticBox(self.panel_1, wx.ID_ANY, _("Cameras"))
		self.checkbox_gnss_javad_d3_tty1 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("Javad Delta 3 (TTY1)"))
		self.sizer_15_copy_2_staticbox = wx.StaticBox(self.panel_1, wx.ID_ANY, _("GNSS"))
		self.checkbox_imu_crossbow_vg440 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("Crossbow vg440"))
		self.sizer_15_copy_1_copy_1_staticbox = wx.StaticBox(self.panel_1, wx.ID_ANY, _("IMU"))
		self.checkbox_lidars_velodyne_hdl_64e = wx.CheckBox(self.panel_1, wx.ID_ANY, _("Velodyne HDL-64e"))
		self.checkbox_lidars_velodyne_hdl_32e = wx.CheckBox(self.panel_1, wx.ID_ANY, _("Velodyne HDL-32e"))
		self.checkbox_lidars_hokuyo_utm30lx_usb1 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("Hokuyo UTM30LX (USB1)"))
		self.checkbox_lidars_hokuyo_utm30lx_usb2 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("Hokuyo UTM30LX (USB2)"))
		self.checkbox_lidars_sick_lms5511 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("SICK LMS511"))
		self.checkbox_lidars_ibeo_8l_single = wx.CheckBox(self.panel_1, wx.ID_ANY, _("IBEO 8L Single"))
		self.sizer_14_copy_1_staticbox = wx.StaticBox(self.panel_1, wx.ID_ANY, _("LIDARs"))
		self.checkbox_other_sensors_xxxx_tty1 = wx.CheckBox(self.panel_1, wx.ID_ANY, _("XXXX (TTY1)"))
		self.sizer_15_copy_1_copy_copy_staticbox = wx.StaticBox(self.panel_1, wx.ID_ANY, _("Other Sensors"))
		self.sizer_23_staticbox = wx.StaticBox(self.panel_1, wx.ID_ANY, _("Drivers"))
		self.checkbox_sensor_fusion = wx.CheckBox(self.notebook_1_pane_5, wx.ID_ANY, _("Sensor Fusion"))
		self.checkbox_rosbag = wx.CheckBox(self.notebook_1_pane_5, wx.ID_ANY, _("ROSBAG"))
		self.sizer_8_staticbox = wx.StaticBox(self.notebook_1_pane_5, wx.ID_ANY, "")
		self.checkbox_auto_probe = wx.CheckBox(self.notebook_1_pane_5, wx.ID_ANY, _("Auto Probe"))
		self.button_probe = wx.Button(self.notebook_1_pane_5, wx.ID_ANY, _("Probe"))
		self.button_calibration = wx.ToggleButton(self.notebook_1_pane_5, wx.ID_ANY, _("Calibration"))
		self.button_tf = wx.ToggleButton(self.notebook_1_pane_5, wx.ID_ANY, _("TF"))
		self.button_rviz = wx.ToggleButton(self.notebook_1_pane_5, wx.ID_ANY, _("Rviz"))
		self.tab_version = wx.Panel(self.notebook_1, wx.ID_ANY)
		self.label_21 = wx.StaticText(self.tab_version, wx.ID_ANY, _("Autoware 1.0"))
		self.bitmap_1 = wx.StaticBitmap(self.tab_version, wx.ID_ANY, wx.NullBitmap)
		self.bitmap_2 = wx.StaticBitmap(self.tab_version, wx.ID_ANY, wx.NullBitmap)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_a_0)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_a_1)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_a_2)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_a_3)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_b_0)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_b_1)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_b_2)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_b_3)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_c_0)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_c_1)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_c_2)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_c_3)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_d_0)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_d_1)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_d_2)
		self.Bind(wx.EVT_TEXT, self.OnTextIp, self.text_ctrl_ip_d_3)
		self.Bind(wx.EVT_BUTTON, self.OnConn, self.button_conn_a)
		self.Bind(wx.EVT_BUTTON, self.OnConn, self.button_conn_b)
		self.Bind(wx.EVT_BUTTON, self.OnConn, self.button_conn_c)
		self.Bind(wx.EVT_BUTTON, self.OnConn, self.button_conn_d)
		self.Bind(wx.EVT_BUTTON, self.OnDisconn, self.button_disconn_a)
		self.Bind(wx.EVT_BUTTON, self.OnDisconn, self.button_disconn_b)
		self.Bind(wx.EVT_BUTTON, self.OnDisconn, self.button_disconn_c)
		self.Bind(wx.EVT_BUTTON, self.OnDisconn, self.button_disconn_d)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnGear, self.button_statchk_d)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnGear, self.button_statchk_r)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnGear, self.button_statchk_b)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnGear, self.button_statchk_n)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnProgManu, self.button_statchk_prog)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnProgManu, self.button_statchk_manu)
		self.Bind(wx.EVT_COMMAND_SCROLL, self.OnScAccel, self.slider_statchk_accel)
		self.Bind(wx.EVT_COMMAND_SCROLL, self.OnScBrake, self.slider_statchk_brake)
		self.Bind(wx.EVT_COMMAND_SCROLL, self.OnScSteer, self.slider_statchk_steer)
		self.Bind(wx.EVT_COMMAND_SCROLL, self.OnScVeloc, self.slider_statchk_veloc)
		self.Bind(wx.EVT_BUTTON, self.OnIndi, self.button_statchk_indi_l)
		self.Bind(wx.EVT_BUTTON, self.OnIndi, self.button_statchk_indi_r)
		self.Bind(wx.EVT_TEXT, self.OnTextRoute, self.text_ctrl_route_to_lat)
		self.Bind(wx.EVT_TEXT, self.OnTextRoute, self.text_ctrl_route_to_lon)
		self.Bind(wx.EVT_TEXT, self.OnTextRoute, self.text_ctrl_route_from_lat)
		self.Bind(wx.EVT_TEXT, self.OnTextRoute, self.text_ctrl_route_from_lon)
		self.Bind(wx.EVT_BUTTON, self.OnMap, self.button_map)
		self.Bind(wx.EVT_BUTTON, self.OnStart, self.button_start)
		self.Bind(wx.EVT_BUTTON, self.OnStop, self.button_stop)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnTest, self.button_2)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_camera_pggh3_usb1)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_camera_pggh3_usb2)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_camera_pglb5)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_camera_usb_gen)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_camera_ieee1394)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_gnss_javad_d3_tty1)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_imu_crossbow_vg440)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_lidars_velodyne_hdl_64e)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_lidars_velodyne_hdl_32e)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_lidars_hokuyo_utm30lx_usb1)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_lidars_hokuyo_utm30lx_usb2)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_lidars_sick_lms5511)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_lidars_ibeo_8l_single)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensingDriver, self.checkbox_other_sensors_xxxx_tty1)
		self.Bind(wx.EVT_CHECKBOX, self.OnSensorFusion, self.checkbox_sensor_fusion)
		self.Bind(wx.EVT_CHECKBOX, self.OnRosbag, self.checkbox_rosbag)
		self.Bind(wx.EVT_CHECKBOX, self.OnAutoProbe, self.checkbox_auto_probe)
		self.Bind(wx.EVT_BUTTON, self.OnProbe, self.button_probe)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnCalib, self.button_calibration)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnTf, self.button_tf)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.OnRviz, self.button_rviz)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle(_("runtime manager"))
		self.button_conn_a.Enable(False)
		self.button_conn_b.Enable(False)
		self.button_conn_c.Enable(False)
		self.button_conn_d.Enable(False)
		self.button_disconn_a.Enable(False)
		self.button_disconn_b.Enable(False)
		self.button_disconn_c.Enable(False)
		self.button_disconn_d.Enable(False)
		self.button_statchk_d.SetMinSize((29, 29))
		self.button_statchk_r.SetMinSize((29, 29))
		self.button_statchk_b.SetMinSize((29, 29))
		self.button_statchk_b.SetValue(1)
		self.button_statchk_n.SetMinSize((29, 29))
		self.button_statchk_manu.SetValue(1)
		self.slider_statchk_accel.SetMinSize((82, 27))
		self.slider_statchk_brake.SetMinSize((82, 27))
		self.slider_statchk_steer.SetMinSize((82, 27))
		self.button_statchk_indi_l.SetMinSize((29, 29))
		self.button_statchk_indi_r.SetMinSize((29, 29))
		self.panel_1.SetScrollRate(10, 10)
		self.label_21.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		self.sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_26 = wx.BoxSizer(wx.VERTICAL)
		sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7 = wx.BoxSizer(wx.VERTICAL)
		sizer_9 = wx.BoxSizer(wx.VERTICAL)
		self.sizer_8_staticbox.Lower()
		sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.VERTICAL)
		self.sizer_23_staticbox.Lower()
		sizer_23 = wx.StaticBoxSizer(self.sizer_23_staticbox, wx.VERTICAL)
		self.sizer_15_copy_1_copy_copy_staticbox.Lower()
		sizer_15_copy_1_copy_copy = wx.StaticBoxSizer(self.sizer_15_copy_1_copy_copy_staticbox, wx.VERTICAL)
		self.sizer_14_copy_1_staticbox.Lower()
		sizer_14_copy_1 = wx.StaticBoxSizer(self.sizer_14_copy_1_staticbox, wx.VERTICAL)
		self.sizer_15_copy_1_copy_1_staticbox.Lower()
		sizer_15_copy_1_copy_1 = wx.StaticBoxSizer(self.sizer_15_copy_1_copy_1_staticbox, wx.VERTICAL)
		self.sizer_15_copy_2_staticbox.Lower()
		sizer_15_copy_2 = wx.StaticBoxSizer(self.sizer_15_copy_2_staticbox, wx.VERTICAL)
		self.sizer_13_copy_staticbox.Lower()
		sizer_13_copy = wx.StaticBoxSizer(self.sizer_13_copy_staticbox, wx.VERTICAL)
		sizer_27 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_4 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
		self.sizer_20_staticbox.Lower()
		sizer_20 = wx.StaticBoxSizer(self.sizer_20_staticbox, wx.HORIZONTAL)
		self.sizer_19_staticbox.Lower()
		sizer_19 = wx.StaticBoxSizer(self.sizer_19_staticbox, wx.HORIZONTAL)
		self.sizer_18_staticbox.Lower()
		sizer_18 = wx.StaticBoxSizer(self.sizer_18_staticbox, wx.HORIZONTAL)
		sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
		self.sizer_6_staticbox.Lower()
		sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
		sizer_10 = wx.BoxSizer(wx.VERTICAL)
		sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_15_copy = wx.BoxSizer(wx.VERTICAL)
		sizer_14_copy = wx.BoxSizer(wx.VERTICAL)
		sizer_32 = wx.BoxSizer(wx.VERTICAL)
		sizer_34 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_33 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_22_copy_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_22_copy_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_22_copy = wx.BoxSizer(wx.VERTICAL)
		sizer_4_copy_4_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_4_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_4_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_4_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_22 = wx.BoxSizer(wx.VERTICAL)
		sizer_22.Add(self.label_5_copy, 1, 0, 0)
		sizer_22.Add(self.label_6_copy, 1, 0, 0)
		sizer_22.Add(self.label_7_copy, 1, 0, 0)
		sizer_22.Add(self.label_7_copy_copy, 1, 0, 0)
		sizer_21.Add(sizer_22, 0, wx.EXPAND, 0)
		sizer_4_copy_2.Add(self.text_ctrl_ip_a_0, 0, 0, 0)
		sizer_4_copy_2.Add(self.label_4_copy_4, 0, 0, 0)
		sizer_4_copy_2.Add(self.text_ctrl_ip_a_1, 0, 0, 0)
		sizer_4_copy_2.Add(self.label_4_copy_copy_2, 0, 0, 0)
		sizer_4_copy_2.Add(self.text_ctrl_ip_a_2, 0, 0, 0)
		sizer_4_copy_2.Add(self.label_4_copy_1_copy_2, 0, 0, 0)
		sizer_4_copy_2.Add(self.text_ctrl_ip_a_3, 0, 0, 0)
		sizer_22_copy.Add(sizer_4_copy_2, 1, wx.EXPAND, 0)
		sizer_4_copy_3.Add(self.text_ctrl_ip_b_0, 0, 0, 0)
		sizer_4_copy_3.Add(self.label_4_copy_5, 0, 0, 0)
		sizer_4_copy_3.Add(self.text_ctrl_ip_b_1, 0, 0, 0)
		sizer_4_copy_3.Add(self.label_4_copy_copy_3, 0, 0, 0)
		sizer_4_copy_3.Add(self.text_ctrl_ip_b_2, 0, 0, 0)
		sizer_4_copy_3.Add(self.label_4_copy_1_copy_3, 0, 0, 0)
		sizer_4_copy_3.Add(self.text_ctrl_ip_b_3, 0, 0, 0)
		sizer_22_copy.Add(sizer_4_copy_3, 1, wx.EXPAND, 0)
		sizer_4_copy_4.Add(self.text_ctrl_ip_c_0, 0, 0, 0)
		sizer_4_copy_4.Add(self.label_4_copy_6, 0, 0, 0)
		sizer_4_copy_4.Add(self.text_ctrl_ip_c_1, 0, 0, 0)
		sizer_4_copy_4.Add(self.label_4_copy_copy_4, 0, 0, 0)
		sizer_4_copy_4.Add(self.text_ctrl_ip_c_2, 0, 0, 0)
		sizer_4_copy_4.Add(self.label_4_copy_1_copy_4, 0, 0, 0)
		sizer_4_copy_4.Add(self.text_ctrl_ip_c_3, 0, 0, 0)
		sizer_22_copy.Add(sizer_4_copy_4, 1, wx.EXPAND, 0)
		sizer_4_copy_4_copy.Add(self.text_ctrl_ip_d_0, 0, 0, 0)
		sizer_4_copy_4_copy.Add(self.label_4_copy_6_copy, 0, 0, 0)
		sizer_4_copy_4_copy.Add(self.text_ctrl_ip_d_1, 0, 0, 0)
		sizer_4_copy_4_copy.Add(self.label_4_copy_copy_4_copy, 0, 0, 0)
		sizer_4_copy_4_copy.Add(self.text_ctrl_ip_d_2, 0, 0, 0)
		sizer_4_copy_4_copy.Add(self.label_4_copy_1_copy_4_copy, 0, 0, 0)
		sizer_4_copy_4_copy.Add(self.text_ctrl_ip_d_3, 0, 0, 0)
		sizer_22_copy.Add(sizer_4_copy_4_copy, 1, wx.EXPAND, 0)
		sizer_21.Add(sizer_22_copy, 0, wx.EXPAND, 0)
		sizer_22_copy_1.Add(self.button_conn_a, 1, 0, 0)
		sizer_22_copy_1.Add(self.button_conn_b, 1, 0, 0)
		sizer_22_copy_1.Add(self.button_conn_c, 1, 0, 0)
		sizer_22_copy_1.Add(self.button_conn_d, 1, 0, 0)
		sizer_21.Add(sizer_22_copy_1, 0, wx.EXPAND, 0)
		sizer_22_copy_2.Add(self.button_disconn_a, 1, wx.EXPAND, 0)
		sizer_22_copy_2.Add(self.button_disconn_b, 1, wx.EXPAND, 0)
		sizer_22_copy_2.Add(self.button_disconn_c, 1, wx.EXPAND, 0)
		sizer_22_copy_2.Add(self.button_disconn_d, 1, wx.EXPAND, 0)
		sizer_21.Add(sizer_22_copy_2, 1, wx.EXPAND, 0)
		sizer_2.Add(sizer_21, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 4)
		sizer_3.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_33.Add(self.button_statchk_d, 1, wx.EXPAND, 0)
		sizer_33.Add(self.button_statchk_r, 1, wx.EXPAND, 0)
		sizer_33.Add(self.button_statchk_b, 1, wx.EXPAND, 0)
		sizer_33.Add(self.button_statchk_n, 1, wx.EXPAND, 0)
		sizer_32.Add(sizer_33, 1, wx.EXPAND, 0)
		sizer_34.Add(self.button_statchk_prog, 1, wx.EXPAND, 0)
		sizer_34.Add(self.button_statchk_manu, 1, wx.EXPAND, 0)
		sizer_32.Add(sizer_34, 1, wx.EXPAND, 0)
		sizer_6.Add(sizer_32, 0, wx.EXPAND, 0)
		sizer_14_copy.Add(self.label_13_copy, 1, 0, 0)
		sizer_14_copy.Add(self.label_14_copy, 1, 0, 0)
		sizer_14_copy.Add(self.label_15_copy, 1, 0, 0)
		sizer_6.Add(sizer_14_copy, 0, wx.LEFT | wx.EXPAND, 4)
		sizer_15_copy.Add(self.slider_statchk_accel, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_15_copy.Add(self.slider_statchk_brake, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_15_copy.Add(self.slider_statchk_steer, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_6.Add(sizer_15_copy, 1, wx.EXPAND, 0)
		sizer_11.Add(self.label_11, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_11.Add(self.slider_statchk_veloc, 1, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_10.Add(sizer_11, 1, wx.LEFT | wx.EXPAND, 2)
		sizer_12.Add(self.label_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_12.Add(self.button_statchk_indi_l, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_12.Add(self.button_statchk_indi_r, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_10.Add(sizer_12, 1, wx.LEFT | wx.EXPAND, 4)
		sizer_6.Add(sizer_10, 1, wx.EXPAND, 0)
		sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
		sizer_2.Add(sizer_3, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 4)
		sizer_16.Add(self.label_16, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_16.Add(self.text_ctrl_route_to_lat, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_16.Add(self.text_ctrl_route_to_lon, 0, 0, 0)
		sizer_16.Add(self.label_17, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_16.Add(self.text_ctrl_route_from_lat, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_16.Add(self.text_ctrl_route_from_lon, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_16.Add(self.button_map, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_2.Add(sizer_16, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 4)
		sizer_18.Add(self.label_error, 0, 0, 0)
		sizer_17.Add(sizer_18, 1, wx.EXPAND, 0)
		sizer_19.Add(self.label_mode, 0, 0, 0)
		sizer_17.Add(sizer_19, 1, wx.EXPAND, 0)
		sizer_20.Add(self.label_gear, 0, 0, 0)
		sizer_17.Add(sizer_20, 1, wx.EXPAND, 0)
		sizer_17.Add(self.button_start, 0, wx.EXPAND, 0)
		sizer_17.Add(self.button_stop, 0, wx.EXPAND, 0)
		sizer_2.Add(sizer_17, 1, wx.ALL | wx.EXPAND, 4)
		self.notebook_1_pane_1.SetSizer(sizer_2)
		self.notebook_1_pane_2.SetSizer(sizer_4)
		sizer_27.Add(self.tree_ctrl, 2, wx.ALL | wx.EXPAND, 4)
		sizer_27.Add(self.button_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 4)
		self.notebook_1_pane_3.SetSizer(sizer_27)
		sizer_13_copy.Add(self.checkbox_camera_pggh3_usb1, 0, 0, 0)
		sizer_13_copy.Add(self.checkbox_camera_pggh3_usb2, 0, 0, 0)
		sizer_13_copy.Add(self.checkbox_camera_pglb5, 0, 0, 0)
		sizer_13_copy.Add(self.checkbox_camera_usb_gen, 0, 0, 0)
		sizer_13_copy.Add(self.checkbox_camera_ieee1394, 0, 0, 0)
		sizer_23.Add(sizer_13_copy, 0, wx.LEFT | wx.TOP | wx.EXPAND, 3)
		sizer_15_copy_2.Add(self.checkbox_gnss_javad_d3_tty1, 0, 0, 0)
		sizer_23.Add(sizer_15_copy_2, 0, wx.LEFT | wx.TOP | wx.EXPAND, 4)
		sizer_15_copy_1_copy_1.Add(self.checkbox_imu_crossbow_vg440, 0, 0, 0)
		sizer_23.Add(sizer_15_copy_1_copy_1, 0, wx.LEFT | wx.TOP | wx.BOTTOM | wx.EXPAND, 4)
		sizer_14_copy_1.Add(self.checkbox_lidars_velodyne_hdl_64e, 0, 0, 0)
		sizer_14_copy_1.Add(self.checkbox_lidars_velodyne_hdl_32e, 0, 0, 0)
		sizer_14_copy_1.Add(self.checkbox_lidars_hokuyo_utm30lx_usb1, 0, 0, 0)
		sizer_14_copy_1.Add(self.checkbox_lidars_hokuyo_utm30lx_usb2, 0, 0, 0)
		sizer_14_copy_1.Add(self.checkbox_lidars_sick_lms5511, 0, 0, 0)
		sizer_14_copy_1.Add(self.checkbox_lidars_ibeo_8l_single, 0, 0, 0)
		sizer_23.Add(sizer_14_copy_1, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 4)
		sizer_15_copy_1_copy_copy.Add(self.checkbox_other_sensors_xxxx_tty1, 0, 0, 0)
		sizer_23.Add(sizer_15_copy_1_copy_copy, 0, wx.ALL | wx.EXPAND, 4)
		self.panel_1.SetSizer(sizer_23)
		sizer_5.Add(self.panel_1, 1, wx.EXPAND, 0)
		sizer_8.Add(self.checkbox_sensor_fusion, 0, wx.LEFT | wx.RIGHT | wx.TOP, 4)
		sizer_8.Add(self.checkbox_rosbag, 0, wx.ALL, 4)
		sizer_7.Add(sizer_8, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 4)
		sizer_9.Add(self.checkbox_auto_probe, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 4)
		sizer_9.Add(self.button_probe, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 4)
		sizer_9.Add(self.button_calibration, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 4)
		sizer_9.Add(self.button_tf, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 4)
		sizer_9.Add(self.button_rviz, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 4)
		sizer_7.Add(sizer_9, 1, wx.TOP | wx.EXPAND, 20)
		sizer_5.Add(sizer_7, 0, wx.LEFT | wx.EXPAND, 4)
		self.notebook_1_pane_5.SetSizer(sizer_5)
		sizer_26.Add(self.label_21, 1, wx.LEFT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 4)
		sizer_26.Add(self.bitmap_1, 1, wx.LEFT | wx.TOP, 4)
		sizer_26.Add(self.bitmap_2, 1, wx.LEFT | wx.TOP, 4)
		self.tab_version.SetSizer(sizer_26)
		self.notebook_1.AddPage(self.notebook_1_pane_1, _("Main"))
		self.notebook_1.AddPage(self.notebook_1_pane_2, _("Actuation"))
		self.notebook_1.AddPage(self.notebook_1_pane_3, _("Computing"))
		self.notebook_1.AddPage(self.notebook_1_pane_4, _("Database"))
		self.notebook_1.AddPage(self.notebook_1_pane_5, _("Sensing"))
		self.notebook_1.AddPage(self.tab_version, _("Version"))
		self.sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
		self.SetSizer(self.sizer_1)
		self.sizer_1.Fit(self)
		self.Layout()
		# end wxGlade

	def OnTextIp(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnTextIp' not implemented!"
		event.Skip()

	def OnConn(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnConn' not implemented!"
		event.Skip()

	def OnDisconn(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnDisconn' not implemented!"
		event.Skip()

	def OnGear(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnGear' not implemented!"
		event.Skip()

	def OnProgManu(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnProgManu' not implemented!"
		event.Skip()

	def OnScAccel(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnScAccel' not implemented!"
		event.Skip()

	def OnScBrake(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnScBrake' not implemented!"
		event.Skip()

	def OnScSteer(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnScSteer' not implemented!"
		event.Skip()

	def OnScVeloc(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnScVeloc' not implemented!"
		event.Skip()

	def OnIndi(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnIndi' not implemented!"
		event.Skip()

	def OnTextRoute(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnTextRoute' not implemented!"
		event.Skip()

	def OnMap(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnMap' not implemented!"
		event.Skip()

	def OnStart(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnStart' not implemented!"
		event.Skip()

	def OnStop(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnStop' not implemented!"
		event.Skip()

	def OnTest(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnTest' not implemented!"
		event.Skip()

	def OnSensingDriver(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnSensingDriver' not implemented!"
		event.Skip()

	def OnSensorFusion(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnSensorFusion' not implemented!"
		event.Skip()

	def OnRosbag(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnRosbag' not implemented!"
		event.Skip()

	def OnAutoProbe(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnAutoProbe' not implemented!"
		event.Skip()

	def OnProbe(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnProbe' not implemented!"
		event.Skip()

	def OnCalib(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnCalib' not implemented!"
		event.Skip()

	def OnTf(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnTf' not implemented!"
		event.Skip()

	def OnRviz(self, event):  # wxGlade: MyFrame.<event_handler>
		print "Event handler 'OnRviz' not implemented!"
		event.Skip()

# end of class MyFrame

class MyDialog(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyDialog.__init__
		kwds["style"] = wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.panel_2 = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
		self.radio_box = wx.RadioBox(self.panel_2, wx.ID_ANY, "", choices=[_("0"), _("1"), _("2"), _("3")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
		self.button_1 = wx.Button(self, wx.ID_ANY, _("OK"))
		self.button_1_copy = wx.Button(self, wx.ID_ANY, _("Cancel"))

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self.OnOk, self.button_1)
		self.Bind(wx.EVT_BUTTON, self.OnCancel, self.button_1_copy)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyDialog.__set_properties
		self.SetSize((258, 212))
		self.radio_box.SetSelection(0)
		self.panel_2.SetScrollRate(10, 10)
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyDialog.__do_layout
		sizer_13 = wx.BoxSizer(wx.VERTICAL)
		sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_14.Add(self.radio_box, 1, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 4)
		self.panel_2.SetSizer(sizer_14)
		sizer_13.Add(self.panel_2, 1, wx.EXPAND, 0)
		sizer_15.Add(self.button_1, 0, wx.ALL, 4)
		sizer_15.Add(self.button_1_copy, 0, wx.ALL, 4)
		sizer_13.Add(sizer_15, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		self.SetSizer(sizer_13)
		self.Layout()
		# end wxGlade

	def OnOk(self, event):  # wxGlade: MyDialog.<event_handler>
		print "Event handler 'OnOk' not implemented!"
		event.Skip()

	def OnCancel(self, event):  # wxGlade: MyDialog.<event_handler>
		print "Event handler 'OnCancel' not implemented!"
		event.Skip()

# end of class MyDialog
class MyApp(wx.App):
	def OnInit(self):
		wx.InitAllImageHandlers()
		frame_1 = MyFrame(None, wx.ID_ANY, "")
		self.SetTopWindow(frame_1)
		frame_1.Show()
		return 1

# end of class MyApp

if __name__ == "__main__":
	gettext.install("app") # replace with the appropriate catalog name

	app = MyApp(0)
	app.MainLoop()