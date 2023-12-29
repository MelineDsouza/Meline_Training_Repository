import configparser

# creating config object for rawconfigparser method of class configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsermail():
        user = config.get('common info','username')
        return user

    @staticmethod
    def getpassword():
        userPass = config.get('common info','password')
        return userPass

