from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Puppy


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine


app = Flask(__name__)


@app.route("/")
@app.route("/puppies", methods=['GET', 'POST'])
def puppiesFunction():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'GET':
        # Call the method to Get all of the puppies
        return getAllPuppies()
    elif request.method == 'POST':
        # Call the method to make a new puppy
        print("Making a New puppy")

        name = request.args.get('name', '')
        description = request.args.get('description', '')
        print(name)
        print(description)
        return makeANewPuppy(name, description)


# Make app.route() decorator here that takes in an integer id in the URI
@app.route("/puppies/<int:id>", methods=['GET', 'PUT', 'DELETE'])
# Call the method to view a specific puppy
def puppiesFunctionId(id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'GET':
        return getPuppy(id)

# Call the method to edit a specific puppy
    elif request.method == 'PUT':
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        return updatePuppy(id, name, description)

    # Call the method to remove a puppy
    elif request.method == 'DELETE':
        return deletePuppy(id)


def getAllPuppies():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    puppies = session.query(Puppy).all()
    return jsonify(Puppies=[i.serialize for i in puppies])


def getPuppy(id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    puppy = session.query(Puppy).filter_by(id=id).one()
    return jsonify(puppy=puppy.serialize)


def makeANewPuppy(name, description):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    puppy = Puppy(name=name, description=description)
    session.add(puppy)
    session.commit()
    return jsonify(Puppy=puppy.serialize)


def updatePuppy(id, name, description):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    puppy = session.query(Puppy).filter_by(id=id).one()
    if not name:
        puppy.name = name
    if not description:
        puppy.description = description
    session.add(puppy)
    session.commit()
    return "Updated a Puppy with id %s" % id


def deletePuppy(id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    puppy = session.query(Puppy).filter_by(id=id).one()
    session.delete(puppy)
    session.commit()
    return "Removed Puppy with id %s" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
