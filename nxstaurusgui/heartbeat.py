from taurus.qt.qtgui.panel.taurusvalue import TaurusValue


class TaurusValueHB(TaurusValue):
    """ TaurusValue widget with Heartbeat events
    """
    
    def __init__(self, parent=None, designMode=False,
                 customWidgetMap=None, period=1000, attr=None):
        """ consturctor

        :param parent: parent widget
        :param designMode: taurus design mode
        :param customWidgetMap: (dict<str,Qt.QWidget>) a dictionary whose
                                keys are device class strings 
                                (see :class:`PyTango.DeviceInfo`) and
                                whose values are widget classes to be used
        :param period: heartbeat period
        :param attr: tango device attribute name
        """
        
        TaurusValue.__init__(self, parent, designMode, customWidgetMap)
        self._attr = attr or 'position'
        self.setEventBufferPeriod(period)

    def setModel(self, model):
        """sets the widget model

        :param model: tango device name
        """
        TaurusValue.setModel(self, model + "/" + self._attr)
