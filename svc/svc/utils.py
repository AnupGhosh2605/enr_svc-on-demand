from django.db import connection
import datetime



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class AllProcedures:

    @staticmethod
    def getUserWithEmail(email):
        user = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUser @email='{email}'")
            user = cursor.fetchone()
        return user

    @staticmethod
    def getUserWithId(user_id):
        user = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUserWithId @id='{user_id}'")
            user = cursor.fetchone()
        return user

    @staticmethod
    def getUserType(id):
        type = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUserType @id='{id}'")
            type = cursor.fetchone()
        return type

    @staticmethod
    def createUser(li):
        status = False
        query = f"EXEC dbo.addUser @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@password='{li[4]}',@UserTypeId='{li[5]}',@ApplicationId='{li[6]}',@date_joined='{datetime.datetime.now()}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status


    @staticmethod
    def createUserWithType(li):
        status = False
        query = f"EXEC dbo.addUserWithType  @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@password='{li[4]}',@UserType='{li[5]}',@ApplicationId='{li[6]}',@date_joined='{datetime.datetime.now()}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def getChatRecord(client_id, professional_id):
        messages = []
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getChatRecord @client_id='{client_id}', @professional_id='{professional_id}'")
            messages = cursor.fetchall()
        return messages

    @staticmethod
    def createChatRecord(message, client_id, professional_id, room_name, side):
        status = False
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.createChatRecord @time_stamp='{datetime.datetime.now()}', @client_id='{client_id}', @professional_id='{professional_id}', @message='{message}', @room_name='{room_name}', @side='{side}'")
            status = True
        return status

    @staticmethod
    def createjob(TopicName, content, Category, City, User, **kwargs):
        status = False
        id = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.addJobPost @TopicName='{TopicName}', @content='{content}', @TopicDate='{datetime.datetime.now()}', @AddedDate='{datetime.datetime.now()}', @Category_id='{Category}', @City_id='{City}', @User_id='{User}', @AddedBy_id='{User}', @IsActive='True', @IsClose='False', @IsNotification='True'")
            id = cursor.execute('SELECT @@IDENTITY AS [@@IDENTITY];')
            print(id)
            id = id.fetchall()
            status = True
        return status, id[0][0]



    @staticmethod
    def updatejob(id=None, TopicName=None, content=None, Category=None, SubCategory=None, City=None, User=None, AddedBy=None, UpdatedBy=None, IsActive=1, CloseBy=None, IsClose=0, ForceCloseReason=None, ForceCloseCategory=None, IsNotification=1, SMSText=None, WhatsAppText=None):
        status = False
        closeDate = None
        closeBy_id = None
        fc_id = None
        UpdatedBy = User
        if IsNotification=='on':
            IsNotification = 1
        if IsActive=="on":
            IsActive = 1
        if IsClose:
            IsClose = 0
            closeDate = datetime.datetime.now()
            closeBy_id = User
            query = f"EXEC dbo.updateJob @id='{id}', @content='{content}', @TopicName='{TopicName}', @UpdatedDate='{datetime.datetime.now()}', @IsActive='{IsActive}', @IsClose='{IsClose}', @CloseDate='{closeDate}', @ForceCloseReason='{ForceCloseReason}', @IsNotification='{IsNotification}', @SMS='{SMSText}', @whatsApp='{WhatsAppText}', @Category_id='{Category}', @City_id='{City}', @CloseBy_id='{closeBy_id}', @subCat_id='{SubCategory}', @UpdatedBy_id='{UpdatedBy}' "
        else:
            query = f"EXEC dbo.updateJob @id='{id}', @content='{content}', @TopicName='{TopicName}', @UpdatedDate='{datetime.datetime.now()}', @IsActive='{IsActive}', @ForceCloseReason='{ForceCloseReason}', @IsNotification='{IsNotification}', @SMS='{SMSText}', @whatsApp='{WhatsAppText}', @Category_id='{Category}', @City_id='{City}', @subCat_id='{SubCategory}', @UpdatedBy_id='{UpdatedBy}' "
        print(id)
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status


    @staticmethod
    def getjobs():
        with connection.cursor() as cursor:
            alljobs = cursor.execute(f"EXEC dbo.getAllJobs")
        return alljobs


    @staticmethod
    def getCountry():
        with connection.cursor() as cursor:
            country = cursor.execute(f"EXEC dbo.getCountry")
            country = dictfetchall(country)
        return country

    @staticmethod
    def getState():
        with connection.cursor() as cursor:
            state = cursor.execute(f"EXEC dbo.getState")
            state = dictfetchall(state)
        return state

    @staticmethod
    def getCity():
        with connection.cursor() as cursor:
            city = cursor.execute(f"EXEC dbo.getCity")
            city = dictfetchall(city)
        return city

    @staticmethod
    def getCityByState():
        with connection.cursor() as cursor:
            city = cursor.execute(f"EXEC dbo.getCityByState")
            city = dictfetchall(city)
        return city

    @staticmethod
    def addressAddUser(li):
        status = False
        query = f"EXEC dbo.addUserAddressList  @street='{li[0]}',@zip_code='{li[8]}',@added_date='{datetime.datetime.now()}',@user_id='{li[9]}',@city='{li[6]}', @IsActive=1;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def getAddressList():
        with connection.cursor() as cursor:
            address = cursor.execute(f"EXEC dbo.getAddressList")
            address = dictfetchall(address)
        return address

    @staticmethod
    def getProfessionalConnections(user_id):
        connections = None
        with connection.cursor() as cursor:
            cursor.execute(f'EXEC dbo.getProfessionalConnections @professinoal_id="{user_id}"')
            connections = cursor.fetchall()
        return connections


    @staticmethod
    def getClientConnections(user_id):
        connections = None
        with connection.cursor() as cursor:
            cursor.execute(f'EXEC dbo.getClientConnections @client_id="{user_id}"')
            connections = cursor.fetchall()
        return connections

    @staticmethod
    def getUserAddress(user_id):
        address = None
        with connection.cursor() as cursor:
            address = cursor.execute(f"EXEC dbo.getUserAddress @user_id='{user_id}'")
            address = dictfetchall(address)
        return address

    @staticmethod
    def updateUser(li,user_id):
        status = False
        query = f"EXEC dbo.UpdateUser @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@ApplicationId='{li[4]}',@user_id='{user_id}',@street='{li[5]}',@city='{li[8]}',@zip_code='{li[9]}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status



class FastProcedures:
    @staticmethod
    def execute_query(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
        return True

    @staticmethod
    def subcat_query_add(topic_id, subcat_id):
        return f"EXEC dbo.createTopicSubCat @TopidId='{topic_id}', @subCatId='{subcat_id}';"

    @staticmethod
    def asset_query_add(file_name, file_ext, added_date, updated_date, addedby_id, topic_id, updatedby_id):
        return f"EXEC dbo.createTopicAsset @file_name='{file_name}', @file_ext='{file_ext}', @added_date='{added_date}', @updated_date='{updated_date}', @addedby_id='{addedby_id}', @topic_id='{topic_id}', @updatedby_id='{updatedby_id}';"
