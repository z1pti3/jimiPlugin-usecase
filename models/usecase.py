import jimi

class _usecase(jimi.db._document):
    name = str()
    description = str()
    usecaseType = str()
    usecaseSubType = str()
    dataSources = list()
    detectionLogic = str()
    detectionStages = list()
    mitreTactics = list()
    passTestEvents = list()
    failedTestEvents = list()
    triggers = list()

    _dbCollection = jimi.db.db["usecase"]
 
