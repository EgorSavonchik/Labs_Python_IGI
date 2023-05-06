from Serializers.serializers_factory import SerializersFactory, SerializerType

Json = SerializersFactory.create_serializer(SerializerType.JSON)
Xml = SerializersFactory.create_serializer(SerializerType.XML)

while (True):
    print('1: get from json')
    print('2: get from xaml')
    print('3: json to xaml')
    print('4: xaml to json')
    
    opt = input()
    
    if (opt == '1'):
        fn = input('Input file name ')
        
        sourse = open(fn, "r")
        data = open("data.json", "w")
        Json.dump(sourse.read(), data)

        sourse.close()
        data.close()

    elif (opt == '2'):
        fn = input('Input file name ')
        
        sourse = open(fn, "r")
        data = open("data.xml", "w")
        Xml.dump(sourse.read(), data)

        sourse.close();
        data.close();

    elif (opt == '3'):
        xml = open("data.xml", "w")
        json = open("data.json", "r")

        obj = Json.load(json)
        Xml.dump(obj, xml)

        xml.close()
        json.close()

    elif (opt == '4'):
        xml = open("data.xml", "r")
        json = open("data.json", "w")

        obj = Xml.load(xml)
        Json.dump(obj, json)

        xml.close()
        json.close()

    else:
        print('incorrect')