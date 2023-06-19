from flask import render_template


class SearchResult:
    def __init__(self, data, app):
        self.app = app
        self.data = data
        if not self.data["type"]:
            raise Exception("No type found in data")
        if not self.data["id"]:
            raise Exception("No id found in data")
        self.apo = ActivityPubObject.makeObject(self.data)

    def __str__(self):
        return self.apo.__str__()


class ActivityPubObject:
    @staticmethod
    def makeObject(data):
        if type(data) is not dict:
            return data

        return {
            "Announce": Announce,
            "Collection": Collection,
            "Create": Create,
            "Note": Note,
            "OrderedCollection": OrderedCollection,
            "OrderedCollectionPage": OrderedCollectionPage,
            "Person": Person,
        }.get(data["type"], ActivityPubObject)(data)

    def __init__(self, data):
        self.type = data["type"]
        self.id = data["id"]
        self.data = data

    def hasAttribute(self, item):
        return item in self.data

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]
        else:
            raise AttributeError("Attribute %s not found" % item)

    def __str__(self):
        return render_template('base.jinja2', data=self)

    def __repr__(self):
        return self.__str__()


class Announce(ActivityPubObject):
    def __str__(self):
        print(self.data.keys())
        return render_template('announce.jinja2', data=self)


class Collection(ActivityPubObject):
    def __str__(self):
        print(self.data.keys())
        return render_template('collection.jinja2', data=self)


class CollectionPage(Collection):
    def __init__(self, data):
        super().__init__(data)
        self.first = self.data["first"]
        self.last = self.data["last"]

    def __str__(self):
        print(self.data.keys())
        return render_template('collectionPage.jinja2', data=self)


class Create(ActivityPubObject):
    def __init__(self, data):
        super().__init__(data)
        self.object = ActivityPubObject.makeObject(self.data["object"])

    def __str__(self):
        print(self.data.keys())
        return render_template('create.jinja2', data=self)


class OrderedCollection(Collection):
    def __init__(self, data):
        super().__init__(data)
        self.children = []
        if self.hasAttribute("orderedItems"):
            for item in self.orderedItems:
                self.children.append(ActivityPubObject.makeObject(item))

    def __str__(self):
        print(self.data.keys())
        return render_template('orderedCollection.jinja2', data=self)


class OrderedCollectionPage(OrderedCollection):
    def __str__(self):
        print(self.data.keys())
        return render_template('orderedCollectionPage.jinja2', data=self)


class Person(ActivityPubObject):
    def __str__(self):
        print(self.data.keys())
        return render_template('person.jinja2', data=self)


class Note(ActivityPubObject):
    def __init__(self, data):
        super().__init__(data)
        self.content = self.data["content"]

    def __str__(self):
        print(self.data.keys())
        return render_template('note.jinja2', data=self)