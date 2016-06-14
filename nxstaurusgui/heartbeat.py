from taurus.qt.qtgui.panel.taurusvalue import TaurusValue


class TaurusValueHB(TaurusValue):

    def __init__(self, parent=None, designMode=False,
                 customWidgetMap=None, period=1000, attr=None):
        TaurusValue.__init__(self, parent, designMode, customWidgetMap)
        self._attr = attr or 'position'
        self.setEventBufferPeriod(period)

    def setModel(self, model):
        TaurusValue.setModel(self, model + "/" + self._attr)
