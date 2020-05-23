#浏览图书管理系统
#主要功能有：
#1.添加图书（书名、作者、推荐语、借阅状态）
#2.查寻图书
#3.借阅图书（未借阅的图书允许被借阅）
#4.归还图书（归还图书后状态改为未借阅）

class Book:

    #记录书籍信息
    def __init__(self,name,author,comment,state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    #打印书籍信息
    def __str__(self):
        if self.state == 0:
            status = '未借出'

        else:
            status = "已借出"

        return '书名：《%s》\n作者：《%s》\n推荐语：%s\n状态：%s' %(self.name,self.author,self.comment,status)


class BookManager:

    books = []

    def __init__(self):
        #初始化添加书籍
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)

        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        #显示菜单功能
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while 1:
            print('【1】查询所有图书\n【2】添加书籍\n【3】借阅书籍\n【4】归还书籍\n【5】退出系统')
            choice = input('请输入你想使用的功能对应的数字：')
            if choice == '1':
                #调用查询功能
                print('所有书籍展示如下：\n')
                self.show_all_book()

            elif choice =='2':
                #调用添加书籍功能
                self.add_book()


            elif choice =='3':
                self.lend_book()

            elif choice =='4':
                #调用归还书籍功能
                self.return_book()

            elif choice =='5':
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break

            else:
                print('输入有误，请输入功能对应的数字！！')

    def show_all_book(self):
        #展示所有图书信息
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        #添加图书
        name = input('请输入书籍名称：')
        author = input('请输入书籍作者：')
        comment =input('请输入推荐语：')
        newbook = Book(name,author,comment)
        self.books.append(newbook)

    def lend_book(self):
        #借阅图书
        name = input('请输入你想借阅的图书名称：')
        res = self.cheak_book(name)

        if res != None:
            if res.state == 0:
                print('借阅成功')
                res.state = 1

            else:
                print('借阅失败，图书《%s》已被借阅 '% res.name)

        else:
            print('对不起，书库中暂无此书。')

    #在书库中查询有没有此书
    def cheak_book(self,name):
        for book in self.books:
            if book.name == name:
                return book

        else:
            return None


    def return_book(self):
        #归还图书
        name = input('请输入你想归还的图书名称：')
        res = self.cheak_book(name)

        if res != None:
            if res.state == 1:
                print('图书《%s》归还成功'%res.name)
                res.state = 0

            else:
                print('你并没有借阅过此书，你是不是记错了？')

        else:
            print('图书名称输入有误，书库中并无此书')

book = BookManager()
book.menu()