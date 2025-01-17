from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from hash import get_shas

# TODO class KeyValLabel
# TODO class KeyValTextInput

class UpdatableLabel(BoxLayout):

	def __initStyle(self):
		self.orientation='horizontal'
		self.width=100

	def __initKey(self,key):
		self.__key=Label(text=key)
		self.add_widget(self.__key)

	def __initVal(self):	
		self.__val=Label()
		self.add_widget(self.__val)

	def updateVal(self,val):
		self.__val.text=val

	def __init__(self, key,**kwargs):
		super(UpdatableLabel, self).__init__(**kwargs)
		self.__initStyle()
		self.__initKey(key)
		self.__initVal()


class MainScreen(BoxLayout):

	def onClearTextChange(self,instance,value):
		hashVals=get_shas(value)
		# print(hashVals)
		for key in self.__outputs:
			self.__outputs[key].updateVal(hashVals[key])

	def __initClearText(self):
		self.clearTextInput = TextInput(multiline=False)
		self.add_widget(self.clearTextInput)
		self.clearTextInput.bind(text=self.onClearTextChange)
	
	def __initHashList(self):
		#"""
		__hashlist=[
			'SHA-1',
			'SHA-224',
			'SHA-256',
			'SHA512-224',
			'SHA3-256',
			'SHA3-512'
		]
		self.__outputs=dict()
		container=BoxLayout(orientation='vertical',padding=(10,10),spacing=10)
		for _h in __hashlist:
			self.__outputs[_h]=UpdatableLabel(_h)
			container.add_widget(self.__outputs[_h])
		self.add_widget(container)
		print(self.__outputs)
		#"""

	def __initLayout(self):
		self.orientation='vertical'
	
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.__initLayout()
		self.__initClearText()
		self.__initHashList()
		
class KiviApp(App):
	def build(self):
		return MainScreen()
