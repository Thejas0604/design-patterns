class ApplicationState:
    instance = None
    def __init__(self):
        self.isLoggedIn = False
    @staticmethod    
    def getState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance
    
appState1 = ApplicationState.getState()
print(appState1.isLoggedIn)
appState1.isLoggedIn = True
appState2 = ApplicationState.getState()
print(appState2.isLoggedIn)
print(appState1==appState2)