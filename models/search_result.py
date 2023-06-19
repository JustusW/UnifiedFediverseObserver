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
        return {
            "OrderedCollection": OrderedCollection,
            "Announce": Announce,
            "Note": Note,
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
        name = self.__class__.__name__
        if self.type != name:
            name += ":%s" % self.type
        else:
            name = ":" + name
        return "%s: %s (%s)\r\n" % (name, self.id, self.data.keys())

    def __repr__(self):
        return self.__str__()


class OrderedCollection(ActivityPubObject):
    def __init__(self, data):
        super().__init__(data)
        self.children = []
        if self.hasAttribute("orderedItems"):
            for item in self.orderedItems:
                self.children.append(ActivityPubObject.makeObject(item))

    def __str__(self):
        print(self.data.keys())
        return render_template('orderedCollection.jinja2', data=self)


class Note(ActivityPubObject):
    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        print(self.data.keys())
        return render_template('note.jinja2', data=self)


class Announce(ActivityPubObject):
    def __str__(self):
        print(self.data.keys())
        return render_template('announce.jinja2', data=self)
