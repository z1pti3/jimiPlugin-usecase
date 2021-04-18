import jimi

class _usecase(jimi.db._document):
    name = str()
    description = str()
    usecaseType = str()
    usecaseSubType = str()
    dataSources = str()
    detectionLogic = str()
    detectionStage = str()
    mitreTactics = list()
    tests = list()
    flows = list()

    _dbCollection = jimi.db.db["usecase"]
 
