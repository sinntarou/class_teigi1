class UserName:
    def __init__(self, name):
        """

        :type name: object
        """
        if not (4 <= len(name) <=20):
            raise ValueError(f'{name}は文字数のルール違反です！')
        self.name = name

    def screen_name(self):
        return self.name.upper()

#UserNameクラスのインスタンス化
hibiki = UserName(name='hibiki')

#print(hibiki)
#print(type(hibiki))
print(hibiki.screen_name())

#sho = UserName('sho')
# print(sho.name)
