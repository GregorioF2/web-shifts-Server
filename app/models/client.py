from app.models.user import *


class Client(User):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    queuesBeingAttended = db.relationship('ConceptQueue', backref='clients', lazy=True)
    shopQueuesEntries = db.relationship('ConceptQueueEntry', backref='clients', lazy=True)
    shopQueues = db.relationship('ConceptQueue', secondary='concept_queues_entries')

    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'shop_queues': list(map(lambda q: q.id, self.shopQueues)),
        }
